from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "API funcionando"

#a) criando o arquivo
import os
from flask import request

@app.route('/criar', methods=['POST'])
def criar_arquivo():
    dados = request.json

    nome_arquivo = dados["nome"]
    conteudo = dados["conteudo"]

    caminho = os.path.join(os.getcwd(), nome_arquivo)

    with open(caminho, "w") as f:
        f.write(conteudo)

    return {"mensagem": "arquivo criado"}

# b) lendo o arquivo
@app.route('/ler', methods=['GET'])
def ler_arquivo():
    nome_arquivo = request.args.get("nome")

    with open(nome_arquivo, "r") as f:
        conteudo = f.read()

    return jsonify({
        "nome": nome_arquivo,
        "conteudo": conteudo
    })

# c) editando o arquivo que ja existe
@app.route('/editar', methods=['POST'])
def editar_arquivo():

    dados = request.json
    nome_arquivo = dados["nome"]
    novo_conteudo = dados["conteudo"]

    with open(nome_arquivo, "a") as f:
        f.write(novo_conteudo)

    return jsonify({"mensagem": "Arquivo editado"})

app.run(debug=True)