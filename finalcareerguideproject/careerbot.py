"""
Module for AI-powered career advisor bot
"""

import random
import json
import re

def get_bot_response(question):
    """
    Get a response from the career bot based on the user's question
    
    Args:
        question (str): The user's question or message
        
    Returns:
        str: The bot's response
    """
    # Normalize the question: lowercase and remove punctuation
    normalized_question = question.lower()
    normalized_question = re.sub(r'[^\w\s]', '', normalized_question)
    
    # Check for keywords in the question to determine the type of query
    knowledge_base = get_knowledge_base()
    
    # Check specific career questions first
    for career in knowledge_base['careers']:
        career_name_lower = career['name'].lower()
        if career_name_lower in normalized_question:
            return get_career_response(career, normalized_question)
        
        # Check for alternative names or specializations
        for alt_name in career.get('alternative_names', []):
            if alt_name.lower() in normalized_question:
                return get_career_response(career, normalized_question)
    
    # Check for general question categories
    for category in knowledge_base['categories']:
        for keyword in category['keywords']:
            if keyword in normalized_question:
                return random.choice(category['responses'])
    
    # If no specific match is found, attempt to provide a helpful response
    for faq in knowledge_base.get('faqs', []):
        for keyword in faq['keywords']:
            if keyword in normalized_question:
                return faq['answer']
    
    # Last resort - fallback response
    return random.choice(knowledge_base['fallback_responses'])

def get_career_response(career, question):
    """
    Generate a response about a specific career
    
    Args:
        career (dict): The career data dictionary
        question (str): The normalized user question
        
    Returns:
        str: A response about the requested career aspect
    """
    # Check what specific aspect of the career the user is asking about
    if any(word in question for word in ['salary', 'pay', 'earn', 'income', 'money']):
        return career['salary_info']
    elif any(word in question for word in ['education', 'degree', 'study', 'school', 'college', 'university']):
        return career['education_info']
    elif any(word in question for word in ['skills', 'abilities', 'requirements', 'need', 'qualification']):
        return career['skills_info']
    elif any(word in question for word in ['outlook', 'future', 'growth', 'demand', 'opportunity']):
        return career['outlook_info']
    else:
        # General information about the career
        return career['general_info']

def get_knowledge_base():
    """
    Get the knowledge base for the CareerBot
    
    Returns:
        dict: The complete knowledge base including career information and FAQs
    """
    return {
        'careers': [
            {
                'name': 'Data Scientist',
                'alternative_names': ['data science', 'data analyst', 'machine learning engineer', 'AI specialist', 'ML engineer'],
                'general_info': 'Data Scientists extract insights from data using statistics, machine learning, and programming. They identify patterns, trends, and correlations in large datasets to help businesses make data-driven decisions. This field combines computer science, statistics, and domain expertise to solve complex problems.',
                'salary_info': 'Data Scientists typically earn between $95,000 and $165,000 annually, varying by experience, location, industry, and specialization. Those with expertise in advanced AI, deep learning, or specialized domains like healthcare or finance often command higher salaries.',
                'education_info': 'Most Data Science positions require at least a bachelor\'s degree in Computer Science, Statistics, Mathematics, or a related field. Many roles prefer or require master\'s or Ph.D. degrees, especially for research-oriented positions. However, bootcamps and self-study with strong projects can also be pathways into the field.',
                'skills_info': 'Essential skills for Data Scientists include programming (Python, R), statistics, machine learning, data visualization, SQL, and communication skills. Proficiency with tools like pandas, scikit-learn, TensorFlow, and data visualization libraries is highly valued. Domain knowledge in the industry you work in is also important.',
                'outlook_info': 'The job outlook for Data Scientists is exceptional, with projected growth of 22-28% through 2030, much faster than average. As organizations increasingly rely on data-driven decision making, demand for skilled data scientists continues to outpace supply in many regions.'
            },
            {
                'name': 'Software Engineer',
                'alternative_names': ['programmer', 'developer', 'coder', 'software development', 'web developer'],
                'general_info': 'Software Engineers design, develop, and maintain software systems and applications. They work in various industries including technology, finance, healthcare, and more. This career involves problem-solving, coding, and collaboration with cross-functional teams.',
                'salary_info': 'Software Engineers typically earn between $70,000 and $150,000 annually, depending on experience, location, and specialization. Senior roles or those in high-demand areas like AI can earn significantly more.',
                'education_info': 'Most Software Engineer positions require a bachelor\'s degree in Computer Science, Software Engineering, or a related field. However, many employers also value practical skills and experience, so bootcamps or self-taught programmers with strong portfolios can also find opportunities.',
                'skills_info': 'Key skills for Software Engineers include programming languages (like Python, Java, JavaScript), algorithms, data structures, problem-solving, version control systems, and teamwork. Specialized roles may require knowledge of specific frameworks, databases, or cloud platforms.',
                'outlook_info': 'The job outlook for Software Engineers is excellent, with growth projected at 22% through 2030, much faster than average. The increasing digitization across all industries continues to drive demand for software development talent.'
            },
            {
                'name': 'Physician',
                'alternative_names': ['doctor', 'medical doctor', 'md', 'medicine', 'medical career', 'medical profession'],
                'general_info': 'Physicians diagnose and treat illnesses, injuries, and other health conditions. They work in various settings like hospitals, clinics, or private practices, and may specialize in specific areas of medicine such as cardiology, pediatrics, or surgery.',
                'salary_info': 'Physicians typically earn between $200,000 and $400,000 annually, though this varies widely by specialization, location, and practice type. Specialists like neurosurgeons or cardiologists often earn at the higher end of the scale.',
                'education_info': 'Becoming a physician requires a bachelor\'s degree, followed by 4 years of medical school, and then 3-7 years of residency training depending on specialization. The path also includes passing licensing exams and, for specialists, board certification.',
                'skills_info': 'Physicians need strong diagnostic skills, medical knowledge, communication abilities, empathy, attention to detail, and critical thinking. They must stay current with medical research and have good decision-making abilities under pressure.',
                'outlook_info': 'The job outlook for physicians is strong, with projected growth of 3-4% through 2030. An aging population and increased healthcare demands continue to drive need, though changes in healthcare delivery models may impact certain specialties.'
            },
            {
                'name': 'Teacher',
                'alternative_names': ['educator', 'instructor', 'professor', 'teaching', 'education career', 'teaching profession'],
                'general_info': 'Teachers educate students in various subjects and grade levels, developing lesson plans, delivering instruction, and evaluating student progress. They play a crucial role in developing students\' knowledge, skills, and character.',
                'salary_info': 'Teachers typically earn between $45,000 and $80,000 annually, depending on location, education level, experience, and whether they work in public or private schools. Teachers with advanced degrees or in administrative roles can earn more.',
                'education_info': 'Most teaching positions require at least a bachelor\'s degree, and public school teachers need state certification or licensure. Many teachers also pursue master\'s degrees in education or their subject area for career advancement and higher pay.',
                'skills_info': 'Essential skills for teachers include instructional techniques, classroom management, communication, patience, adaptability, and organization. Subject expertise, assessment design, and technology integration are also important.',
                'outlook_info': 'The job outlook for teachers varies by specialty and location, with overall growth around 7-8% through 2030. Subjects like mathematics, science, and special education often have higher demand and better opportunities.'
            },
            {
                'name': 'Graphic Designer',
                'alternative_names': ['designer', 'graphic design', 'artist', 'visual designer', 'creative designer'], 
                'general_info': 'Graphic Designers create visual concepts for various media including websites, advertisements, publications, and product packaging. They help communicate ideas through images, typography, and layout design.',
                'salary_info': 'Graphic Designers typically earn between $45,000 and $85,000 annually. Salaries vary based on experience, industry, location, and whether they work in-house, at agencies, or freelance. Senior designers or creative directors can earn significantly more.',
                'education_info': 'Many Graphic Designers have a bachelor\'s degree in Graphic Design or a related field, though a strong portfolio showcasing technical skills and creativity is often more important than formal education. Many successful designers are self-taught or have completed focused certificate programs.',
                'skills_info': 'Key skills include proficiency with design software (Adobe Creative Suite), typography, color theory, layout design, visual communication, attention to detail, and keeping up with design trends. Client communication and time management are also important, especially for freelancers.',
                'outlook_info': 'The job outlook for Graphic Designers is stable but competitive, with growth around 3% through 2030. Designers with web, UX/UI, and multimedia skills have better prospects as digital media continues to expand.'
            },
            {
                'name': 'Financial Analyst',
                'alternative_names': ['finance', 'financial career', 'investment analyst', 'economics', 'banking'], 
                'general_info': 'Financial Analysts evaluate financial data and market trends to provide investment recommendations and strategies for individuals or organizations. They assess the performance of stocks, bonds, and other investments to help guide business and investment decisions.',
                'salary_info': 'Financial Analysts typically earn between $60,000 and $120,000 annually. Those working in investment banking or with advanced certifications like CFA can earn significantly more, especially in financial centers like New York or London.',
                'education_info': 'Most Financial Analyst positions require at least a bachelor\'s degree in Finance, Economics, Accounting, or related fields. Many analysts pursue MBAs or professional certifications like the Chartered Financial Analyst (CFA) designation for career advancement.',
                'skills_info': 'Key skills include financial modeling, data analysis, Excel proficiency, accounting knowledge, attention to detail, and research abilities. Understanding of market dynamics, industry trends, and regulatory environments is also important.',
                'outlook_info': 'The job outlook for Financial Analysts is positive, with projected growth of 6% through 2030. Increasing complexity in investments and global finance, along with growing data availability, continue to drive demand for skilled analysts.'
            }
        ],
        'faqs': [
            {
                'keywords': ['what is data science', 'explain data science', 'define data science'],
                'answer': 'Data Science is an interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data. It combines expertise in statistics, mathematics, programming, and domain knowledge to analyze data and solve complex problems. Data scientists use tools like Python, R, SQL, and various machine learning algorithms to identify patterns, make predictions, and inform decision-making.'
            },
            {
                'keywords': ['machine learning', 'ml', 'ai', 'artificial intelligence', 'algorithms'],
                'answer': 'Machine Learning (ML) is a subset of Artificial Intelligence that focuses on developing systems that can learn from and make decisions based on data. Instead of being explicitly programmed to perform a task, ML algorithms use data to build models that can make predictions or decisions without being specifically programmed for that task. Common ML approaches include supervised learning (using labeled data), unsupervised learning (finding patterns in unlabeled data), and reinforcement learning (learning through trial and error).'
            },
            {
                'keywords': ['programming languages', 'coding languages', 'best language', 'learn to code', 'which language'],
                'answer': 'The best programming language to learn depends on your goals and interests. For web development, HTML/CSS/JavaScript are essential. For data science and ML, Python is widely used due to its readability and extensive libraries. Java and C# are popular for enterprise applications. Swift is used for iOS development, while Kotlin is preferred for Android. For beginners, Python is often recommended due to its simple syntax and versatility across many fields.'
            },
            {
                'keywords': ['high school preparation', 'prepare for career', 'high school classes', 'what courses', 'extracurricular'],
                'answer': 'To prepare for a career while in high school: 1) Take challenging courses in subjects relevant to your interests; 2) Participate in extracurricular activities related to potential career fields; 3) Seek volunteer or internship opportunities; 4) Develop soft skills like communication and teamwork; 5) Research colleges and programs aligned with your career goals; 6) Consider dual enrollment or AP/IB courses for college credit; 7) Network with professionals through job shadowing or informational interviews.'
            },
            {
                'keywords': ['which career test', 'assessment accuracy', 'test reliable', 'trust assessment', 'career quiz'],
                'answer': 'Career assessments like the one on CareerGuide are tools to help you explore options based on your interests, values, and aptitudes—not to provide definitive answers. They work best when used as one part of your exploration process, alongside research, informational interviews, job shadowing, and trying activities related to potential careers. Remember that your interests and goals may evolve over time, so view assessment results as helpful suggestions rather than fixed predictions.'
            }
        ],
        'categories': [
            {
                'name': 'career_exploration',
                'keywords': ['how do i choose', 'find right career', 'career path', 'right for me', 'career test', 'find passion', 'discover career', 'career options', 'choices', 'decide career'],
                'responses': [
                    'Choosing a career path involves understanding your interests, values, skills, and personality. Our assessment tool can help identify careers that align with your unique profile. Additionally, try job shadowing, internships, or volunteering to gain firsthand experience in fields that interest you.',
                    'Finding the right career is a journey of self-discovery. Start by reflecting on activities you enjoy and excel at. Research careers that utilize these strengths, talk to professionals in those fields, and consider taking our aptitude assessment to get personalized recommendations.',
                    'When exploring career options, consider both your passions and practicality. Look at careers that match your interests but also have good job prospects and align with your lifestyle goals. Our career assessment can provide guidance based on your unique attributes and preferences.',
                    'Career exploration is about finding the intersection of what you love, what you\'re good at, and what the world needs. Start by making a list of your skills and interests, then research careers that match. Our assessment can help narrow down options that suit your aptitude profile.',
                    'To discover suitable career paths, pay attention to subjects and activities that engage you deeply. Consider your values and work preferences (like working with people, data, or things). Our career assessment provides recommendations based on your unique combination of aptitudes.'
                ]
            },
            {
                'name': 'education_planning',
                'keywords': ['college', 'university', 'degree', 'major', 'study', 'education', 'school', 'course', 'class', 'training', 'learn', 'program', 'certificate'],
                'responses': [
                    'Educational planning should align with your career goals. Research the typical education requirements for careers you\'re interested in. Consider factors like program reputation, cost, location, and how well the curriculum matches industry needs. Remember that some careers have multiple educational pathways.',
                    'When choosing a major or degree program, look for opportunities to gain practical experience through internships, co-ops, or research projects. Many careers value relevant experience alongside formal education. Also consider whether graduate education might be necessary or beneficial in your chosen field.',
                    'Educational decisions should balance passion with practicality. While following your interests is important, also research job prospects and return on investment for different educational paths. Consider starting at community college to explore interests cost-effectively before committing to a specific major.',
                    'For many careers, skill-building can be as important as formal credentials. Look for educational programs that offer hands-on learning, industry partnerships, and opportunities to build a portfolio of work. Consider complementing traditional education with online courses or certifications in specialized skills.',
                    'When planning your education, research which institutions have strong programs in your areas of interest. Look at graduation rates, job placement statistics, and alumni networks. Consider talking to professionals in your target field about which educational paths they recommend based on current industry trends.'
                ]
            },
            {
                'name': 'skill_development',
                'keywords': ['skills', 'improve', 'learn skills', 'develop', 'abilities', 'get better', 'practice', 'master', 'competency', 'capability', 'proficiency', 'expertise'],
                'responses': [
                    'Skill development is a lifelong process. Identify both technical skills specific to your field and transferable skills valuable across careers (like communication, problem-solving, and teamwork). Create a development plan with regular practice, feedback opportunities, and measurable goals.',
                    'To develop career-relevant skills, combine formal learning with practical application. Online courses, workshops, and tutorials can teach fundamentals, but real mastery comes through projects, internships, volunteering, or part-time work that lets you apply and refine those skills.',
                    'When building skills, focus on both depth and breadth. Develop deep expertise in core skills for your field, while also acquiring complementary skills that make you versatile. For example, technical professionals benefit from communication skills, while creative roles benefit from basic business knowledge.',
                    'Skill development accelerates with deliberate practice and feedback. Set specific improvement goals, break complex skills into components, practice regularly, seek expert feedback, and reflect on your progress. Consider finding a mentor in your field who can guide your skill development journey.',
                    'In today\'s rapidly changing workplace, continuous skill development is essential. Stay current with industry trends and emerging technologies in your field. Professional associations, industry publications, and online learning platforms can help you identify which skills will be most valuable to develop.'
                ]
            },
            {
                'name': 'job_search',
                'keywords': ['find job', 'job search', 'application', 'resume', 'interview', 'cover letter', 'apply', 'hiring', 'employer', 'recruitment', 'job market', 'job board', 'linked', 'networking'],
                'responses': [
                    'Effective job searching combines multiple strategies. Create tailored resumes and cover letters for each position, highlighting relevant skills and achievements. Utilize job boards, company websites, and professional networking sites, but also focus on networking—many opportunities are never publicly advertised.',
                    'For successful job applications, research each company thoroughly and customize your materials to show how your skills address their specific needs. Prepare for interviews by practicing responses to common questions and developing thoughtful questions about the role and organization.',
                    'Networking is crucial in job searching. Connect with professionals in your target field through LinkedIn, professional associations, alumni networks, and industry events. Informational interviews can provide insights about companies and sometimes lead to job opportunities.',
                    'When preparing your resume, focus on achievements rather than just responsibilities. Use specific metrics and examples to demonstrate your impact. Keep the format clean and scannable, as most resumes receive initial screening for just 6-7 seconds.',
                    'Job searching requires persistence and resilience. Set regular goals for applications, networking, and skill development. Track your efforts, learn from each interview experience, and maintain a positive mindset. Consider working with career counselors or coaches for personalized guidance.'
                ]
            },
            {
                'name': 'work_life_balance',
                'keywords': ['balance', 'stress', 'burnout', 'workload', 'pressure', 'wellness', 'mental health', 'well-being', 'overwork', 'time management', 'boundaries', 'self-care'],
                'responses': [
                    'Work-life balance varies by career and workplace culture. Research typical hours, flexibility, and remote work options in careers you\'re considering. During interviews, look for cues about company culture and ask current employees about their experience with work-life balance.',
                    'Creating work-life balance requires clear boundaries and prioritization. Identify your non-negotiables for personal time, learn to delegate when possible, and practice saying no to low-priority commitments. Many successful professionals schedule personal activities with the same importance as work meetings.',
                    'Different careers offer varying levels of flexibility and demands. Some high-intensity careers may require periods of imbalance but offer other benefits like extended time off between projects. Consider what balance means for you personally when evaluating career options.',
                    'Managing stress in high-pressure careers requires intentional strategies. Regular exercise, mindfulness practices, hobbies, and social connections all help build resilience. Also consider whether your stress comes from the nature of the work itself or from workplace culture, which can vary widely within the same career.',
                    'Work-life integration, rather than strict separation, works better for some people and careers. This approach involves finding ways to blend professional and personal activities in a fulfilling way, rather than keeping them rigidly separate. Consider whether this approach might suit your career goals and lifestyle preferences.'
                ]
            }
        ],
        'fallback_responses': [
            "That's an interesting question about careers. Could you provide more details about what specifically you'd like to know?",
            "I'm not sure I have enough information to answer that career question effectively. Could you rephrase or provide more context about what you're looking for?",
            "I don't have specific information about that, but I'd be happy to help you explore related career topics. What aspects are you most interested in learning about?",
            "That's a great question about professional development. To give you the most helpful answer, could you tell me more about your specific situation or goals?",
            "I appreciate your career question. To provide the most relevant guidance, could you share a bit more about your background, interests, or what prompted this question?"
        ]
    }