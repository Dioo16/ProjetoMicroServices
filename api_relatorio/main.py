from funcoes import get_relatorio
from fastapi import FastAPI

import uvicorn

relatorio_transacoes = get_relatorio()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Pessoal"}

@app.get("/relatorio_transacoes_efetuadas")
async def get_produtos_vendidos():
    return relatorio_transacoes 

if __name__ == '__main__':
    uvicorn.run(app, port=8090, host='127.0.0.1')
