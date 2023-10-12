from mercado import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=60), nullable=False, unique=True)
    senha = db.Column(db.String(length=60), nullable=False, unique=True)
    valor = db.Column(db.Integer, nullable=False, default=5000)
    itens = db.relationship('Item', backref='dono_user', lazy=True)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preço = db.Column(db.Integer, nullable=False)
    cod_barras = db.Column(db.String(length=12), nullable=False,unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False, unique=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f"Item {self.nome}"