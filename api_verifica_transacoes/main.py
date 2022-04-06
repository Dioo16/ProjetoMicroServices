import json
from funcoes import get_lista_de_transacoes_validadas
from flask import Flask, request
import requests
import uvicorn

lista_de_transacoes_verificadas = get_lista_de_transacoes_validadas()

app = Flask('Transacoes')

@app.route("/transacoes_com_verificacoes", methods=["GET"])
async def root():
    return lista_de_transacoes_verificadas

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

app.run()
