from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

@auth.route('/create_account', methods=['GET', 'POST'])
def create_account():
    """
    Handle requests to the /create_account route
    Add a user to the database through the registration form
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.', 'success')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('create_account.html', form=form, title='Create Account')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('home.users'))

        # when login details are incorrect
        else:
            flash('Invalid email or password', 'error')

    # load login template
    return render_template('login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
