from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from extensions import db, jwt, migrate
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database and JWT manager
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate.init_app(app, db)

# Root route to avoid 404
@app.route('/')
def home():
    return 'Welcome to the API!'  # You can customize this message as needed

# Favicon route
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

from routes import auth_routes, admin_routes, user_routes

# Register blueprints for routes
app.register_blueprint(auth_routes.auth_bp, url_prefix='/auth')
app.register_blueprint(admin_routes.admin_bp, url_prefix='/admin')
app.register_blueprint(user_routes.user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
