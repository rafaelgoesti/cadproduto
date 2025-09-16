import os
from dotenv import load_dotenv

load_dotenv()

class Configuracao:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///bancoproduto.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PASTA_UPLOADS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')

    TAMANHO_MAXIMO = 5 * 1024 * 1024 # Mb
