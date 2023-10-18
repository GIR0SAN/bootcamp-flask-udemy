from mercado import app
from flask import render_template, redirect, url_for, flash, session
from mercado.models import Item, User
from mercado.forms import CadastroForm, LoginForm
from mercado import db



@app.route('/')
def page_home():
    return render_template("index.html")

@app.route('/produtos')
def page_produtos():
    itens = Item.query.all()
    return render_template("produtos.html", itens=itens)

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
        #autenticação funcionou, redireciona a pagina para produtos.
        #session['user_id'] = usuario.id
        if usuario_logado and usuario_logado.converter_senha(senha_texto_claro=form.senha.data):
            flash('Login bem sucessido!')
            return redirect(url_for('page_produtos'))
    else:
        flash('Nome do usuário ou senhas incorretos')
    return render_template('login.html', form=form)