from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "parol"
UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new.db"
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "Login"