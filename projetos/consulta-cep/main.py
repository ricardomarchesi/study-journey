from fastapi import FastAPI, HTTPException
import requests
from fontes_cep import consultar_viacep, consultar_brasilapi
app = FastAPI()
@app.get("/")
def raiz():
    return {"mensagem": "Consulta de CEP. Use /cep/{cep}, ex: /cep/01310100"}


@app.get("/cep/{cep}")
def consultar_cep(cep: str):
    try:
        resultado = consultar_viacep(cep)
        if resultado:
            return resultado
    except requests.RequestException:
        pass  # ignora o erro e vai para proxima
    try:
        return consultar_brasilapi(cep)
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=404, detail=f"CEP {cep} não encontrado em nenhuma fonte.")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Nenhuma das duas APIs de CEP respondeu.")