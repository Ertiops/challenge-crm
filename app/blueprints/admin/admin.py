from flask import Blueprint, render_template, redirect, request, url_for, flash
import uuid
import crud


admin = Blueprint("admin", __name__, template_folder="templates", static_folder='static')

# не тргоай пока
@admin.route("/", methods=['GET'])
def statistics():
    return render_template('statistics.html', title='Статистика')

@admin.route("/franchises", methods=['GET', 'POST'])
def franchises():
    franchises = crud.get_franchises_and_franchiser()
    if request.method == 'POST':
        id = uuid.uuid4()
        city = request.form['city'].capitalize()
        first_name = request.form['firstName'].capitalize()
        last_name = request.form['lastName'].capitalize()
        patronymic = request.form['patronymic'].capitalize()
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        role = 'франчайзер'
        franchise_id = id
        crud.add_franchise(id, city)
        crud.add_user(first_name, last_name, patronymic, email, phone, password, role, franchise_id)
        flash("Франшиза зарегистрирована успешно", category="success")
        return redirect(url_for('admin.franchises'))           
    return render_template('franchises.html', title='Франшизы', franchises=franchises)


@admin.route("/update_franchise", methods=['GET', 'POST'])
def update_franchise():
    franchise_id = request.args.get('franchise_id', None)

    franchise = crud.get_franchise_and_franchiser_by_id(franchise_id)
    print(franchise)
    if request.method == 'POST':
        if request.form['submit'] == 'update':

            print("Обновить")

        elif request.form['submit'] == 'delete':

            print("Удалить")            

        # if request.form
        # id = uuid.uuid4()
        # city = request.form['city'].capitalize()
        # first_name = request.form['firstName'].capitalize()
        # last_name = request.form['lastName'].capitalize()
        # patronymic = request.form['patronymic'].capitalize()
        # email = request.form['email']
        # phone = request.form['phone']
        # password = request.form['password']
        # role = 'франчайзер'
        # franchise_id = id
        # crud.add_franchise(id, city)
        # crud.add_user(first_name, last_name, patronymic, email, phone, password, role, franchise_id)
        # flash("Франшиза зарегистрирована успешно", category="success")
        return redirect(url_for('admin.update_franchise', franchise_id=franchise_id))        
    

    return render_template('update_franchise.html', title='Франшизы', franchise=franchise)

# добавка в бд бронирований



# отсылка данных в другой роутер и повтор функционала псевдостраницы с бронированием