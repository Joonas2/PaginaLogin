from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5b8ab54624efba22aeec46ff87c9b3c4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


database = SQLAlchemy(app)
from documentos import routes