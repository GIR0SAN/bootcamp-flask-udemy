from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preço = db.Column(db.Integer, nullable=False)
    cod_barras = db.Column(db.String(length=12), nullable=False,unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False, unique=True)


    def __repr__(self):
        return f"Item {self.nome}"
    

@app.route('/')
def page_home():
    return render_template("index.html")


@app.route('/produtos')
def page_produtos():
    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)