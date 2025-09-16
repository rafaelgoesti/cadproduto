# Deploy no Railway - Guia Completo

## Configuração do Banco PostgreSQL

O erro que você está enfrentando indica que a aplicação está usando SQLite em vez do PostgreSQL no Railway. Siga estes passos para corrigir:

### 1. Configurar Variáveis de Ambiente no Railway

1. Acesse o painel do Railway (https://railway.app)
2. Selecione seu projeto
3. Vá para a aba **"Variables"**
4. Adicione a seguinte variável:

```
DATABASE_URL=postgresql://postgres:bRwPdxAQizHWgLahETaihcHCjbeTdvhZ@yamanote.proxy.rlwy.net:39387/railway
```

### 2. Verificar se o PostgreSQL está ativo

1. No painel Railway, verifique se você tem um serviço PostgreSQL ativo
2. Se não tiver, adicione um novo serviço PostgreSQL
3. Copie a DATABASE_URL fornecida pelo Railway

### 3. Comandos que foram atualizados

#### Procfile
```
web: flask db upgrade && python run.py
```
- Agora executa as migrações automaticamente antes de iniciar

#### Config.py
- Adicionada conversão automática de `postgres://` para `postgresql://`
- Força o uso do PostgreSQL em produção

### 4. Redeploy da Aplicação

Após configurar as variáveis:
1. Faça commit das mudanças:
```bash
git add .
git commit -m "Fix PostgreSQL configuration for Railway"
git push
```

2. O Railway fará redeploy automaticamente

### 5. Verificação

Após o deploy, a aplicação deve:
- Executar `flask db upgrade` (cria as tabelas no PostgreSQL)
- Iniciar o servidor na porta configurada
- Usar PostgreSQL em vez de SQLite

### 6. Debug (se ainda houver problemas)

Verifique os logs no Railway:
- Procure por erros de conexão com banco
- Confirme se `DATABASE_URL` está sendo carregada
- Verifique se as migrações foram executadas

### 7. Estrutura de Arquivos Criados/Atualizados

- ✅ `Procfile` - Atualizado com migração automática
- ✅ `railway.toml` - Configuração do Railway
- ✅ `app/config.py` - Configuração do banco atualizada
- ✅ `requirements.txt` - Todas as dependências incluídas
- ✅ `.env.railway` - Exemplo de variáveis de ambiente

## Próximos Passos

1. Configure a variável `DATABASE_URL` no Railway
2. Faça push das mudanças
3. Aguarde o redeploy
4. Teste a aplicação na URL fornecida pelo Railway

A aplicação deve funcionar corretamente com PostgreSQL!
