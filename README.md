# CareerGuide
A comprehensive career guidance platform for 10th-12th grade students with assessment tools, personalized recommendations, and an AI career assistant.

## Features

- 🧠 **Aptitude Assessment**: 30-question assessment covering 6 aptitude categories
- 🔍 **Career Recommendations**: AI-powered matching of student aptitudes to career paths
- 🤖 **CareerBot**: Intelligent chatbot that answers career-related questions
- 📊 **Visualization**: Interactive charts and graphs for aptitude and career data
- 📱 **User Dashboard**: Track assessment history and save favorite careers
- 👩‍🏫 **Admin Panel**: Monitor student progress and view assessment results

## System Requirements

- Python 3.8 or higher
- PostgreSQL database
- Jupyter Lab (for data analysis features)

  ##Set up the PostgreSQL database:
   - Create a new database for the application
   - Set the `DATABASE_URL` environment variable to your database connection string

  ## Project Structure

- `app.py`: Main Flask application
- `models.py`: Database models
- `assessment.py`: Assessment logic and processing
- `recommendation.py`: Career recommendation algorithms
- `career_data.py`: Career database initialization
- `careerbot.py`: AI career assistant
- `static/`: CSS, JavaScript, and image assets
- `templates/`: HTML templates
