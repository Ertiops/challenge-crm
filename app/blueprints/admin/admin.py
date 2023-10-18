from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify
import uuid0
import crud
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash


admin = Blueprint("admin", __name__, template_folder="templates", static_folder='static')


# не тргоай пока
@admin.route("/", methods=['GET'])
def statistics():
    return render_template('statistics.html', title='Статистика')

@admin.route("/franchises", methods=['GET', 'POST'])
def franchises():
    franchises = crud.get_franchises_and_employees_count()
    if request.method == 'POST':
        if request.form['submit'] == 'register':        
            id = uuid0.generate()
            city = request.form['city'].capitalize()
            crud.add_franchise(id, city)
            return redirect(url_for('admin.franchises'))         
        elif request.form['submit'] == 'delete':
            provided_password = request.form['password']
            is_valid = check_password_hash(current_user.password_hash, provided_password)
            if is_valid:
               franchise_id = request.form['franchise_id']
               crud.delete_franchise(franchise_id)              
               return redirect(url_for('admin.franchises'))
            else:
                modal_index = request.form['modal_index']
                flash("Пароль неверный", category=f"delete danger {modal_index}")
                return redirect(url_for('admin.franchises'))
        elif request.form['submit'] == 'update':
            city = request.form['city'].capitalize()
            if city:
                franchise_id = request.form['franchise_id']
                crud.update_franchise(franchise_id, city)               
                return redirect(url_for('admin.franchises'))
            else:
                modal_index = request.form['modal_index']
                flash("Поле должно быть заполнено", category=f"update danger {modal_index}")
                return redirect(url_for('admin.franchises'))





       
    return render_template('franchises.html', title='Франшизы', franchises=franchises)



@admin.route("/employees", methods=['GET'])
def employees():
    franchises = crud.get_franchises_and_franchiser()
        
    return render_template('employees.html', title='Сотрудники', franchises=franchises)

@admin.route("/employees/<franchise_id>", methods=['GET', 'POST'])
def franchise_employees(franchise_id):
    actors = crud.get_employees(franchise_id, role='актёр')
    admins = crud.get_employees(franchise_id, role='администратор')
    operators = crud.get_employees(franchise_id, role='оператор')
    bosses = crud.get_bosses(franchise_id)

    if request.method == "POST":
        email = request.form['email']
        phone = request.form['phone']
        is_email_unique = crud.is_email_unique(email)
        is_phone_unique = crud.is_phone_unique(email)

        if is_email_unique and is_phone_unique:
            id = uuid0.generate()
            role = request.form['role']
            first_name = request.form['firstName'].capitalize()
            last_name = request.form['lastName'].capitalize()
            patronymic = request.form['patronymic'].capitalize()
            password = request.form['password']
            crud.add_user(id, first_name, last_name, patronymic, email, phone, password, role, franchise_id)
            return redirect(url_for('admin.franchise_employees', franchise_id=franchise_id))  
        elif not is_email_unique:
            flash("Данный email уже зарегистрирован", category="danger") 
            return redirect(url_for('admin.franchise_employees', franchise_id=franchise_id))
        elif not is_phone_unique:
            flash("Данный номер уже зарегистрирован", category="danger") 
            return redirect(url_for('admin.franchise_employees', franchise_id=franchise_id))               
        
    return render_template('franchise_employees.html', title='Сотрудники', 
                                                       actors=actors, admins=admins, 
                                                       operators=operators, bosses=bosses, 
                                                       franchise_id=franchise_id)


@admin.route("/update_user", methods=['GET', 'POST'])
def update_user():
    franchise_id = request.args.get('franchise_id', None)
    user_email = request.args.get('user_email', None)
    user = crud.get_user(user_email)
    if request.method == 'POST':
        if request.form['submit'] == 'update':
            email = request.form['email']
            phone = request.form['phone']
            unique_email = crud.is_email_unique_except_current(user.id, email)
            unique_phone = crud.is_phone_unique_except_current(user.id, phone)
            if unique_email and unique_phone:
                role = request.form['role']
                first_name = request.form['firstName'].capitalize()
                last_name = request.form['lastName'].capitalize()
                patronymic = request.form['patronymic'].capitalize()
                result_user = crud.update_user(id, first_name, last_name, patronymic, email, user_email, phone, role)
                if result_user:
                    flash("Данные обновлены успешно", category="update success") 
                    return redirect(url_for('admin.update_user', user_email=email, franchise_id=franchise_id))
            elif not unique_email:
                flash("Данный email уже зарегистрирован", category="update danger") 
                return redirect(url_for('admin.update_user', user_email=user_email, franchise_id=franchise_id))
            elif not unique_phone:
                flash("Данный номер уже зарегистрирован", category="update danger") 
                return redirect(url_for('admin.update_user', user_email=user_email, franchise_id=franchise_id))                             
        elif request.form['submit'] == 'delete':
            provided_password = request.form['password']
            is_valid = check_password_hash(current_user.password_hash, provided_password)
            if is_valid:
               crud.delete_user(user_email)
               return redirect(url_for('admin.franchise_employees', franchise_id=franchise_id))
            else:
                flash("Пароль неверный", category="delete danger")
                return redirect(url_for('admin.update_user', user_email=user_email, franchise_id=franchise_id))        
    

    return render_template('update_user.html', title='Сотрудники', user=user)



# добавка в бд бронирований



# отсылка данных в другой роутер и повтор функционала псевдостраницы с бронированием