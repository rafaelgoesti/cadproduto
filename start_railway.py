#!/usr/bin/env python3
"""
Script de inicialização para Railway
Verifica a conexão com PostgreSQL e executa migrações
"""
import os
import sys
from app import criar_aplicacao
from app.extencoes import db

def verificar_database_url():
    """Verifica se DATABASE_URL está configurada corretamente"""
    database_url = os.environ.get('DATABASE_URL')
    print(f"DATABASE_URL: {database_url}")
    
    if not database_url:
        print("❌ ERRO: DATABASE_URL não configurada!")
        print("Configure a variável DATABASE_URL no Railway com:")
        print("postgresql://postgres:bRwPdxAQizHWgLahETaihcHCjbeTdvhZ@yamanote.proxy.rlwy.net:39387/railway")
        sys.exit(1)
    
    if "sqlite" in database_url.lower():
        print("❌ ERRO: Ainda usando SQLite!")
        print("Configure DATABASE_URL com PostgreSQL no Railway")
        sys.exit(1)
    
    if database_url.startswith("postgres://"):
        new_url = database_url.replace("postgres://", "postgresql://", 1)
        os.environ['DATABASE_URL'] = new_url
        print(f"✅ URL convertida para: {new_url}")
    
    print("✅ DATABASE_URL configurada corretamente")

def testar_conexao():
    """Testa a conexão com o banco de dados"""
    try:
        app = criar_aplicacao()
        with app.app_context():
            # Tenta conectar ao banco
            db.engine.execute("SELECT 1")
            print("✅ Conexão com PostgreSQL estabelecida")
            return True
    except Exception as e:
        print(f"❌ Erro ao conectar com o banco: {e}")
        return False

def executar_migracoes():
    """Executa as migrações do banco"""
    try:
        import subprocess
        result = subprocess.run(['flask', 'db', 'upgrade'], 
                              capture_output=True, text=True, 
                              env=os.environ)
        
        if result.returncode == 0:
            print("✅ Migrações executadas com sucesso")
            print(result.stdout)
        else:
            print("❌ Erro ao executar migrações:")
            print(result.stderr)
            return False
        return True
    except Exception as e:
        print(f"❌ Erro ao executar migrações: {e}")
        return False

def main():
    print("🚀 Iniciando aplicação Railway...")
    print("-" * 50)
    
    # Verificar DATABASE_URL
    verificar_database_url()
    
    # Executar migrações
    if not executar_migracoes():
        sys.exit(1)
    
    # Testar conexão
    if not testar_conexao():
        sys.exit(1)
    
    print("-" * 50)
    print("✅ Aplicação pronta para iniciar!")

if __name__ == "__main__":
    main()
