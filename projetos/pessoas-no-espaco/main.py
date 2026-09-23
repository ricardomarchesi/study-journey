from fastapi import FastAPI
import requests

app = FastAPI()

OPEN_NOTIFY_URL = "http://api.open-notify.org/astros.json"

@app.get("/")
def raiz():
    return {"message": "API de pessoas no espaço. Acesse /pessoas-no-espaco"}

@app.get("/pessoas-no-espaco")
def pessoas_no_espaco():
   
        resposta = requests.get(OPEN_NOTIFY_URL, timeout=5)
        dados = resposta.json()

        return {
            "quantidade": dados["number"],
            "astronautas": [pessoa["name"] for pessoa in dados["people"]]
        }

