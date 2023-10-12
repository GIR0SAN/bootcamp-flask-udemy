from mercado import app
from flask import render_template 
from mercado.models import Item
from mercado.forms import CadastroForms

@app.route('/')
def page_home():
    return render_template("index.html")

@app.route('/produtos')
def page_produtos():
    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)

@app.route('/cadastro')
def page_cadastro():
    form = CadastroForms()
    return render_template('cadastro.html', form=form)