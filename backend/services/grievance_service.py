from ai.nlp.text_classifier import classify_text
from ai.nlp.sentiment_analyzer import analyze_sentiment
from ai.predictive.response_time_predictor import predict_response_time

def process_grievance(grievance):
    # Classify the grievance
    grievance.category = classify_text(grievance.content)
    
    # Analyze sentiment
    sentiment = analyze_sentiment(grievance.content)
    
    # Set priority based on sentiment and other factors
    grievance.priority = set_priority(sentiment, grievance.category)
    
    # Predict response time
    estimated_response_time = predict_response_time(grievance)
    
    # Update grievance in database
    grievance.estimated_response_time = estimated_response_time
    db.session.commit()

def set_priority(sentiment, category):
    # Logic to set priority based on sentiment and category
    # This is a simplified version
    if sentiment == 'very negative' or category == 'urgent':
        return 'High'
    elif sentiment == 'negative':
        return 'Medium'
    else:
        return 'Low'
