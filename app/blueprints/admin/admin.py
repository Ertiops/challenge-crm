from flask import Blueprint, render_template, redirect


admin = Blueprint("admin", __name__, template_folder="templates", static_folder='static')

# не тргоай пока
@admin.route("/", methods=['GET'])
def index():
    return render_template('sidebar.html')


# добавка в бд бронирований



# отсылка данных в другой роутер и повтор функционала псевдостраницы с бронированием