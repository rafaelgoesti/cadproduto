#!/usr/bin/env python3
"""
Script de configuração para deploy no Railway
Este script prepara o projeto para deploy na plataforma Railway
"""

import os
import subprocess
import sys

def criar_procfile():
    """Cria o Procfile para o Railway"""
    procfile_content = "web: python run.py"
    
    with open("Procfile", "w") as f:
        f.write(procfile_content)
    print("✅ Procfile criado")

def criar_railway_toml():
    """Cria o arquivo railway.toml para configurações específicas do Railway"""
    railway_config = """[build]
builder = "NIXPACKS"

[deploy]
healthcheckPath = "/"
healthcheckTimeout = 100
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10

[env]
PYTHONPATH = "/app"
PORT = "5000"
"""
    
    with open("railway.toml", "w") as f:
        f.write(railway_config)
    print("✅ railway.toml criado")

def atualizar_run_py():
    """Atualiza o run.py para usar a porta do Railway"""
    run_py_content = """from app import criar_aplicacao
import os

app = criar_aplicacao()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
"""
    
    with open("run.py", "w") as f:
        f.write(run_py_content)
    print("✅ run.py atualizado para Railway")

def verificar_requirements():
    """Verifica se todos os pacotes necessários estão no requirements.txt"""
    required_packages = [
        "psycopg2-binary",
        "python-dotenv",
        "Flask",
        "Flask-SQLAlchemy",
        "gunicorn"  # Servidor WSGI para produção
    ]
    
    with open("requirements.txt", "r") as f:
        current_requirements = f.read()
    
    missing_packages = []
    for package in required_packages:
        if package not in current_requirements:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"⚠️  Pacotes faltando no requirements.txt: {', '.join(missing_packages)}")
        return False
    
    print("✅ Todos os pacotes necessários estão no requirements.txt")
    return True

def criar_runtime_txt():
    """Cria o runtime.txt especificando a versão do Python"""
    python_version = f"python-{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    
    with open("runtime.txt", "w") as f:
        f.write(python_version)
    print(f"✅ runtime.txt criado com {python_version}")

def main():
    """Função principal do setup"""
    print("🚀 Configurando projeto para Railway...")
    print("-" * 50)
    
    # Criar arquivos de configuração
    criar_procfile()
    criar_railway_toml()
    criar_runtime_txt()
    atualizar_run_py()
    
    # Verificar requirements
    verificar_requirements()
    
    print("-" * 50)
    print("✅ Configuração do Railway concluída!")
    print("\n📝 Próximos passos:")
    print("1. Faça commit das mudanças: git add . && git commit -m 'Configure Railway deployment'")
    print("2. Conecte seu repositório ao Railway")
    print("3. Configure as variáveis de ambiente no Railway:")
    print("   - DATABASE_URL (já configurado no .env)")
    print("4. Faça o deploy!")
    print("\n🌐 Sua aplicação estará disponível na URL fornecida pelo Railway")

if __name__ == "__main__":
    main()
