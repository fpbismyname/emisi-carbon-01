from flask import Blueprint, render_template, request, jsonify
LoginController = Blueprint("LoginController", __name__)

# Make Methods Controller
def index():
    return render_template("Auth/LoginPage.html")

def login():
    return jsonify(request.form.to_dict())