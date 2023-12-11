from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.email
        password = request.form.password
    return render_template("login.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fullname) < 2:
            flash('Your name must be greater than 2 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        elif password != confirm_password:
            flash('Your passwords do not match.', category='error')
        else:
            flash('User account created successfully', category='success')

    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return '<p>logout</p>'
