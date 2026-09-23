from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

OPEN_NOTIFY_URL = "http://api.open-notify.org/astros.json"

@app.get("/")
def raiz():
    return {"mensagem": "API de pessoas no espaço. Acesse /pessoas-no-espaco"}

@app.get("/pessoas-no-espaco")
def pessoas_no_espaco():
    try:
        resposta = requests.get(OPEN_NOTIFY_URL, timeout=5)
        resposta.raise_for_status()
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Serviço indisponível. Tente novamente mais tarde."
        )

    dados = resposta.json()
    return {
        "quantidade": dados["number"],
        "astronautas": [pessoa["name"] for pessoa in dados["people"]]
    }
