from flask import Blueprint, render_template, request, redirect, url_for, current_app, send_from_directory
from .models import Produto
from .extencoes import db
import os
from werkzeug.utils import secure_filename

rotas_pricipal = Blueprint("principal", __name__)

@rotas_pricipal.route("/")
def pagina_inicial():
    produtos = Produto.query.order_by(Produto.criado_em.desc()).all()
    return render_template("index.html", produtos=produtos)

@rotas_pricipal.route("/static/upload/<filename>")
def upload_file(filename):
    return send_from_directory(current_app.config['PASTA_UPLOADS'], filename)

# Rota para Criar um Produto
@rotas_pricipal.route("/adicionar", methods=["post"])
def adicionar_produto():
    try:
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = request.form["preco"]
        categoria = request.form["categoria"]
        arquivo = request.files.get("imagem")

        nome_imagem = None
        if arquivo and arquivo.filename != "":
            # Garantir que a pasta de uploads existe
            pasta_uploads = current_app.config['PASTA_UPLOADS']
            os.makedirs(pasta_uploads, exist_ok=True)
            
            filename = secure_filename(arquivo.filename)
            caminho = os.path.join(pasta_uploads, filename)
            arquivo.save(caminho)
            nome_imagem = filename

        produto = Produto(nome=nome, descricao=descricao, preco=preco, categoria=categoria, nome_imagem=nome_imagem)
        db.session.add(produto)
        db.session.commit()

        return redirect(url_for("principal.pagina_inicial"))
    
    except Exception as e:
        current_app.logger.error(f"Erro ao adicionar produto: {e}")
        db.session.rollback()
        return f"Erro ao adicionar produto: {e}", 500

# Rota para Atualizar um Produto
@rotas_pricipal.route("/editar/<int:id_produto>", methods=["GET", "POST"])
def editar_produto(id_produto):
    produto = Produto.query.get_or_404(id_produto)

    if request.method == "POST":
        try:
            produto.nome = request.form["nome"]
            produto.descricao = request.form["descricao"]
            produto.preco = request.form["preco"]
            produto.categoria = request.form["categoria"]

            arquivo = request.files.get("imagem")
            if arquivo and arquivo.filename != "":
                # Garantir que a pasta de uploads existe
                pasta_uploads = current_app.config['PASTA_UPLOADS']
                os.makedirs(pasta_uploads, exist_ok=True)
                
                filename = secure_filename(arquivo.filename)
                caminho = os.path.join(pasta_uploads, filename)
                arquivo.save(caminho)
                produto.nome_imagem = filename

            db.session.commit()
            return redirect(url_for("principal.pagina_inicial"))
        
        except Exception as e:
            current_app.logger.error(f"Erro ao editar produto: {e}")
            db.session.rollback()
            return f"Erro ao editar produto: {e}", 500

    return render_template("editar.html", produto=produto)

# Rota para Excluir um produto
@rotas_pricipal.route("/excluir/<int:id_produto>", methods=["POST"])
def excluir_produto(id_produto):
    # Buscar o produto pelo id
    produto = Produto.query.get_or_404(id_produto)

    # Remover o produto do banco
    db.session.delete(produto)
    db.session.commit()

    return redirect(url_for("principal.pagina_inicial"))