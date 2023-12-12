from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

from . import home

@home.route('/')
def homepage():
    """
    Render the login template on the / route
    """
    return redirect(url_for('auth.login'))

#dashboard view
@home.route('/users')
@login_required
def users():
    return render_template('users.html', title="Users")

