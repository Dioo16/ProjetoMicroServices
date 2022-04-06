from asyncio.windows_events import NULL
from query import lista_de_vendedores_validados, lista_de_produtos_existentes, lista_precos_fora_padrao
import requests
import json

def valida_vendedores_por_transacao(lista_de_compras_efetuadas):
    for compra_efetuada in lista_de_compras_efetuadas:
        if compra_efetuada['vendedor'] not in lista_de_vendedores_validados:
            compra_efetuada['vendedor_validado'] = False
        else:
            compra_efetuada['vendedor_validado'] = True
            
def valida_produto_por_transacao(lista_de_compras_efetuadas):
    for produto_comprado in lista_de_compras_efetuadas:
        if produto_comprado['produto'] not in lista_de_produtos_existentes:
            produto_comprado['produto_existente'] = False 
        else:
            produto_comprado['produto_existente'] = True
            
def verifica_preco_produto(lista_de_compras_efetuadas):
    for preco_produto_comprado in lista_de_compras_efetuadas:
        if preco_produto_comprado['preco'] == 0 or preco_produto_comprado['preco'] == NULL:
            preco_produto_comprado['verificacao_preco'] = 'preco inexistente ou igual a 0'
            
        elif preco_produto_comprado['preco'] in lista_precos_fora_padrao:
             preco_produto_comprado['verificacao_preco'] = 'preco fora dos padroes'
               
        elif preco_produto_comprado['preco'] > 5000:
             preco_produto_comprado['verificacao_preco'] = 'preco do produto excedente'
              
        else:
            preco_produto_comprado['verificacao_preco'] = 'preco normalizado'
                
        
def get_lista_de_transacoes_totais():
    lista_de_transacoes_totais = requests.get('http://127.0.0.1:8000/produtos_vendidos').json()
    return lista_de_transacoes_totais

def get_lista_de_transacoes_validadas():
    lista_de_transacoes_efetuadas = get_lista_de_transacoes_totais()
    valida_vendedores_por_transacao(lista_de_transacoes_efetuadas)
    valida_produto_por_transacao(lista_de_transacoes_efetuadas)
    verifica_preco_produto(lista_de_transacoes_efetuadas)
    return json.dumps(lista_de_transacoes_efetuadas)
    