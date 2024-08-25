from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from models.user import User
from models.grievance import Grievance
from services.grievance_service import process_grievance
from services.analytics_service import generate_analytics
from routes.admin import admin_bp
from routes.analytics import analytics_bp
app.register_blueprint(admin_bp)
app.register_blueprint(analytics_bp)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grievanceai.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this!
db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/grievance', methods=['POST'])
@jwt_required()
def submit_grievance():
    data = request.json
    new_grievance = Grievance(user_id=data['user_id'], content=data['content'])
    db.session.add(new_grievance)
    db.session.commit()
    process_grievance(new_grievance)
    return jsonify({"msg": "Grievance submitted successfully"}), 201

@app.route('/grievance/<int:grievance_id>', methods=['GET'])
@jwt_required()
def get_grievance(grievance_id):
    grievance = Grievance.query.get_or_404(grievance_id)
    return jsonify(grievance.to_dict()), 200

@app.route('/analytics', methods=['GET'])
@jwt_required()
def get_analytics():
    analytics = generate_analytics()
    return jsonify(analytics), 200

if __name__ == '__main__':
    app.run(debug=True)
