from models.grievance import Grievance

def generate_analytics():
    total_grievances = Grievance.query.count()
    pending_grievances = Grievance.query.filter_by(status='Pending').count()
    resolved_grievances = Grievance.query.filter_by(status='Resolved').count()
    
    category_breakdown = {}
    grievances_by_category = Grievance.query.with_entities(Grievance.category, db.func.count(Grievance.id)).group_by(Grievance.category).all()
    for category, count in grievances_by_category:
        category_breakdown[category] = count

    analytics = {
        'total_grievances': total_grievances,
        'pending_grievances': pending_grievances,
        'resolved_grievances': resolved_grievances,
        'category_breakdown': category_breakdown
    }
    return analytics

