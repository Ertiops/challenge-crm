from flask import Flask, render_template

from blueprints.admin.admin import admin

app = Flask(__name__, template_folder='./templates')

app.register_blueprint(admin, url_prefix="/admin")

@app.route("/")
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)