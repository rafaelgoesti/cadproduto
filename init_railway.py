#!/usr/bin/env python3
"""
Script de inicialização simplificado para Railway
Cria as tabelas diretamente sem usar Flask-Migrate CLI
"""
import os
import sys

def setup_database():
    """Configura o banco de dados criando as tabelas"""
    try:
        from app import criar_aplicacao
        from app.extencoes import db
        
        print("🔧 Configurando banco de dados...")
        
        # Criar aplicação
        app = criar_aplicacao()
        
        with app.app_context():
            # Verificar URL do banco
            database_url = app.config.get('SQLALCHEMY_DATABASE_URI', '')
            print(f"📊 Database URL: {database_url[:50]}...")
            
            if 'sqlite' in database_url:
                print("⚠️  AVISO: Usando SQLite")
            elif 'postgresql' in database_url:
                print("✅ Usando PostgreSQL")
            
            # Criar todas as tabelas
            db.create_all()
            print("✅ Tabelas criadas com sucesso!")
            
            return True
            
    except Exception as e:
        print(f"❌ Erro ao configurar banco: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 Iniciando configuração Railway...")
    
    # Verificar variáveis de ambiente
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL não configurada!")
        print("Configure no Railway: postgresql://postgres:bRwPdxAQizHWgLahETaihcHCjbeTdvhZ@yamanote.proxy.rlwy.net:39387/railway")
        sys.exit(1)
    
    # Configurar banco
    if not setup_database():
        sys.exit(1)
    
    print("✅ Configuração concluída!")

if __name__ == "__main__":
    main()
