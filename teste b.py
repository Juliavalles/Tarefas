import requests

url = "http://127.0.0.1:5000/ler"

params = {"nome": "bloco-de-notas.txt"}

resposta = requests.get(url, params=params)

print(resposta.text)