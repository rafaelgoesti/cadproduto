from app import criar_aplicacao
from app.extencoes import db
import os

app = criar_aplicacao()

# Inicializar banco na primeira execução
with app.app_context():
    try:
        # Tentar criar as tabelas se não existirem
        db.create_all()
        print("✅ Tabelas do banco criadas/verificadas")
    except Exception as e:
        print(f"⚠️  Erro ao inicializar banco: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(debug=debug, host="0.0.0.0", port=port)