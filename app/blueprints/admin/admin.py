from flask import Blueprint, render_template, redirect


admin = Blueprint("admin", __name__, template_folder="templates", static_folder='static')

# не тргоай пока
@admin.route("/", methods=['GET'])
def statistics():
    return render_template('statistics.html', title='Статистика')

@admin.route("/franchises", methods=['GET', 'POST'])
def franchises():
    return render_template('franchises.html', title='Франшизы')


# добавка в бд бронирований



# отсылка данных в другой роутер и повтор функционала псевдостраницы с бронированием