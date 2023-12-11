from flask import Blueprint, render_template,request, flash, jsonify
from flask_login import login_required, current_user
import json
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
    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    req_data = json.loads(request.data)
    note_id = req_data['noteID']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({'message': 'Note deleted.'})
    else:
        return jsonify({'message': 'Note cannot be deleted.'})
