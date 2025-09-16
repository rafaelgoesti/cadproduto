# 🚂 Deploy no Railway - Solução Definitiva

## ❌ Problema Atual
A aplicação está usando SQLite em vez de PostgreSQL no Railway, causando o erro:
```
sqlite3.OperationalError: no such table: produto
```

## ✅ Solução Passo a Passo

### 1. 🔧 Configurar Variável de Ambiente no Railway

**PASSO MAIS IMPORTANTE:**

1. Acesse: https://railway.app
2. Faça login e selecione seu projeto
3. Clique na aba **"Variables"** 
4. Clique em **"+ New Variable"**
5. Adicione exatamente:

```
Nome: DATABASE_URL
Valor: postgresql://postgres:bRwPdxAQizHWgLahETaihcHCjbeTdvhZ@yamanote.proxy.rlwy.net:39387/railway
```

6. Clique em **"Add"**

### 2. 🔄 Redeploy

Após adicionar a variável:
1. Vá para a aba **"Deployments"**
2. Clique em **"Deploy"** ou faça um novo commit

### 3. 📊 Verificar Logs

Monitore os logs durante o deploy:
- Deve aparecer: "✅ DATABASE_URL configurada corretamente"
- Deve aparecer: "✅ Migrações executadas com sucesso"
- Deve aparecer: "✅ Conexão com PostgreSQL estabelecida"

### 4. 🐛 Debug (se ainda não funcionar)

Execute o script de verificação localmente:
```bash
python check_config.py
```

## 📁 Arquivos Atualizados

- ✅ `Procfile` - Usa gunicorn + migrações automáticas
- ✅ `railway.toml` - Configuração completa Railway
- ✅ `start_railway.py` - Script de inicialização com verificações
- ✅ `check_config.py` - Script para debug
- ✅ `run.py` - Compatível com gunicorn

## 🔧 Comandos Railway

```bash
# Instalar Railway CLI (opcional)
npm install -g @railway/cli

# Fazer login
railway login

# Verificar variáveis
railway variables

# Ver logs em tempo real
railway logs
```

## 🚨 Pontos Críticos

1. **A variável DATABASE_URL DEVE estar configurada no Railway**
2. **NUNCA commite arquivos .env para o Git**
3. **O Railway deve usar PostgreSQL, não SQLite**

## ✅ Como Saber que Funcionou

Quando tudo estiver correto, você verá nos logs:
```
✅ DATABASE_URL configurada corretamente  
✅ Migrações executadas com sucesso
✅ Conexão com PostgreSQL estabelecida
✅ Aplicação pronta para iniciar!
```

## 📞 Se Ainda Não Funcionar

1. Verifique se a variável `DATABASE_URL` está realmente no Railway
2. Confirme que o valor é PostgreSQL (não SQLite)
3. Verifique os logs de deploy
4. Teste o script `check_config.py`
