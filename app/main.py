from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
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
        print(email, '/n',password)
        result = crud.check_user(email, password)
        # if result is None:
        #     flash("Пользователь не зарегистрирован", category="error")


    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)