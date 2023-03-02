from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from .models import Note
from .models import Transaction
from . import db
import json
import pandas as pd

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        date = request.form.get('date')
        category = request.form.get('category')
        income = request.form.get('income')
        outcome = request.form.get('outcome')
        des = request.form.get('des')

        if len(date) < 1 | len(category) < 1: # wrong condition
            flash('transaction is invalid', category='error')
        else:
            new_transaction = Transaction(date=date, category=category, income=income, outcome=outcome, des=des, user_id=current_user.id, )
            db.session.add(new_transaction)
            db.session.commit()
            flash('transaction is added', category='success')
    
    return render_template("home.html", user=current_user)
    # if request.method == 'POST':
    #     note = request.form.get('note')

    #     if len(note) < 1:
    #         flash('note is too short', category='error')
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('note is added', category='success')

    # return render_template("home.html", user=current_user)


# @views.route('/month', methods=['GET'])
# def month():
    # query = f"SELECT SUM(outcome) FROM transactions WHERE EXTRACT(MONTH FROM date) = {month}"
    # df = pd.read_sql(query, engine)
    # return df.iloc[0][0]

# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Transaction.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})