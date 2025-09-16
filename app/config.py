import os
from dotenv import load_dotenv

load_dotenv()

class Configuracao:
    # Força o uso do PostgreSQL em produção
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or "sqlite:///bancoproduto.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração da pasta de uploads
    # No Railway/produção, usar /tmp para uploads temporários
    if os.environ.get('PORT') or os.environ.get('RAILWAY_ENVIRONMENT'):
        PASTA_UPLOADS = '/tmp/uploads'
    else:
        PASTA_UPLOADS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')

    TAMANHO_MAXIMO = 5 * 1024 * 1024 # Mb
