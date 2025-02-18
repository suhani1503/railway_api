from app import db
from models import Train, Booking

def check_availability(train_id, seats_to_book):
    train = Train.query.get(train_id)
    if train.seats >= seats_to_book:
        return True
    return False

def process_booking(user_id, train_id, seats_to_book):
    train = Train.query.get(train_id)
    train.seats -= seats_to_book
    booking = Booking(user_id=user_id, train_id=train.id, seats_booked=seats_to_book)
    db.session.add(booking)
    db.session.commit()
