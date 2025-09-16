from flask import Flask
from .config import Configuracao
from .extencoes import db, migrate
from .routes import rotas_pricipal
from .models import Produto  # Importar o modelo aqui
import os

def criar_aplicacao():
    app = Flask(__name__)
    app.config.from_object(Configuracao)

    db.init_app(app)
    migrate.init_app(app, db)

    # Criar pasta de uploads se não existir
    os.makedirs(app.config["PASTA_UPLOADS"], exist_ok=True)

    app.register_blueprint(rotas_pricipal)

    return app
