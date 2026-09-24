from fastapi import FastAPI, HTTPException
import requests
import time

app = FastAPI()

@app.get("/")
def raiz():
    return {"message": "Verificador de site. Use /status?url=https://exemplo.com"}

@app.get("/status")
def verificar_status(url: str):
    inicio = time.time()
    try:
        resposta = requests.get(url,  timeout=5)
        tempo_resposta_ms = round((time.time() - inicio) * 1000, 2)
        return {
            "url": url,
            "online": True,
            "status_code": resposta.status_code,
            "tempo_resposta_ms": tempo_resposta_ms
        }
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail=f"O site {url} demorou muito para resp onder (timeout).")
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail=f"Não foi possível conectar a {url}. O site pode estar fora do ar.")
    except requests.exceptions.missing_schema:
        raise HTTPException(status_code=400, detail=f"URL inválida: '{url}'. Inclua o protocolo, ex: https://{url}")
    