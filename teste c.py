import requests

url = "http://127.0.0.1:5000/editar"

dados = {"nome": "bloco-de-notas.txt", "conteudo": "\nteste2 teste2 teste2"}

resposta = requests.post(url, json=dados)

print(resposta.json())