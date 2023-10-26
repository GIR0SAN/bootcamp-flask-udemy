from mercado import app
from flask import render_template, redirect, url_for, flash, request 
from mercado.models import Item, User
from mercado.forms import CadastroForm, LoginForm, CompraProdutoForm
from mercado import db
from flask_login import login_user, logout_user, login_required, current_user



@app.route('/')
def page_home():
    return render_template("index.html")

@app.route('/produtos', methods=["GET", "POST"])
@login_required
def page_produtos():
    compra_form = CompraProdutoForm()
    if request.method == 'POST':
        compra_produto = request.form.get('compra_produto')
        produto_obj = Item.query.filter_by(nome=compra_produto).first()
        if produto_obj:
            if current_user.compra_disponivel(produto_obj):
                produto_obj.dono = current_user.id
                current_user.valor -= produto_obj.preço
                db.session.commit()
                flash(f"Parabéns! Você comprou o produto {produto_obj.nome}", category="success")
            else:
                flash(f"Você não possui saldo suficiente para comprar o produto {produto_obj.nome}", category="danger")
        return redirect(url_for('page_produtos'))
    if request.method == "GET":
        itens = Item.query.filter_by(dono=None)
        return render_template("produtos.html", itens=itens, compra_form=compra_form)
    
@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario = User(
            usuario = form.usuario.data,
            email = form.email.data,
            senhacrip = form.senha1.data
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_produtos'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário {err}", category="danger")

    return render_template('cadastro.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario_logado = User.query.filter_by(usuario=form.usuario.data).first()
        if usuario_logado and usuario_logado.converte_senha(senha_texto_claro=form.senha.data):
            login_user(usuario_logado)
            flash(f'Usuario logado:{usuario_logado.usuario}', category='success')
            return redirect(url_for('page_produtos'))
        else:
            flash(f'Usuario ou senha estão incorretos', category='danger')
            
    return render_template('login.html', form=form)

@app.route('/logout')
def page_logout():
    logout_user()
    flash("Você fez o Logout", category="info")
    return redirect(url_for("page_home"))