"""
Da get na outra API, para pegar dados
"""
import requests
mensagem_erro_estoque = ''
mensagem_erro_transacoes = ''
try:
    estoque_produtos_e_preco = \
        requests.get('http://127.0.0.1:5000/estoque_e_precos'
                    ).json()
except:
    mensagem_erro_estoque = 'Error 404: Não houve validação com o estoque'
    estoque_produtos_e_preco = ''

try:
    transacoes = \
    requests.get('http://127.0.0.1:8000/transacoes'
                 ).json()
except:
    mensagem_erro_transacoes = 'Error 404: Não encontramos dados de transações'
    transacoes = ''