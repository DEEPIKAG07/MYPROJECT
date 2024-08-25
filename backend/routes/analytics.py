from flask import Blueprint, jsonify
from app import db
from models.grievance import Grievance
from sqlalchemy import func
from flask_jwt_extended import jwt_required

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics', methods=['GET'])
@jwt_required()
def get_analytics():
    grievances_by_month = db.session.query(func.strftime('%Y-%m', Grievance.created_at).label('month'), func.count('*')).group_by('month').all()
    return jsonify(grievances_by_month), 200
