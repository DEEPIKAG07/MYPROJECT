from flask import Blueprint, request, jsonify
from app import db
from models.grievance import Grievance
from flask_jwt_extended import jwt_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/grievances', methods=['GET'])
@jwt_required()
def get_all_grievances():
    grievances = Grievance.query.all()
    return jsonify([grievance.to_dict() for grievance in grievances]), 200

@admin_bp.route('/admin/grievance/<int:grievance_id>', methods=['PATCH'])
@jwt_required()
def update_grievance(grievance_id):
    data = request.json
    grievance = Grievance.query.get_or_404(grievance_id)
    grievance.status = data.get('status', grievance.status)
    db.session.commit()
    return jsonify(grievance.to_dict()), 200

