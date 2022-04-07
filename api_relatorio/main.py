"""
Main que tem a funcao de retornar o relatorio das transacoes
"""
import uvicorn
from fastapi import FastAPI
from funcoes import get_relatorio


relatorio_transacoes = get_relatorio()

app = FastAPI()


@app.get("/relatorio_transacoes_efetuadas")
async def get_produtos_vendidos():
    """
    cria endpoit do relatorio das transacoes e retorna dados
    """
    return relatorio_transacoes


if __name__ == '__main__':
    uvicorn.run(app, port=8090, host='127.0.0.1')
