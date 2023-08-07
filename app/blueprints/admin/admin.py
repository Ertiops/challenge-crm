from flask import Blueprint, render_template, redirect


admin = Blueprint("admin", __name__, template_folder="templates")

@admin.route("/")
def index():
    return "Hello World!"


@admin.route("/hello")
def hello():
    return "Hello World Again!"


@admin.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"


@admin.route("/hellohtml")
def hello_html():
    return render_template("admin/hello.html")