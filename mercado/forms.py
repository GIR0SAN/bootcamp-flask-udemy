from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class CadastroForms(FlaskForm):
    usuario = StringField(label='Usuário')
    email = StringField(label='E-mail:')
    senha1 = PasswordField(label="Senha:")
    senha2 = PasswordField(label="Confirme a senha:")
    submit = SubmitField(label="Cadastrar")
