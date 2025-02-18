from flask import Blueprint, request, jsonify
from extensions import db
from models import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    role = data['role']

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    user = User(username=username, password=password, role=role)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
