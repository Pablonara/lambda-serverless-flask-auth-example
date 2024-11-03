from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:8TKf4LMBNrQ-izo2XAGrR4fKmgwLubRqxJq@postgres-db.cvq642g6w293.us-west-2.rds.amazonaws.com:5432/flask_sql_auth'
    
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .models import User  # Import after db.init_app
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()  # This should work within app context

    # Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
