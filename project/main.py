from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for, Blueprint
from flask_login import login_required, current_user, LoginManager
import requests
import json
import random
from .extensions import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)
points = []

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)


# if __name__ == '__main__':
#     app.run(debug=True, port=2233)
