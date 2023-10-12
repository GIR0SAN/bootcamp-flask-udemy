from mercado import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preço = db.Column(db.Integer, nullable=False)
    cod_barras = db.Column(db.String(length=12), nullable=False,unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False, unique=True)


    def __repr__(self):
        return f"Item {self.nome}"