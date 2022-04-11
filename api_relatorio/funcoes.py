"""
Funcoes da api de relatorio
"""
from query import transacoes, estoque_produtos_e_preco, mensagem_erro_estoque, mensagem_erro_transacoes
from asyncio.windows_events import NULL

def transforma_em_relatorio(transacoes_efetuadas):
    """
    Pega os dados e transforma em relatorio
    """
    valida_produto_por_transacao(transacoes_efetuadas)
    verifica_preco_produto(transacoes_efetuadas)
    
    relatorio_de_transacoes = []
    cont_vendas = 0
    
    if transacoes_efetuadas:
        for transacao in transacoes_efetuadas:
            cont_vendas += 1
            status_transacao = 'Falha'
            motivo_status_transacao = ''


            if transacao['produto_existente'] is False:
                motivo_status_transacao += \
                    '| O produto transacionado nao existe em nosso sistema'
                
            if transacao['verificacao_preco'] == 'preco inexistente ou igual a 0':
                motivo_status_transacao += \
                    '| O preco do produto é inexistente'

            if transacao['verificacao_preco'] == 'preco fora dos padroes':
                status_transacao = 'Verificacao manual pendente'
                motivo_status_transacao += '| Preco do produto anormal'

            if transacao['verificacao_preco'] == 'preco do produto excedente':
                motivo_status_transacao += '| Preco do produto excedente'
                
            if transacao['produto_existente'] == '':
                motivo_status_transacao = "validações  de estoque incompletas"
            
            if transacao['verificacao_preco'] == '':
                motivo_status_transacao = "validacoes de estoque incompletas"
            
            if motivo_status_transacao == '':
                status_transacao = 'Sucesso'
                motivo_status_transacao = \
                    'A transacao passou por todas verificacoes com sucesso'
            relatorio_de_transacoes.append([
                {'id_transacao': cont_vendas},
                {'status_transacao': status_transacao},
                {'motivo_status_transacao': motivo_status_transacao},
                {'detalhes_produto': {
                    'nome_produto': transacao['produto'],
                    'preco_produto': transacao['preco'],
                    'data_produto': transacao['data'],
                    'comprador_do_produto': transacao['comprador'],
                    }}])
    else:
        relatorio = {
            'status_relatorio' : 'Falha',
            'motivo:': 'Não houve conexão com nenhuma transacao',
            'Erro': mensagem_erro_transacoes
        }
        
        relatorio_de_transacoes = relatorio
        
        
    return relatorio_de_transacoes
        


"""
Funcoes referentes a validacao da transacao
"""

def valida_produto_por_transacao(dados_transacoes):
    """
    Valida se o produto é existente no estoque
    """
    if dados_transacoes:
        for produto_comprado in dados_transacoes:
            if estoque_produtos_e_preco:
            
                if produto_comprado['produto'] not in estoque_produtos_e_preco['itens_do_estoque']:
                    produto_comprado['produto_existente'] = False
                else:
                    produto_comprado['produto_existente'] = True
            else:
                produto_comprado['produto_existente'] = ''
         
def verifica_preco_produto(dados_transacoes):
    """
    Verifica se o preco do produto esta em um padrao aceitável
    """
    if dados_transacoes:
        if estoque_produtos_e_preco:
            for preco_produto in dados_transacoes:
                if preco_produto['preco'] == 0 or preco_produto['preco'] == NULL:
                    preco_produto['verificacao_preco'] = \
                        'preco inexistente ou igual a 0'
                elif preco_produto['preco'] in estoque_produtos_e_preco['precos_fora_do_padrao']:
                    preco_produto['verificacao_preco'] = 'preco anormal'
                    
                elif preco_produto['preco'] > 5000:
                    preco_produto['verificacao_preco'] = \
                        'preço do produto excedente'
                else:
                    preco_produto['verificacao_preco'] = \
                        'preço normalizado'
        else:
            for preco_produto in dados_transacoes:
                preco_produto['verificacao_preco'] = ''

def get_relatorio():
    relatorio = transforma_em_relatorio(transacoes)
    
    return relatorio