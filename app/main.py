from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask import Flask, render_template, request, redirect, url_for, flash, abort, session
from werkzeug.security import check_password_hash
import crud
from models.models import Users, Owners
from blueprints.admin.admin import admin
import custom_defs



app = Flask(__name__, template_folder='./templates')
# app.config.from_object(__name__)
app.config['SECRET_KEY'] = "lskhglojihslsJHBShuldsBGHD12436"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return crud.session.query(Users).get(str(user_id))

@login_manager.user_loader
def load_user(user_id):
    return crud.session.query(Owners).get(str(user_id))


app.register_blueprint(admin, url_prefix="/admin")



@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.statistics')) 
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            role = crud.get_user(email).role
            user = crud.session.query(Users).filter_by(email=email).first()
            if user:
                if check_password_hash(user.password_hash, password):
                    login_user(user)
                    if role == ('администратор' or 'франчайзер' or 'работник' or 'оператор'):
                        return redirect(url_for('admin.statistics'))
                    else:
                        abort(401)
                else:
                    flash("Неверный Email или пароль", category="danger")

    return render_template('login.html')

@app.route("/login_owner", methods=['GET', 'POST'])
def login_owner():
    
    if current_user.is_authenticated:
        return redirect(url_for('admin.statistics'))
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            role = crud.get_owner(email).role
            user = crud.session.query(Owners).filter_by(email=email).first()
            if user:
                if check_password_hash(user.password_hash, password):
                    login_user(user)
                    if role == 'владелец':
                        return redirect(url_for('admin.statistics'))
                    else:
                        abort(401)
                else:
                    flash("Неверный Email или пароль", category="danger")

    return render_template('login_owner.html')


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', category="primary")
    return redirect(url_for('login'))





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

    crud.add_reservation(name, phone, email, quest, date, time, guest_num, price, franchise)

    return redirect(url_for('login'))
    # return str(date)


if __name__ == "__main__":
    app.run(debug=True)