from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config['SECRET_KEY'] = '27b0ae2fc91246b6576e2303'
db.init_app(app)  
bcrypt = Bcrypt(app)

from mercado import routes