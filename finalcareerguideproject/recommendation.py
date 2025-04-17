"""
Module for generating career recommendations based on assessment results
"""
from models import CareerPath
from sqlalchemy import desc

def get_career_recommendations(assessment_result, limit=5):
    """
    Generate career recommendations based on assessment results
    
    Args:
        assessment_result: An AssessmentResult object with aptitude scores
        limit (int): Maximum number of recommendations to return
        
    Returns:
        list: List of recommended CareerPath objects with match scores
    """
    # Get all career paths from the database
    all_careers = CareerPath.query.all()
    
    # Get the user's aptitude scores
    user_scores = assessment_result.get_scores_dict()
    
    # Calculate match scores for each career
    career_matches = []
    
    for career in all_careers:
        # Get the relevance scores for this career
        relevance_scores = career.get_relevance_scores()
        
        # Calculate the match score using weighted sum
        match_score = calculate_match_score(user_scores, relevance_scores)
        
        career_matches.append({
            'career': career,
            'match_score': match_score
        })
    
    # Sort careers by match score (descending)
    career_matches.sort(key=lambda x: x['match_score'], reverse=True)
    
    # Take the top matches
    top_matches = career_matches[:limit]
    
    return top_matches

def calculate_match_score(user_scores, relevance_scores):
    """
    Calculate a match score between user aptitudes and career relevance scores
    
    Args:
        user_scores (dict): Dictionary of user's aptitude scores
        relevance_scores (dict): Dictionary of career's aptitude relevance scores
        
    Returns:
        float: Match score as a percentage (0-100)
    """
    # Initialize weighted sum and weights
    weighted_sum = 0
    total_relevance = 0
    
    # Calculate match score with more weight on high-relevance aptitudes
    for aptitude in user_scores:
        user_score = user_scores[aptitude]
        relevance = relevance_scores[aptitude]
        
        # Skip if relevance is 0
        if relevance == 0:
            continue
        
        # Calculate how well the user's score matches the relevance
        # If the relevance is high, we want the user to have a high score
        # If the relevance is low, it doesn't matter as much
        match = (user_score / 5) * relevance
        
        weighted_sum += match
        total_relevance += relevance
    
    # Calculate final score as percentage
    if total_relevance > 0:
        match_percentage = (weighted_sum / total_relevance) * 100
    else:
        match_percentage = 0
    
    return round(match_percentage, 1)

def get_aptitude_improvement_suggestions(user_scores, career):
    """
    Generate suggestions for improving aptitudes based on career requirements
    
    Args:
        user_scores (dict): Dictionary of user's aptitude scores
        career: A CareerPath object
        
    Returns:
        dict: Dictionary of aptitudes that need improvement with suggestions
    """
    relevance_scores = career.get_relevance_scores()
    
    # Find areas that need improvement
    improvements = {}
    
    for aptitude, relevance in relevance_scores.items():
        # Only suggest improvements for aptitudes with high relevance
        if relevance >= 3.5:
            user_score = user_scores[aptitude]
            
            # If user score is notably lower than the relevance, suggest improvement
            gap = relevance - user_score
            if gap > 1:
                improvements[aptitude] = {
                    'user_score': user_score,
                    'relevance': relevance,
                    'gap': gap,
                    'suggestion': get_aptitude_suggestion(aptitude)
                }
    
    return improvements

def get_aptitude_suggestion(aptitude):
    """
    Get a suggestion for improving a specific aptitude
    
    Args:
        aptitude (str): The aptitude to improve
        
    Returns:
        str: A suggestion for improving the aptitude
    """
    suggestions = {
        'analytical': "Consider activities that strengthen your logical reasoning and problem-solving skills like puzzles, math games, or programming exercises.",
        'creative': "Try expressing yourself through art, music, writing, or design projects. Creative thinking can be developed through practice.",
        'practical': "Engage in hands-on activities like DIY projects, building models, or learning to use tools and equipment.",
        'social': "Practice communication skills by joining group activities, volunteering, or participating in discussions. Building empathy through understanding others' perspectives can help.",
        'conventional': "Try organizing tasks and projects with clear steps. Practice attention to detail by proofreading or organizing your study materials.",
        'enterprising': "Take on leadership roles in school activities, practice public speaking, or try persuasive writing to develop convincing communication skills."
    }
    
    return suggestions.get(aptitude, "Focus on developing this skill through practice and learning.")
