# CareerGuide Platform

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

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/careerguide.git
   cd careerguide
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database:
   - Create a new database for the application
   - Set the `DATABASE_URL` environment variable to your database connection string

4. Initialize the database:
   ```
   python initialize_db.py
   ```

5. Run the application:
   ```
   python -m flask run --host=0.0.0.0
   ```

## Running in Jupyter Lab

CareerGuide includes a Jupyter Lab integration for advanced data analysis and visualization:

1. Start Jupyter Lab:
   ```
   jupyter lab
   ```

2. Open the tutorial notebook:
   ```
   jupyter/CareerGuide_Tutorial.ipynb
   ```

3. Follow the step-by-step guide to deploy and use the application within Jupyter.

## Project Structure

- `app.py`: Main Flask application
- `models.py`: Database models
- `assessment.py`: Assessment logic and processing
- `recommendation.py`: Career recommendation algorithms
- `career_data.py`: Career database initialization
- `careerbot.py`: AI career assistant
- `static/`: CSS, JavaScript, and image assets
- `templates/`: HTML templates
- `jupyter/`: Jupyter notebooks for data analysis

## Development

### Setup for Development

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install development dependencies:
   ```
   pip install -r requirements-dev.txt
   ```

3. Set up the development database:
   ```
   export DATABASE_URL=postgresql://user:password@localhost/careerguide_dev
   ```

### Running Tests

```
pytest
```

## Deployment

For production deployment, use Gunicorn:

```
gunicorn --bind 0.0.0.0:5000 main:app
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.