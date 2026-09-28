from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

VIACEP_URL = "https://viacep.com.br/ws/{CEP}/json/"

@app.get("/")
def raiz():
    return {"message": "API de Consulta de CEP. Use /cep/{CEP}, ex: /cep/01310100"}


@app.get("/cep/{cep}")
def consulta_cep(cep: str):
    url = VIACEP_URL.format(CEP=cep)
    resposta = requests.get(url, timeout=5)
    dados = resposta.json()

    if dados.get("erro"):
        raise HTTPException(status_code=404, detail=f"CEP {cep} não encontrado")

    return {
        "cep": dados.get("cep"),
        "logradouro": dados.get("logradouro"),
        "complemento": dados.get("complemento"),
        "bairro": dados.get("bairro"),
        "localidade": dados.get("localidade"),
        "uf": dados.get("uf")
    }