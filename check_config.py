#!/usr/bin/env python3
"""
Script para verificar configuração Railway
"""
import os

def main():
    print("🔍 Verificando configuração Railway...")
    print("-" * 50)
    
    # Verificar variáveis de ambiente importantes
    vars_importantes = [
        'DATABASE_URL',
        'PORT',
        'FLASK_APP',
        'PYTHONPATH'
    ]
    
    for var in vars_importantes:
        valor = os.environ.get(var, 'NÃO CONFIGURADA')
        print(f"{var}: {valor}")
    
    print("-" * 50)
    
    # Verificar se DATABASE_URL é PostgreSQL
    database_url = os.environ.get('DATABASE_URL', '')
    if 'postgresql://' in database_url:
        print("✅ PostgreSQL configurado corretamente")
    elif 'sqlite' in database_url:
        print("❌ PROBLEMA: Ainda usando SQLite")
        print("Configure DATABASE_URL no Railway com PostgreSQL")
    else:
        print("❌ PROBLEMA: DATABASE_URL não configurada")
    
    print("\n📝 Para configurar no Railway:")
    print("1. Vá ao painel Railway")
    print("2. Selecione seu projeto")  
    print("3. Clique em 'Variables'")
    print("4. Adicione:")
    print("   DATABASE_URL=postgresql://postgres:bRwPdxAQizHWgLahETaihcHCjbeTdvhZ@yamanote.proxy.rlwy.net:39387/railway")

if __name__ == "__main__":
    main()
