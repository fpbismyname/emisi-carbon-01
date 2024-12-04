from flask import Flask
from app.routes.routes import routes

app = Flask(__name__, template_folder="app/views")
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run()