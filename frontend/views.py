from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

frontend_page = Blueprint('simple_page', __name__, template_folder='templates')

@frontend_page.route('/')
def index():
    try:
        context = {"user": 'Joe'}
        return render_template('login.html', context=context)
    except TemplateNotFound:
        abort(404)