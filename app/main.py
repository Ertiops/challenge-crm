from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask import Flask, render_template, request, redirect, url_for, flash, abort, current_app
from flask_redmail import RedMail
from werkzeug.security import check_password_hash
from crud import OwnersCRUD, EmployeesCRUD, ReservationsCRUD, session
from models.models import Users, Owners
from blueprints.admin.admin import admin
import jwt



app = Flask(__name__, template_folder='./templates')
app.config['SECRET_KEY'] = "lskhglojihslsJHBShuldsBGHD12436"

app.register_blueprint(admin, url_prefix="/admin")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
mail = RedMail()

app.config["EMAIL_HOST"] = "smtp.gmail.com"
app.config['EMAIL_PORT'] = 587
app.config['EMAIL_USERNAME'] = 'zzzeni42@gmail.com'
app.config['EMAIL_PASSWORD'] = 'qjxc ttrf fjao rlga'
mail.init_app(app)


@login_manager.user_loader
def load_user(user_id: str):
    employee = EmployeesCRUD.get_employee_by_id(user_id)
    if employee:
        return employee
    else:
        owner = OwnersCRUD.get_owner_by_id(user_id)
        if owner:
            return owner
    return None

@app.route("/vefify-email/<token>")
def verify_email(token):
    data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=['HS256'])
    email = data["email"]
    user = session.query(Users).filter_by(email=email).first()
    user.verified = True
    session.commit()
    return redirect(url_for('admin.statistics'))


@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.role != "владелец":
            # заменить на начальную страницу блюпринта, когда у работников он появится            
            return redirect(url_for('admin.franchises'))
        else:
            return redirect(url_for('admin.statistics'))     
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = EmployeesCRUD.get_user(email)
            if user:
                if check_password_hash(user.password_hash, password):
                    login_user(user)
                    print("yes")
                    if current_user.verified != True:
                        token = jwt.encode({"email": email}, current_app.config["SECRET_KEY"])
                        mail.send(
                        subject="Verify email",
                        receivers=email,
                        html_template="verify.html",
                        body_params={
                            "token": token
                        }
                    )
                    return redirect(url_for('admin.franchises'))
                else:
                    flash("Неверный пароль", category="primary")
                    return redirect(url_for('login'))
            else:
                flash("Неверный Email", category="primary")
                return redirect(url_for('login'))    
                        

    return render_template('login.html')


@app.route("/login_owner", methods=['GET', 'POST'])
def login_owner():   
    if current_user.is_authenticated:
        if current_user.role == "владелец":
            return redirect(url_for('admin.statistics'))
        else:
            # заменить на начальную страницу блюпринта, когд у работников он появится
            return redirect(url_for('admin.franchises')) 
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            owner = OwnersCRUD.get_owner(email)
            if owner:
                if check_password_hash(owner.password_hash, password):
                    login_user(owner)
                    return redirect(url_for('admin.statistics'))
                else:
                    flash("Неверный пароль", category="primary")
                    return redirect(url_for('login_owner'))
            else:
                flash("Неверный Email", category="primary")
                return redirect(url_for('login_owner'))               
    return render_template('login_owner.html')


@app.route("/logout/<role>", methods=['GET', 'POST'])
@login_required
def logout(role):
    logout_user()
    flash('Вы вышли из системы', category="primary")    
    if role == "владелец":
        return redirect(url_for('login_owner'))
    else:
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

    ReservationsCRUD.add_reservation(name, phone, email, quest, date, time, guest_num, price, franchise)

    return redirect(url_for('login'))
    # return str(date)


if __name__ == "__main__":
    app.run(debug=True)