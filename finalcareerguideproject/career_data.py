"""
Module for initializing and managing career data in the database
"""

def initialize_career_data(db):
    """
    Initialize the database with career data if it doesn't exist
    
    Args:
        db: SQLAlchemy database instance
    """
    from models import CareerPath
    
    # Define career paths with their attributes
    careers = [
        {
            "title": "Software Engineer / Developer",
            "description": "Software engineers design, develop, and maintain computer programs, applications, and systems. They analyze user needs, write code, test software, and work on improvements. This field offers diverse opportunities from web and mobile app development to artificial intelligence and database management.",
            "category": "Technology",
            "education_requirements": "Bachelor's degree in Computer Science, Software Engineering, or related field. Some roles may accept self-taught developers with strong portfolios.",
            "skills_required": "Programming languages (Python, Java, JavaScript, etc.), problem-solving, logical thinking, teamwork, attention to detail, continuous learning",
            "analytical_relevance": 4.5,
            "creative_relevance": 3.5,
            "practical_relevance": 4.0,
            "social_relevance": 2.5,
            "conventional_relevance": 3.0,
            "enterprising_relevance": 2.5
        },
        {
            "title": "Data Scientist",
            "description": "Data scientists extract, analyze, and interpret large amounts of data to help organizations make better decisions. They use statistical analysis, machine learning, and data visualization to identify patterns and trends in data.",
            "category": "Technology",
            "education_requirements": "Bachelor's or Master's degree in Data Science, Statistics, Computer Science, or related field.",
            "skills_required": "Statistical analysis, programming (Python, R), machine learning, data visualization, communication, problem-solving",
            "analytical_relevance": 5.0,
            "creative_relevance": 3.0,
            "practical_relevance": 3.5,
            "social_relevance": 2.0,
            "conventional_relevance": 3.5,
            "enterprising_relevance": 2.0
        },
        {
            "title": "Doctor / Physician",
            "description": "Doctors diagnose and treat illnesses, injuries, and other health conditions. They examine patients, order tests, prescribe medications, and provide healthcare advice. Specializations include family medicine, surgery, pediatrics, cardiology, and many others.",
            "category": "Healthcare",
            "education_requirements": "Medical degree (MBBS/MD) after 12th science, followed by residency and specialization if desired.",
            "skills_required": "Scientific knowledge, problem-solving, communication, empathy, attention to detail, decision-making under pressure",
            "analytical_relevance": 4.5,
            "creative_relevance": 2.5,
            "practical_relevance": 4.0,
            "social_relevance": 4.5,
            "conventional_relevance": 3.5,
            "enterprising_relevance": 3.0
        },
        {
            "title": "Registered Nurse",
            "description": "Nurses provide care for patients in hospitals, clinics, and other healthcare settings. They administer medications, monitor patients' conditions, assist with medical procedures, and educate patients about health management.",
            "category": "Healthcare",
            "education_requirements": "Nursing degree or diploma from recognized nursing council. Options include GNM, B.Sc Nursing, etc.",
            "skills_required": "Patient care, medical knowledge, communication, empathy, critical thinking, teamwork",
            "analytical_relevance": 3.5,
            "creative_relevance": 2.0,
            "practical_relevance": 4.5,
            "social_relevance": 5.0,
            "conventional_relevance": 3.5,
            "enterprising_relevance": 2.0
        },
        {
            "title": "Chartered Accountant",
            "description": "Chartered Accountants manage financial records, prepare financial statements, ensure regulatory compliance, and provide financial advice to organizations and individuals. They may specialize in auditing, taxation, financial planning, or forensic accounting.",
            "category": "Finance",
            "education_requirements": "Commerce in 12th, followed by CA foundation, intermediate, and final exams from ICAI.",
            "skills_required": "Mathematical aptitude, analytical thinking, attention to detail, integrity, communication, knowledge of financial regulations",
            "analytical_relevance": 4.5,
            "creative_relevance": 2.0,
            "practical_relevance": 3.0,
            "social_relevance": 2.5,
            "conventional_relevance": 5.0,
            "enterprising_relevance": 3.5
        },
        {
            "title": "Mechanical Engineer",
            "description": "Mechanical engineers design, develop, build, and test mechanical devices and systems. They work on various machines, tools, engines, and manufacturing processes across industries like automotive, aerospace, energy, and manufacturing.",
            "category": "Engineering",
            "education_requirements": "Bachelor's degree in Mechanical Engineering from an accredited institution.",
            "skills_required": "Mathematics, physics, CAD software, problem-solving, technical drawing, creativity",
            "analytical_relevance": 4.0,
            "creative_relevance": 3.5,
            "practical_relevance": 4.5,
            "social_relevance": 2.0,
            "conventional_relevance": 3.5,
            "enterprising_relevance": 2.5
        },
        {
            "title": "Architect",
            "description": "Architects design buildings and structures, considering aesthetics, functionality, safety, and sustainability. They create plans and specifications, oversee construction, and ensure compliance with building codes and regulations.",
            "category": "Design & Construction",
            "education_requirements": "Bachelor's of Architecture (B.Arch) followed by registration with the Council of Architecture.",
            "skills_required": "Design skills, spatial awareness, technical drawing, CAD software, creativity, communication",
            "analytical_relevance": 3.5,
            "creative_relevance": 5.0,
            "practical_relevance": 4.0,
            "social_relevance": 3.0,
            "conventional_relevance": 3.0,
            "enterprising_relevance": 3.0
        },
        {
            "title": "Graphic Designer",
            "description": "Graphic designers create visual content for various media including websites, advertisements, publications, packaging, and branding materials. They communicate ideas through images, typography, and layout design.",
            "category": "Arts & Design",
            "education_requirements": "Bachelor's degree in Graphic Design, Visual Communication, or related field. Some positions may accept a strong portfolio without formal education.",
            "skills_required": "Creativity, design software (Adobe Creative Suite), visual communication, attention to detail, time management",
            "analytical_relevance": 2.5,
            "creative_relevance": 5.0,
            "practical_relevance": 4.0,
            "social_relevance": 2.5,
            "conventional_relevance": 3.0,
            "enterprising_relevance": 2.5
        },
        {
            "title": "Digital Marketing Specialist",
            "description": "Digital marketers promote products and services through digital channels like social media, email, search engines, and websites. They develop marketing strategies, create content, analyze campaign performance, and optimize marketing efforts.",
            "category": "Marketing & Communications",
            "education_requirements": "Bachelor's degree in Marketing, Communications, or related field. Specialized courses and certifications in digital marketing are valuable.",
            "skills_required": "Social media management, SEO, content creation, data analysis, creativity, communication",
            "analytical_relevance": 3.5,
            "creative_relevance": 4.0,
            "practical_relevance": 3.0,
            "social_relevance": 3.5,
            "conventional_relevance": 3.0,
            "enterprising_relevance": 4.0
        },
        {
            "title": "Teacher / Educator",
            "description": "Teachers educate students in various subjects, develop lesson plans, assess learning progress, and support student development. They work in schools, colleges, universities, and other educational institutions.",
            "category": "Education",
            "education_requirements": "Bachelor's degree in Education (B.Ed) after graduation in the subject of specialization. For primary teaching, Diploma in Elementary Education (D.El.Ed) after 12th.",
            "skills_required": "Subject knowledge, communication, patience, creativity, organization, adaptability",
            "analytical_relevance": 3.5,
            "creative_relevance": 3.5,
            "practical_relevance": 3.0,
            "social_relevance": 5.0,
            "conventional_relevance": 3.5,
            "enterprising_relevance": 3.0
        },
        {
            "title": "Civil Engineer",
            "description": "Civil engineers design, construct, and maintain infrastructure projects like buildings, roads, bridges, dams, and water systems. They ensure projects are safe, efficient, and environmentally sound.",
            "category": "Engineering",
            "education_requirements": "Bachelor's degree in Civil Engineering from an accredited institution.",
            "skills_required": "Mathematics, physics, CAD software, problem-solving, project management, attention to detail",
            "analytical_relevance": 4.0,
            "creative_relevance": 3.0,
            "practical_relevance": 4.5,
            "social_relevance": 2.5,
            "conventional_relevance": 3.5,
            "enterprising_relevance": 3.0
        },
        {
            "title": "Lawyer / Advocate",
            "description": "Lawyers provide legal advice and representation to individuals, businesses, and organizations. They research legal issues, prepare legal documents, and represent clients in court and legal proceedings.",
            "category": "Legal",
            "education_requirements": "Bachelor's degree in Law (LLB) after 12th or graduation, followed by enrollment with the Bar Council.",
            "skills_required": "Legal knowledge, research, critical thinking, communication, persuasion, attention to detail",
            "analytical_relevance": 4.5,
            "creative_relevance": 3.0,
            "practical_relevance": 2.5,
            "social_relevance": 3.5,
            "conventional_relevance": 4.0,
            "enterprising_relevance": 4.0
        },
        {
            "title": "Psychologist",
            "description": "Psychologists study human behavior and mental processes to help people overcome psychological challenges and improve their well-being. They assess, diagnose, and treat mental health issues and conduct research.",
            "category": "Healthcare",
            "education_requirements": "Bachelor's, Master's, and often Doctoral degree in Psychology. Clinical psychologists need a Ph.D. or Psy.D.",
            "skills_required": "Empathy, active listening, analytical thinking, communication, ethics, research skills",
            "analytical_relevance": 4.0,
            "creative_relevance": 3.0,
            "practical_relevance": 2.5,
            "social_relevance": 5.0,
            "conventional_relevance": 3.0,
            "enterprising_relevance": 2.5
        },
        {
            "title": "Financial Analyst",
            "description": "Financial analysts evaluate investment opportunities, analyze financial data, and provide recommendations to individuals and organizations. They monitor market trends, create financial models, and help with investment decisions.",
            "category": "Finance",
            "education_requirements": "Bachelor's degree in Finance, Economics, or related field. Professional certifications like CFA are valuable.",
            "skills_required": "Financial modeling, data analysis, attention to detail, research, communication, critical thinking",
            "analytical_relevance": 4.5,
            "creative_relevance": 2.0,
            "practical_relevance": 3.0,
            "social_relevance": 2.5,
            "conventional_relevance": 4.5,
            "enterprising_relevance": 3.0
        },
        {
            "title": "Entrepreneur",
            "description": "Entrepreneurs start and run their own businesses. They identify opportunities, develop business plans, secure funding, manage operations, and drive growth. They must be versatile and willing to take calculated risks.",
            "category": "Business",
            "education_requirements": "No specific requirements, though business education or experience can be helpful. Many entrepreneurs learn through experience.",
            "skills_required": "Leadership, creativity, risk management, financial awareness, communication, problem-solving, perseverance",
            "analytical_relevance": 3.5,
            "creative_relevance": 4.0,
            "practical_relevance": 3.5,
            "social_relevance": 3.5,
            "conventional_relevance": 3.0,
            "enterprising_relevance": 5.0
        }
    ]
    
    # Add careers to the database
    for career_data in careers:
        existing_career = CareerPath.query.filter_by(title=career_data['title']).first()
        if not existing_career:
            career = CareerPath(**career_data)
            db.session.add(career)
    
    db.session.commit()
