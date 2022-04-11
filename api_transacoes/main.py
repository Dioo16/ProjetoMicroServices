"""
high level support for doing this and that.
"""
from fastapi import FastAPI
import uvicorn
from query import dados_venda

app = FastAPI()


@app.get("/")
async def root():
    """
    funcao root
    """
    return {"message": "Hello Pessoal"}


@app.get("/transacoes")
async def get_produtos_vendidos():
    """
    endpoint get transacoes
    """
    return dados_venda

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
