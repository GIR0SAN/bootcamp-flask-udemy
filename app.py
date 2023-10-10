from flask import Flask, render_template

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'

@app.route('/')
def page_home():
    return render_template("index.html")


@app.route('/produtos')
def page_produto():
    itens =[
        {'id':1, 'nome':'Celular', 'cod-barras': '125489563245', 'preço': 2450},
        {'id':2, 'nome': 'Notebook', 'cod-barras':'854123654896', 'preço':7680},
        {'id':3, 'nome': 'Teclado', 'cod-barras': '569841230015', 'preço':650},
        {'id':4, 'nome':'Monitor', 'cod-barras': '546333257800', 'preço':1250}
    ]
    return render_template("produtos.html", itens=itens)