"""
Arquivo main cria endpoint com as rotas
"""
from fastapi import FastAPI
import uvicorn
from funcoes import cria_dict_estoque


app = FastAPI()


@app.get("/estoque_e_precos")
async def root():
    """
    Endpoint do estoque verificado
    """
    
    estoque_e_precos = cria_dict_estoque()
    return estoque_e_precos


if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='127.0.0.1')
