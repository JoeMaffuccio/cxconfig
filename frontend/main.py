from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from backend.database import db
import requests
import json

main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/client')
@login_required
def client():
    response = requests.get('http://127.0.0.1:19999/api/client')
    return render_template('client.html', name=current_user.name, clients=json.loads(response.text))
    
@main_blueprint.route('/pos', methods=['POST','GET'])
def pos():
    clientid = request.form.get('clients')
    response = requests.get('http://127.0.0.1:19999/api/pos/' + clientid)
    return render_template('pos.html', poss=json.loads(response.text))
