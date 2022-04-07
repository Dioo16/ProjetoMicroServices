"""
Arquivo main cria endpoint com as rotas
"""
from fastapi import FastAPI
import uvicorn
from funcoes import get_lista_de_transacoes_validadas


lista_de_transacoes_verificadas = get_lista_de_transacoes_validadas()

app = FastAPI()


@app.get("/transacoes_com_verificacoes")
async def root():
    """
    Endpoint das transacoes verificadas
    """
    return lista_de_transacoes_verificadas


if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='127.0.0.1')
