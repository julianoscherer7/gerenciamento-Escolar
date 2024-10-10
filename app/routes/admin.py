from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from models import *
from .auth import admin_required

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@admin_required
def admin_panel():
    usuario = Usuario.query.get(session['user_id'])
    return render_template('admin_panel.html', usuario=usuario)
