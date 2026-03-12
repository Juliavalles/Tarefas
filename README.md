# API Flask – Manipulação de Arquivos

Este projeto consiste em uma API desenvolvida em Python utilizando o pacote Flask.
A API permite criar, ler e editar arquivos `.txt` através de requisições HTTP.

Também foram criados scripts de teste utilizando a biblioteca requests para acessar os endereços da API.

---

# Tecnologias utilizadas

* Python 3
* Flask
* Requests
* Biblioteca OS

---

# Como executar o projeto

## 1. Instalar as dependências

Instale as bibliotecas

`pip install flask`
`pip install requests`

## 2. Executar a API

Execute o arquivo principal da API:

`python Tarefa1.py`

Deixe o terminal aberto com a API em execução

A API será iniciada no endereço:

http://127.0.0.1:5000


## 3. Verificar se a API está funcionando

GET: 
http://127.0.0.1:5000

Resposta esperada:

API funcionando


# Scripts de teste

O projeto possui três arquivos de teste que utilizam a biblioteca `requests`.


## Teste A – Criar arquivo

Arquivo responsável por enviar uma requisição POST para o endereço `/criar` e gerar um novo arquivo `.txt`.

Execute em um terminal diferente daquele onde a API foi iniciada na etapa anterior:
`python "teste a.py"`

Resposta esperada: 
{
  "mensagem": "arquivo criado"
}

Certifique-se de que na pasta exista um arquivo .txt com o nome `bloco-de-notas.txt` com o conteudo "teste teste teste".


## Teste B – Ler arquivo

Realiza uma requisição GET para `/ler` e retorna o conteúdo do arquivo.


#### 1ª opção: Execute, também, em um terminal diferente do qual o principal foi executado:
`python "teste b.py"`

#### 2ª opção: http://127.0.0.1:5000/ler?nome=bloco-de-notas.txt


Resposta esperada: 
{
  "conteudo": "teste teste teste",
  "nome": "bloco-de-notas.txt"
}
 

## Teste C – Editar arquivo já existente

Envia uma requisição POST para `/editar` adicionando novo conteúdo ao arquivo existente.

Execute, também, em um terminal diferente do qual o principal foi executado:
`python "teste c.py"`

Resposta esperada: 
{'mensagem': 'Arquivo editado'}

Verifique que o arquivo `.txt` foi alterado e agora contém uma nova linha contendo "teste2 teste2 teste2"
