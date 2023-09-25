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
    franchises = crud.get_franchises_and_franchiser()
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        is_email_unique = crud.is_email_unique(email)
        is_phone_unique = crud.is_phone_unique(email)

        if is_email_unique and is_phone_unique:
            id = uuid0.generate()
            city = request.form['city'].capitalize()
            first_name = request.form['firstName'].capitalize()
            last_name = request.form['lastName'].capitalize()
            patronymic = request.form['patronymic'].capitalize()
            password = request.form['password']
            role = 'франчайзер'
            franchise_id = id
            crud.add_franchise(id, city)
            crud.add_user(id, first_name, last_name, patronymic, email, phone, password, role, franchise_id)
            return redirect(url_for('admin.franchises'))  
        elif not is_email_unique:
            flash("Данный email уже зарегистрирован", category="danger") 
            return redirect(url_for('admin.franchises'))
        elif not is_phone_unique:
            flash("Данный номер уже зарегистрирован", category="danger") 
            return redirect(url_for('admin.franchises'))        

    return render_template('franchises.html', title='Франшизы', franchises=franchises)


@admin.route("/update_franchise", methods=['GET', 'POST'])
def update_franchise():
    franchise_id = request.args.get('franchise_id', None)
    franchise = crud.get_franchise_and_franchiser_by_id(franchise_id)
    # old_email = franchise.Users.email
    # old_phone = franchise.Users.phone

    if request.method == 'POST':
        if request.form['submit'] == 'update':
            email = request.form['email']
            phone = request.form['phone']
            unique_email = crud.is_email_unique_except_current(franchise_id, email)
            unique_phone = crud.is_phone_unique_except_current(franchise_id, phone)
            if unique_email and unique_phone:
                city = request.form['city'].capitalize() 
                first_name = request.form['firstName'].capitalize()
                last_name = request.form['lastName'].capitalize()
                patronymic = request.form['patronymic'].capitalize()
                result_franchiser = crud.update_franchiser(franchise_id, first_name, last_name, patronymic, email, phone)
                result_franchise = crud.update_franchise(franchise_id, city)
                if result_franchiser and result_franchise:
                    flash("Данные обновлены успешно", category="success") 
                    return redirect(url_for('admin.update_franchise', franchise_id=franchise_id))
            elif not unique_email:
                flash("Данный email уже зарегистрирован", category="danger") 
                return redirect(url_for('admin.update_franchise', franchise_id=franchise_id))
            elif not unique_phone:
                flash("Данный номер уже зарегистрирован", category="danger") 
                return redirect(url_for('admin.update_franchise', franchise_id=franchise_id))                             
            

        elif request.form['submit'] == 'delete':
            print("Удалить")            
            flash("Сися пися", category="danger")
            return redirect(url_for('admin.update_franchise', franchise_id=franchise_id))        
    

    return render_template('update_franchise.html', title='Франшизы', franchise=franchise)


@admin.route("/validate_password", methods=["POST"])
def validate():
    data = request.get_json()
    provided_password = data.get("password")
    is_valid = check_password_hash(current_user.password_hash, provided_password)
    return jsonify({"is_valid": is_valid})

# добавка в бд бронирований



# отсылка данных в другой роутер и повтор функционала псевдостраницы с бронированием