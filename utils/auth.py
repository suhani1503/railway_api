from flask_jwt_extended import get_jwt_identity
from models import User

def is_admin():
    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity).first()
    return user.role == 'admin'
