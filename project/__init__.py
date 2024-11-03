from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_required, current_user    
from .extensions import db

from .models import User 
def create_app(event=None, context=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:8TKf4LMBNrQ-izo2XAGrR4fKmgwLubRqxJq@postgres-db.cvq642g6w293.us-west-2.rds.amazonaws.com:5432/flask_sql_auth'
    print("init db")
    db.init_app(app)
    print("load db")
    with app.app_context():
        from . import models    
        db.create_all()
    
    print("init app")
    login_manager = LoginManager()
    login_manager.init_app(app)

    print("query db")
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()

    print("register blueprint")
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    print("return app model")
    return app
