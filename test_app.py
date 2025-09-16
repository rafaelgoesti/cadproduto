#!/usr/bin/env python3
"""
Script para testar a aplicação localmente e verificar uploads
"""
import os
from app import criar_aplicacao

def testar_aplicacao_local():
    """Testa a aplicação localmente"""
    print("🧪 Testando aplicação localmente...")
    
    app = criar_aplicacao()
    
    with app.app_context():
        # Verificar configurações
        print(f"📊 Database URI: {app.config['SQLALCHEMY_DATABASE_URI'][:50]}...")
        print(f"📁 Pasta uploads: {app.config['PASTA_UPLOADS']}")
        print(f"📏 Tamanho máximo: {app.config['TAMANHO_MAXIMO']} bytes")
        
        # Verificar se pasta existe
        if os.path.exists(app.config['PASTA_UPLOADS']):
            print("✅ Pasta de uploads existe")
            files = os.listdir(app.config['PASTA_UPLOADS'])
            print(f"📋 Arquivos na pasta: {files}")
        else:
            print("❌ Pasta de uploads não existe")
    
    # Verificar se está em ambiente de produção
    if os.environ.get('PORT'):
        print("🚂 Detectado ambiente Railway (PORT definida)")
    else:
        print("💻 Ambiente local detectado")

def main():
    print("🔍 Diagnóstico da Aplicação")
    print("=" * 50)
    
    testar_aplicacao_local()
    
    print("\n📝 Próximos passos para corrigir imagens no Railway:")
    print("1. Faça commit das mudanças atuais")
    print("2. Push para o repositório")
    print("3. Railway fará redeploy automático")
    print("4. Teste novamente o upload de imagens")
    print("\n⚠️  Nota: No Railway, imagens são temporárias em /tmp")
    print("   Para produção real, considere usar um serviço como AWS S3")

if __name__ == "__main__":
    main()
