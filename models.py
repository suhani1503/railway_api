from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    # Relationship with Booking
    bookings = db.relationship('Booking', backref='user', lazy=True)

class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    seats = db.Column(db.Integer, nullable=False)

    # Relationship with Booking
    bookings = db.relationship('Booking', backref='train', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    train_id = db.Column(db.Integer, db.ForeignKey('train.id'), nullable=False)
    seats_booked = db.Column(db.Integer, nullable=False)

    # Optional: Add user & train references for easier querying
    user = db.relationship('User', back_populates='bookings')
    train = db.relationship('Train', back_populates='bookings')
