from flask import Blueprint, render_template, redirect, url_for, flash, session, request, send_from_directory
from models import *
from .auth import login_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.home'))

@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/static/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('templates/static/img', filename)
