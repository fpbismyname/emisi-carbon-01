from flask import Blueprint
routes = Blueprint("routes", __name__)

# Register controller
import app.controllers.LoginController as LoginController

# Create Routes Here --
@routes.route("/", methods=['GET'])
def index():
    return LoginController.index()

@routes.route("/login", methods=['POST'])
def login():
    return LoginController.login()