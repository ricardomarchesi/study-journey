from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

VIACEP_URL = "https://viacep.com.br/ws/{CEP}/json/"
BRASILAPI_URL = "https://brasilapi.com.br/api/cep/v1/{cep}"

def consultar_viacep(cep: str):
    resposta = requests.get(VIACEP_URL.format(CEP=cep), timeout=5)
    dados = resposta.json()
    if dados.get("erro"):
        return None
    return {
        "cep": dados["cep"],
        "logradouro": dados["logradouro"],
        "bairro": dados["bairro"],
        "cidade": dados["localidade"],
        "estado": dados["uf"],
        "fonte": "ViaCEP"
    }

def consultar_brasilapi(cep: str):
    resposta = requests.get(BRASILAPI_URL.format(cep=cep), timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    if dados.get("erro"):
        return None
    return {
        "cep": dados["cep"],
        "logradouro": dados["logradouro"],
        "bairro": dados["bairro"],
        "cidade": dados["localidade"],
        "estado": dados["uf"],
        "fonte": "BrasilAPI"
    }