from flask import Blueprint, render_template
LoginController = Blueprint("LoginController", __name__)

def index():
    return render_template("Auth/LoginPage.html")

def login():
    return "Logging in process..."