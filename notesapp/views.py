from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views  = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Submitted note wass empty.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully.', category='success')
    else:
        return render_template('home.html', user=current_user)
