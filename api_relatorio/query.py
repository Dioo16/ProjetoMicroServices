import requests

transacoes_efetudas_e_verificadas = requests.get('http://127.0.0.1:5000/transacoes_com_verificacoes').json()
