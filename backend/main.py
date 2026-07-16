# Importa a classe FastAPI da biblioteca fastapi
from fastapi import FastAPI

# Cria uma instância da aplicação FastAPI, que será usada para definir as rotas
app = FastAPI()

# Define a rota para o método HTTP GET no caminho raiz ("/")
@app.get("/")
def hello_world():
    # Retorna um dicionário que o FastAPI converterá automaticamente em JSON
    return {"mensagem": "Olá, mundo! 🌍"}
