from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

class CadastroForm(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já cadastrado. Cadastre outro usuário")

    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email já cadastrado. Cadastre outro email")
        
    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha).first()
        if senha:
            raise ValidationError("Senha já cadastrada. Cadastre outra senha")

    usuario = StringField(label='Usuário', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label="Senha:", validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label="Confirme a senha:", validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label="Cadastrar")
