from app import db
from models.user import User
from models.grievance import Grievance

def init_db():
    db.create_all()

    # Create admin user
    admin = User(username='admin')
    admin.set_password('adminpass')
    db.session.add(admin)
    db.session.commit()

if __name__ == '__main__':
    init_db()

