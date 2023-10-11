from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(length=30), nullable=False, unique=True)
    preço=db.Column(db.Integer, nullable=False)
    cod_barras=db.Column(db.String(length=12), nullable=False,unique=True)
    descricao=db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route('/')
def page_home():
    return render_template("index.html")


@app.route('/produtos')
def page_produtos():
    itens =[
        {'id':1, 'nome':'Celular', 'cod_barras': '125489563245', 'preço': 2450},
        {'id':2, 'nome': 'Notebook', 'cod_barras':'854123654896', 'preço':7680},
        {'id':3, 'nome': 'Teclado', 'cod_barras': '569841230015', 'preço':650},
        {'id':4, 'nome':'Monitor', 'cod_barras': '546333257800', 'preço':1250}
    ]
    return render_template("produtos.html", itens=itens)