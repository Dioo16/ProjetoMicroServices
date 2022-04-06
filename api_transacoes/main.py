from fastapi import FastAPI
import uvicorn
from query import dados_venda
import json
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Pessoal"}

@app.get("/produtos_vendidos")
async def get_produtos_vendidos():
    return dados_venda 

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
