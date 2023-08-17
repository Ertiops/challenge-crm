from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.models import Reservations
import crud
from blueprints.admin.admin import admin



app = Flask(__name__, template_folder='./templates')
# app.config.from_object(__name__)
app.config['SECRET_KEY'] = "lskhglojihslsJHBShuldsBGHD12436"

app.register_blueprint(admin, url_prefix="/admin")

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = crud.check_user(email, password)
        if result is None or result is False:
            flash("Неверный Email или пароль", category="danger")
        else:
            role = crud.get_user(email).role
            if role == 'owner':
                return redirect(url_for('admin.statistics'))


    return render_template('login.html')


@app.route("/formfields", methods=['GET', 'POST'])
def formfields():
    return render_template('formfields.html')

@app.route("/formreturns", methods=['GET', 'POST'])
def formreturns():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    quest = request.form['quest']
    date = request.form['date']
    time = request.form['time']
    guest_num = request.form['guest_num']
    price = request.form['price']
    franchise = request.form['franchise']

    add_reservation(name, phone, email, quest, date, time, guest_num, price, franchise)

    return redirect(url_for('login'))
    # return str(date)


def add_reservation(name, phone, mail, quest, date, time, guest_number, price, franchise):
    reservations = Reservations(
        name = name,
        phone = phone,
        mail = mail,
        quest = quest,
        date = date,
        time = time,
        guest_number = guest_number,
        price = price,
        franchise = franchise
        )
    crud.session.add(reservations)
    crud.session.commit()


if __name__ == "__main__":
    app.run(debug=True)