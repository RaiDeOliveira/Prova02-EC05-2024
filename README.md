# Aplicação Web

Essa é uma aplicação web simples geita com Flask, HTMX e TinyDB

## Instalação

1. Numa janela de terminal, clone o repositório com o seguinte comando:

```git clone git@github.com:RaiDeOliveira/Prova02-EC05-2024.git```

2. Digite os seguintes comandos para entrar na pasta raiz do repositório, criar um ambiente virutal e ativá-lo:

```cd Prova02-EC05-2024```

```python -m venv venv```

```venv\Scripts\activate```

3. Digite o seguinte comando para instalar as dependências necessárias para executar a aplicação web:

```pip install -r requirements.txt```

4. Digite o seguinte comando para executar a aplicação:

```py web-app/app.py```

> Uma URL aparecerá na janela do terminal. Clique nela com o botão esquerdo do mouse enquanto segura a tecla ctrl para abrir a aplicação web no seu navegador padrão.

## Funcionamento

A aplicação possui várias rotas, das quais as principais são:

- **/ping**: retorna uma mensagem de "pong" em formato json
- **/echo**: permite que o usuário digite uma mensagem e à retorna na tela em formato json
- **/das**: exibe um dashboard com logs das datas, horários e tipos de cada requisição feita através da aplicação web