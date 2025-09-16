from .extencoes import db
from datetime import datetime

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    nome_imagem = db.Column(db.String(255), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    