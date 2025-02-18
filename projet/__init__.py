from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
<<<<<<< HEAD
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 's3cr3t'

app.config["SECRET_KEY"] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///imasouk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
=======
app = Flask(__name__)
from flask_login import LoginManager
app.config[ "SECRET_KEY" ] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///imasouk.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

>>>>>>> f62f24c (Premier commit avec les fichiers)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
<<<<<<< HEAD

=======
>>>>>>> f62f24c (Premier commit avec les fichiers)
from projet import routes
