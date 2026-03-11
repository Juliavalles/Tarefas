import requests

url = "http://127.0.0.1:5000/criar"

dados = {"nome": "bloco-de-notas.txt", "conteudo": "teste teste teste"}

resposta = requests.post(url, json=dados)

print(resposta.status_code)
print(resposta.text)