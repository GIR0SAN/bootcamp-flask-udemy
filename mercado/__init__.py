from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_bcrypt import Bcrypt
from flask_login import LoginManager  
#pip install Werkzeug==2.2.2(tem que instalar essa versão )

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config['SECRET_KEY'] = '27b0ae2fc91246b6576e2303'
db.init_app(app)  
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = "page_login"
login_manager.login_message = "Por favor, realize o login."
login_manager.login_message_category = "info"

from mercado import routes