import os
import logging
from flask import Flask, render_template, redirect, url_for, flash, request, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import DeclarativeBase
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_wtf.csrf import CSRFProtect
import json
from extensions import db, csrf

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create database base class
#class Base(DeclarativeBase):
 #   pass

# Initialize database
#db = SQLAlchemy(model_class=Base)

# Initialize CSRF protection
#csrf = CSRFProtect()


# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)  # needed for url_for to generate with https

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Vinny%401998@localhost:5432/careerguidefinal"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database with the app
db.init_app(app)

# Initialize CSRF protection
csrf.init_app(app)

# Initialize flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import models after db is defined to avoid circular imports
with app.app_context():
    from models import User, AssessmentResult, CareerPath, SavedCareer, AdminUser
    import career_data
    from careerbot import get_bot_response
    from recommendation import get_career_recommendations
    from assessment import get_assessment_questions, process_assessment_results
    
    # Create all database tables
    db.create_all()
    
    # Initialize career data if none exists
    if CareerPath.query.count() == 0:
        career_data.initialize_career_data(db)
    
    # Create admin user if none exists
    if AdminUser.query.count() == 0:
        admin = AdminUser(
            username="admin",
            email="admin@careerguide.com",
            password_hash=generate_password_hash("admin123")
        )
        db.session.add(admin)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    # Check if it's a admin user
    if str(user_id).startswith('admin_'):
        user_id = str(user_id).replace('admin_', '')
        return db.session.get(AdminUser, int(user_id))
    # Regular user
    return db.session.get(User, int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/jupyter-guide')
def jupyter_guide():
    return render_template('jupyter_guide.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if admin login
        admin = AdminUser.query.filter_by(email=email).first()
        if admin and check_password_hash(admin.password_hash, password):
            admin.get_id = lambda: f"admin_{admin.id}"
            login_user(admin)
            flash('Admin login successful', 'success')
            return redirect(url_for('admin_dashboard'))
        
        # Regular user login
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        grade = request.form.get('grade')
        
        # Validate required fields
        if not username or not email or not password or not grade:
            flash('All fields are required', 'danger')
            return render_template('register.html')
            
        # Basic email validation
        if '@' not in email or '.' not in email:
            flash('Please enter a valid email address', 'danger')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return render_template('register.html')
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered', 'danger')
            return render_template('register.html')
            
        # Check username is available
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash('Username already taken', 'danger')
            return render_template('register.html')
        
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            grade=grade
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Check if admin user
    if hasattr(current_user, 'is_admin') and current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    
    # Get user's assessment results if available
    assessment_result = AssessmentResult.query.filter_by(user_id=current_user.id).order_by(AssessmentResult.id.desc()).first()
    
    # Get recommended careers if assessment completed
    recommended_careers = []
    if assessment_result:
        recommended_careers = get_career_recommendations(assessment_result)
    
    # Get saved careers
    saved_careers = [saved.career for saved in SavedCareer.query.filter_by(user_id=current_user.id).all()]
    
    return render_template(
        'dashboard.html', 
        assessment_result=assessment_result,
        recommended_careers=recommended_careers,
        saved_careers=saved_careers
    )

@app.route('/assessment', methods=['GET', 'POST'])
@login_required
def assessment():
    if request.method == 'GET':
        questions = get_assessment_questions()
        return render_template('assessment.html', questions=questions)
    else:
        # Process assessment form submission
        assessment_data = request.form.to_dict()
        
        # Process the assessment data
        results = process_assessment_results(assessment_data)
        
        # Save the assessment results
        assessment_result = AssessmentResult(
            user_id=current_user.id,
            analytical_score=results['analytical'],
            creative_score=results['creative'],
            practical_score=results['practical'],
            social_score=results['social'],
            conventional_score=results['conventional'],
            enterprising_score=results['enterprising'],
            raw_data=json.dumps(assessment_data)
        )
        
        db.session.add(assessment_result)
        db.session.commit()
        
        return redirect(url_for('results', result_id=assessment_result.id))

@app.route('/results/<int:result_id>')
@login_required
def results(result_id):
    result = AssessmentResult.query.get_or_404(result_id)
    
    # Check if this result belongs to the current user
    if result.user_id != current_user.id:
        flash('You do not have permission to view that result', 'danger')
        return redirect(url_for('dashboard'))
    
    # Get career recommendations based on assessment
    recommended_careers = get_career_recommendations(result)
    
    return render_template('results.html', result=result, recommended_careers=recommended_careers)

@app.route('/careers')
def careers():
    # Get all career paths
    careers = CareerPath.query.all()
    
    # Get filter parameters
    category = request.args.get('category')
    
    # Apply filters if provided
    if category:
        careers = CareerPath.query.filter_by(category=category).all()
    
    # Get all unique categories for the filter dropdown
    categories = db.session.query(CareerPath.category).distinct().all()
    categories = [c[0] for c in categories]
    
    return render_template('careers.html', careers=careers, categories=categories)

@app.route('/career/<int:career_id>')
def career_details(career_id):
    career = CareerPath.query.get_or_404(career_id)
    
    # Check if the career is saved by current user
    is_saved = False
    if current_user.is_authenticated:
        saved = SavedCareer.query.filter_by(user_id=current_user.id, career_id=career_id).first()
        is_saved = saved is not None
    
    # Get aptitude scores from latest assessment if available
    user_aptitudes = None
    if current_user.is_authenticated and not current_user.is_admin:
        assessment = AssessmentResult.query.filter_by(user_id=current_user.id).order_by(AssessmentResult.id.desc()).first()
        if assessment:
            user_aptitudes = {
                'analytical': assessment.analytical_score,
                'creative': assessment.creative_score,
                'practical': assessment.practical_score,
                'social': assessment.social_score,
                'conventional': assessment.conventional_score,
                'enterprising': assessment.enterprising_score
            }
    
    return render_template('career_details.html', career=career, is_saved=is_saved, user_aptitudes=user_aptitudes)

@app.route('/save_career/<int:career_id>', methods=['POST'])
@login_required
def save_career(career_id):
    # Check if career exists
    career = CareerPath.query.get_or_404(career_id)
    
    # Check if already saved
    existing = SavedCareer.query.filter_by(user_id=current_user.id, career_id=career_id).first()
    
    if not existing:
        saved_career = SavedCareer(user_id=current_user.id, career_id=career_id)
        db.session.add(saved_career)
        db.session.commit()
        flash(f'Career "{career.title}" saved successfully', 'success')
    else:
        flash('Career already saved', 'info')
    
    return redirect(url_for('career_details', career_id=career_id))

@app.route('/remove_saved_career/<int:career_id>', methods=['POST'])
@login_required
def remove_saved_career(career_id):
    saved = SavedCareer.query.filter_by(user_id=current_user.id, career_id=career_id).first()
    
    if saved:
        db.session.delete(saved)
        db.session.commit()
        flash('Career removed from saved list', 'success')
    
    return redirect(url_for('dashboard'))

@app.route('/chatbot')
@login_required
def chatbot():
    return render_template('chatbot.html')

@app.route('/ask_bot', methods=['POST'])
@login_required
def ask_bot():
    data = request.get_json()
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    try:
        response = get_bot_response(question)
        return jsonify({'response': response})
    except Exception as e:
        app.logger.error(f"Bot error: {str(e)}")
        return jsonify({'error': 'Failed to get response from career bot. Please try again.'}), 500

@app.route('/profile')
@login_required
def profile():
    # Get assessment history
    assessment_history = AssessmentResult.query.filter_by(user_id=current_user.id).order_by(AssessmentResult.created_at.desc()).all()
    
    return render_template('profile.html', user=current_user, assessment_history=assessment_history)

# Admin routes
@app.route('/admin')
@login_required
def admin_dashboard():
    # Check if the user is an admin
    if not hasattr(current_user, 'is_admin') or not current_user.is_admin:
        flash('You do not have permission to access the admin dashboard', 'danger')
        return redirect(url_for('dashboard'))
    
    # Get stats for admin dashboard
    total_users = User.query.count()
    total_assessments = AssessmentResult.query.count()
    
    # Recent users
    recent_users = User.query.order_by(User.registered_at.desc()).limit(10).all()
    
    # Recent assessments
    recent_assessments = db.session.query(
        AssessmentResult, User
    ).join(
        User, AssessmentResult.user_id == User.id
    ).order_by(
        AssessmentResult.created_at.desc()
    ).limit(10).all()
    
    # Get assessment count by grade
    grade_stats = db.session.query(
        User.grade, db.func.count(AssessmentResult.id)
    ).join(
        AssessmentResult, User.id == AssessmentResult.user_id
    ).group_by(
        User.grade
    ).all()
    
    grade_stats_dict = {grade: count for grade, count in grade_stats}
    
    return render_template(
        'admin.html', 
        total_users=total_users,
        total_assessments=total_assessments,
        recent_users=recent_users,
        recent_assessments=recent_assessments,
        grade_stats=grade_stats_dict
    )

@app.route('/admin/users')
@login_required
def admin_users():
    # Check if the user is an admin
    if not hasattr(current_user, 'is_admin') or not current_user.is_admin:
        flash('You do not have permission to access the admin dashboard', 'danger')
        return redirect(url_for('dashboard'))
    
    # Get all users
    users = User.query.all()
    
    return render_template('admin_users.html', users=users)

@app.route('/admin/assessments')
@login_required
def admin_assessments():
    # Check if the user is an admin
    if not hasattr(current_user, 'is_admin') or not current_user.is_admin:
        flash('You do not have permission to access the admin dashboard', 'danger')
        return redirect(url_for('dashboard'))
    
    # Get all assessments with user info
    assessments = db.session.query(
        AssessmentResult, User
    ).join(
        User, AssessmentResult.user_id == User.id
    ).order_by(
        AssessmentResult.created_at.desc()
    ).all()
    
    return render_template('admin_assessments.html', assessments=assessments)

@app.route('/admin/view_assessment/<int:result_id>')
@login_required
def admin_view_assessment(result_id):
    # Check if the user is an admin
    if not hasattr(current_user, 'is_admin') or not current_user.is_admin:
        flash('You do not have permission to access the admin dashboard', 'danger')
        return redirect(url_for('dashboard'))
    
    # Get the assessment result
    result = AssessmentResult.query.get_or_404(result_id)
    user = User.query.get_or_404(result.user_id)
    
    # Get career recommendations based on assessment
    recommended_careers = get_career_recommendations(result)
    
    return render_template('admin_view_assessment.html', result=result, user=user, recommended_careers=recommended_careers)


if __name__ == "__main__":
    app.run(debug=True, port=8501)

    

