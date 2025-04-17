from datetime import datetime
from flask_login import UserMixin
#from app import db
from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    grade = db.Column(db.String(10))  # 10th, 11th, 12th
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    assessment_results = db.relationship('AssessmentResult', backref='user', lazy=True)
    saved_careers = db.relationship('SavedCareer', backref='user', lazy=True)
    
    @property
    def is_admin(self):
        return False

class AdminUser(UserMixin, db.Model):
    __tablename__ = 'admin_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def is_admin(self):
        return True

class AssessmentResult(db.Model):
    __tablename__ = 'assessment_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    analytical_score = db.Column(db.Float)
    creative_score = db.Column(db.Float)
    practical_score = db.Column(db.Float)
    social_score = db.Column(db.Float)
    conventional_score = db.Column(db.Float)
    enterprising_score = db.Column(db.Float)
    raw_data = db.Column(db.Text)  # JSON string of the raw assessment responses
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def get_scores_dict(self):
        return {
            'analytical': self.analytical_score,
            'creative': self.creative_score,
            'practical': self.practical_score,
            'social': self.social_score,
            'conventional': self.conventional_score,
            'enterprising': self.enterprising_score
        }

class CareerPath(db.Model):
    __tablename__ = 'career_paths'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    education_requirements = db.Column(db.Text)
    skills_required = db.Column(db.Text)
    
    # Aptitude relevance scores (1-5 scale)
    analytical_relevance = db.Column(db.Float)
    creative_relevance = db.Column(db.Float)
    practical_relevance = db.Column(db.Float)
    social_relevance = db.Column(db.Float)
    conventional_relevance = db.Column(db.Float)
    enterprising_relevance = db.Column(db.Float)
    
    # Relationships
    saved_by = db.relationship('SavedCareer', backref='career', lazy=True)
    
    def get_relevance_scores(self):
        return {
            'analytical': self.analytical_relevance,
            'creative': self.creative_relevance,
            'practical': self.practical_relevance,
            'social': self.social_relevance,
            'conventional': self.conventional_relevance,
            'enterprising': self.enterprising_relevance
        }

class SavedCareer(db.Model):
    __tablename__ = 'saved_careers'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    career_id = db.Column(db.Integer, db.ForeignKey('career_paths.id'), nullable=False)
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Add a unique constraint to prevent duplicate saved careers
    __table_args__ = (db.UniqueConstraint('user_id', 'career_id', name='unique_user_career'),)
