from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)

    # SQLAlchemy configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/books_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Register the blueprint from routes.py
    from .routes import bp
    app.register_blueprint(bp)

    return app
