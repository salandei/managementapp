from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password.', category='error')
        else:
            flash('User does not exist.', category='error')
    return render_template('login.html', user=current_user)

@auth.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fullname) < 2:
            flash('Your name must be greater than 2 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        elif password != confirm_password:
            flash('Your passwords do not match.', category='error')
        else:

            new_user = User(email=email, fullname=fullname, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('User account created successfully', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.index'))

    return render_template('create_account.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
