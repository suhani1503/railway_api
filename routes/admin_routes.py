from flask import Blueprint, request, jsonify
from app import db
from models import Train
from flask_jwt_extended import jwt_required



admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/add_train', methods=['POST'])
@jwt_required()
def add_train():
    data = request.get_json()
    source = data['source']
    destination = data['destination']
    seats = data['seats']

    new_train = Train(source=source, destination=destination, seats=seats)
    db.session.add(new_train)
    db.session.commit()

    return jsonify({"message": "Train added successfully"}), 201
