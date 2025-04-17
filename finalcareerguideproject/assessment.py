"""
Module for career assessment functionality
"""

import json
import random
from collections import defaultdict

def get_assessment_questions():
    """
    Get the questions for the career assessment quiz
    
    Returns:
        list: A list of dictionaries containing questions and answer options
    """
    questions = [
        # Analytical aptitude questions
        {
            'id': 1,
            'text': 'I enjoy solving complex problems that require logical thinking.',
            'category': 'analytical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 2,
            'text': 'I like analyzing data to draw conclusions.',
            'category': 'analytical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 3,
            'text': 'I enjoy subjects like mathematics, physics, or computer science.',
            'category': 'analytical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 4,
            'text': 'I am good at spotting patterns and inconsistencies.',
            'category': 'analytical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 5,
            'text': 'I prefer tasks that have clear, logical solutions.',
            'category': 'analytical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        
        # Creative aptitude questions
        {
            'id': 6,
            'text': 'I enjoy coming up with new ideas and creative solutions.',
            'category': 'creative',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 7,
            'text': 'I am interested in artistic activities like drawing, music, or writing.',
            'category': 'creative',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 8,
            'text': 'I like thinking outside the box and exploring unconventional approaches.',
            'category': 'creative',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 9,
            'text': 'I enjoy activities that allow me to express myself.',
            'category': 'creative',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 10,
            'text': 'I am good at imagining how things could be different or improved.',
            'category': 'creative',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        
        # Practical aptitude questions
        {
            'id': 11,
            'text': 'I enjoy working with my hands and building things.',
            'category': 'practical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 12,
            'text': 'I like fixing things that are broken or not working properly.',
            'category': 'practical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 13,
            'text': 'I am good at understanding how mechanical or electronic devices work.',
            'category': 'practical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 14,
            'text': 'I prefer activities with tangible, physical results.',
            'category': 'practical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 15,
            'text': 'I like learning through hands-on experience rather than just reading or listening.',
            'category': 'practical',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        
        # Social aptitude questions
        {
            'id': 16,
            'text': 'I enjoy working with and helping other people.',
            'category': 'social',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 17,
            'text': 'I am good at understanding others\' perspectives and feelings.',
            'category': 'social',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 18,
            'text': 'I like activities that involve teamwork and collaboration.',
            'category': 'social',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 19,
            'text': 'I am comfortable speaking in front of groups or teaching others.',
            'category': 'social',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 20,
            'text': 'I am interested in human behavior and what motivates people.',
            'category': 'social',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        
        # Conventional aptitude questions
        {
            'id': 21,
            'text': 'I prefer tasks that have clear instructions and procedures.',
            'category': 'conventional',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 22,
            'text': 'I am good at organizing information and keeping accurate records.',
            'category': 'conventional',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 23,
            'text': 'I enjoy working with numbers and detailed information.',
            'category': 'conventional',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 24,
            'text': 'I like following schedules and routines.',
            'category': 'conventional',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 25,
            'text': 'I am detail-oriented and thorough in my work.',
            'category': 'conventional',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        
        # Enterprising aptitude questions
        {
            'id': 26,
            'text': 'I enjoy taking on leadership roles.',
            'category': 'enterprising',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 27,
            'text': 'I am good at persuading others and selling ideas.',
            'category': 'enterprising',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 28,
            'text': 'I like competitive activities and challenges.',
            'category': 'enterprising',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 29,
            'text': 'I am interested in business, entrepreneurship, or management.',
            'category': 'enterprising',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        },
        {
            'id': 30,
            'text': 'I enjoy making decisions and taking calculated risks.',
            'category': 'enterprising',
            'options': [
                {'value': '1', 'text': 'Strongly Disagree'},
                {'value': '2', 'text': 'Disagree'},
                {'value': '3', 'text': 'Neutral'},
                {'value': '4', 'text': 'Agree'},
                {'value': '5', 'text': 'Strongly Agree'}
            ]
        }
    ]
    
    return questions

def process_assessment_results(assessment_data):
    """
    Process the raw assessment responses into category scores
    
    Args:
        assessment_data (dict): Dictionary of form responses
        
    Returns:
        dict: Dictionary of category scores
    """
    # Define the categories and initialize scores
    categories = ['analytical', 'creative', 'practical', 'social', 'conventional', 'enterprising']
    category_scores = defaultdict(list)
    
    # Get the assessment questions to map responses to categories
    questions = get_assessment_questions()
    questions_by_id = {q['id']: q for q in questions}
    
    # Process each response
    for key, value in assessment_data.items():
        if key.startswith('q'):
            try:
                # Extract question ID from the form field name
                question_id = int(key[1:])
                # Get the question category
                if question_id in questions_by_id:
                    category = questions_by_id[question_id]['category']
                    # Convert response to numerical score (1-5)
                    score = int(value)
                    # Add score to appropriate category
                    category_scores[category].append(score)
            except (ValueError, KeyError):
                # Skip invalid entries
                continue
    
    # Calculate average score for each category
    results = {}
    for category in categories:
        if category_scores[category]:
            avg_score = sum(category_scores[category]) / len(category_scores[category])
            results[category] = round(avg_score, 1)
        else:
            results[category] = 0.0
    
    return results

def get_sample_assessment_result():
    """
    Generate a sample assessment result for demonstration purposes
    
    Returns:
        dict: Dictionary of simulated aptitude scores
    """
    questions = get_assessment_questions()
    assessment_data = {}
    
    # Simulate random responses
    for question in questions:
        assessment_data[f'q{question["id"]}'] = str(random.randint(1, 5))
    
    return process_assessment_results(assessment_data)

def interpret_assessment_result(result):
    """
    Provide an interpretation of assessment results
    
    Args:
        result (dict): Dictionary of aptitude scores
        
    Returns:
        dict: Interpretation of each aptitude score and overall profile
    """
    # Sort aptitudes by score (descending)
    sorted_aptitudes = sorted(result.items(), key=lambda x: x[1], reverse=True)
    top_aptitudes = sorted_aptitudes[:2]
    
    # Define interpretations for each aptitude
    aptitude_descriptions = {
        'analytical': {
            'high': 'You have strong analytical abilities, suggesting you would excel in careers that involve problem-solving, logical reasoning, and critical thinking. You likely enjoy understanding complex systems and analyzing data to draw conclusions.',
            'medium': 'You have moderate analytical abilities, suggesting you can engage with logical problems and systematic thinking but might not find deep analytical work to be your primary strength.',
            'low': 'Your analytical abilities appear less dominant in your profile, suggesting you might prefer careers that emphasize other strengths rather than detailed analysis or complex problem-solving.'
        },
        'creative': {
            'high': 'You show strong creative aptitude, suggesting you would thrive in environments that value innovation, artistic expression, and unconventional thinking. You likely enjoy generating new ideas and finding unique solutions.',
            'medium': 'You have moderate creative abilities, suggesting you can engage with creative tasks and appreciate innovation, but might balance this with more structured approaches.',
            'low': 'Your creative aptitude appears less dominant in your profile, suggesting you might prefer more structured and defined activities rather than open-ended creative work.'
        },
        'practical': {
            'high': 'You display strong practical aptitude, suggesting you would excel in careers that involve hands-on work, building, fixing, or operating equipment. You likely enjoy seeing tangible results from your efforts.',
            'medium': 'You have moderate practical abilities, suggesting you can engage effectively with hands-on tasks while also valuing other types of work.',
            'low': 'Your practical aptitude appears less dominant in your profile, suggesting you might prefer more conceptual or interpersonal work rather than hands-on technical tasks.'
        },
        'social': {
            'high': 'You show strong social aptitude, suggesting you would thrive in careers involving interaction, communication, and helping others. You likely enjoy building relationships and working collaboratively.',
            'medium': 'You have moderate social abilities, suggesting you can work effectively with others while also valuing some independent work.',
            'low': 'Your social aptitude appears less dominant in your profile, suggesting you might prefer careers with more independent work rather than those centered on frequent interaction.'
        },
        'conventional': {
            'high': 'You display strong conventional aptitude, suggesting you would excel in structured environments with clear procedures and attention to detail. You likely value organization, accuracy, and systematic approaches.',
            'medium': 'You have moderate conventional abilities, suggesting you can work effectively with systems and procedures while also adapting to less structured situations.',
            'low': 'Your conventional aptitude appears less dominant in your profile, suggesting you might prefer more flexible or creative environments rather than highly structured ones.'
        },
        'enterprising': {
            'high': 'You show strong enterprising aptitude, suggesting you would thrive in leadership, business, or persuasive roles. You likely enjoy taking initiative, making decisions, and influencing others.',
            'medium': 'You have moderate enterprising abilities, suggesting you can take leadership when needed while also being comfortable in collaborative or supporting roles.',
            'low': 'Your enterprising aptitude appears less dominant in your profile, suggesting you might prefer collaborative or specialist roles rather than those centered on leadership or persuasion.'
        }
    }
    
    # Generate interpretations for each aptitude
    interpretations = {}
    for aptitude, score in result.items():
        if score >= 4.0:
            level = 'high'
        elif score >= 3.0:
            level = 'medium'
        else:
            level = 'low'
        
        interpretations[aptitude] = {
            'score': score,
            'level': level,
            'description': aptitude_descriptions[aptitude][level]
        }
    
    # Generate overall profile interpretation based on top aptitudes
    top_combo = f"{top_aptitudes[0][0]}_{top_aptitudes[1][0]}"
    
    # Dictionary of combination interpretations
    combo_interpretations = {
        'analytical_creative': 'Your combination of analytical and creative strengths suggests you might excel in fields that require innovative problem-solving, such as research and development, data science, or certain engineering disciplines where creativity in approach is valued.',
        'analytical_practical': 'Your combination of analytical and practical strengths suggests you might excel in fields that require hands-on problem-solving, such as engineering, technical troubleshooting, or applied scientific research.',
        'analytical_social': 'Your combination of analytical and social strengths suggests you might excel in fields that require analyzing human behavior or communicating complex information, such as certain psychology roles, management consulting, or technical training.',
        'analytical_conventional': 'Your combination of analytical and conventional strengths suggests you might excel in fields that require systematic analysis and attention to detail, such as financial analysis, quality assurance, or certain research roles.',
        'analytical_enterprising': 'Your combination of analytical and enterprising strengths suggests you might excel in fields that require data-driven leadership, such as technical management, data-oriented business roles, or entrepreneurship in technical fields.',
        
        'creative_analytical': 'Your combination of creative and analytical strengths suggests you might excel in fields that require innovative approaches guided by logical thinking, such as design engineering, architectural design, or scientific innovation.',
        'creative_practical': 'Your combination of creative and practical strengths suggests you might excel in fields that involve making or building artistic products, such as craftsmanship, product design, or certain engineering specialties.',
        'creative_social': 'Your combination of creative and social strengths suggests you might excel in fields that combine artistic expression with human interaction, such as teaching arts, art therapy, or collaborative creative disciplines.',
        'creative_conventional': 'Your combination of creative and conventional strengths suggests you might excel in fields that require creative output within structured parameters, such as graphic design, technical writing, or certain architectural roles.',
        'creative_enterprising': 'Your combination of creative and enterprising strengths suggests you might excel in fields that require innovative leadership, such as creative direction, design management, or entrepreneurship in creative industries.',
        
        'practical_analytical': 'Your combination of practical and analytical strengths suggests you might excel in fields that require hands-on technical problem-solving, such as engineering, technical troubleshooting, or certain scientific roles.',
        'practical_creative': 'Your combination of practical and creative strengths suggests you might excel in fields that involve making innovative physical products or spaces, such as product design, certain construction specialties, or technical artisanship.',
        'practical_social': 'Your combination of practical and social strengths suggests you might excel in fields that combine hands-on work with helping others, such as certain healthcare roles, vocational education, or community-oriented technical work.',
        'practical_conventional': 'Your combination of practical and conventional strengths suggests you might excel in fields that require meticulous hands-on work following established procedures, such as precision manufacturing, certain healthcare technician roles, or quality control.',
        'practical_enterprising': 'Your combination of practical and enterprising strengths suggests you might excel in fields that involve leading technical projects or teams, such as construction management, technical supervision, or entrepreneurship in practical fields.',
        
        'social_analytical': 'Your combination of social and analytical strengths suggests you might excel in fields that require understanding and analyzing human behavior, such as psychology, certain healthcare roles, or data-driven marketing.',
        'social_creative': 'Your combination of social and creative strengths suggests you might excel in fields that require innovative approaches to human interaction, such as counseling, certain educational roles, or experience design.',
        'social_practical': 'Your combination of social and practical strengths suggests you might excel in fields that combine helping people with hands-on work, such as occupational therapy, coaching, or certain healthcare roles.',
        'social_conventional': 'Your combination of social and conventional strengths suggests you might excel in fields that require organized approaches to helping others, such as healthcare administration, educational administration, or certain social services roles.',
        'social_enterprising': 'Your combination of social and enterprising strengths suggests you might excel in fields that involve leading and motivating others, such as management, sales, education leadership, or nonprofit administration.',
        
        'conventional_analytical': 'Your combination of conventional and analytical strengths suggests you might excel in fields that require systematic analysis and attention to detail, such as accounting, certain legal roles, or quality assurance.',
        'conventional_creative': 'Your combination of conventional and creative strengths suggests you might excel in fields that require creativity within structured parameters, such as certain design roles, technical writing, or event planning.',
        'conventional_practical': 'Your combination of conventional and practical strengths suggests you might excel in fields that require meticulous hands-on work following established procedures, such as medical technology, laboratory work, or precision manufacturing.',
        'conventional_social': 'Your combination of conventional and social strengths suggests you might excel in fields that require organized approaches to working with people, such as human resources, administrative support in educational or healthcare settings, or certain customer service roles.',
        'conventional_enterprising': 'Your combination of conventional and enterprising strengths suggests you might excel in fields that involve leadership in structured environments, such as administrative management, compliance management, or certain financial roles.',
        
        'enterprising_analytical': 'Your combination of enterprising and analytical strengths suggests you might excel in fields that require data-driven leadership, such as business analytics, investment banking, or technical management.',
        'enterprising_creative': 'Your combination of enterprising and creative strengths suggests you might excel in fields that require innovative leadership, such as marketing management, product development leadership, or entrepreneurship in creative industries.',
        'enterprising_practical': 'Your combination of enterprising and practical strengths suggests you might excel in fields that involve leading technical operations, such as operations management, construction management, or entrepreneurship in practical industries.',
        'enterprising_social': 'Your combination of enterprising and social strengths suggests you might excel in fields that require motivating and directing others, such as sales management, educational administration, or nonprofit leadership.',
        'enterprising_conventional': 'Your combination of enterprising and conventional strengths suggests you might excel in fields that involve leadership in structured environments, such as financial management, operations management, or administration.'
    }
    
    # Default interpretation if combination not found
    overall_interpretation = combo_interpretations.get(
        top_combo,
        'Your unique combination of strengths suggests you might excel in fields that allow you to leverage your top aptitudes together. Consider careers that combine elements of both areas.'
    )
    
    return {
        'aptitudes': interpretations,
        'overall': overall_interpretation,
        'top_aptitudes': [aptitude for aptitude, score in top_aptitudes]
    }