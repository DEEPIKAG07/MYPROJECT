import random

def predict_response_time(grievance):
    # Simplified version: Randomly assign an estimated response time based on priority
    if grievance.priority == 'High':
        return random.randint(1, 2)  # 1-2 days
    elif grievance.priority == 'Medium':
        return random.randint(3, 5)  # 3-5 days
    else:
        return random.randint(6, 10)  # 6-10 days


