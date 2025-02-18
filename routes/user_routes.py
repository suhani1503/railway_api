from flask import Blueprint, request, jsonify
from app import db
from models import Train, Booking
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

@user_bp.route('/get_seat_availability', methods=['GET'])
def get_seat_availability():
    source = request.args.get('source')
    destination = request.args.get('destination')

    trains = Train.query.filter_by(source=source, destination=destination).all()
    availability = []

    for train in trains:
        availability.append({
            'train_id': train.id,
            'source': train.source,
            'destination': train.destination,
            'seats_available': train.seats
        })

    return jsonify(availability), 200

@user_bp.route('/book_seat', methods=['POST'])
@jwt_required()
def book_seat():
    data = request.get_json()
    train_id = data['train_id']
    seats_to_book = data['seats_to_book']
    user_identity = get_jwt_identity()

    train = Train.query.get(train_id)

    if train.seats < seats_to_book:
        return jsonify({"message": "Not enough seats available"}), 400

    train.seats -= seats_to_book
    booking = Booking(user_id=user_identity, train_id=train.id, seats_booked=seats_to_book)
    db.session.add(booking)
    db.session.commit()

    return jsonify({"message": "Seats booked successfully"}), 200
