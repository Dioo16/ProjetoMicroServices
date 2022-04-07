"""
Funcoes da api de relatorio
"""
from query import transacoes_efetudas_e_verificadas


def transforma_em_relatorio(transacoes_verificadas):
    """
    Pega os dados e transforma em relatorio
    """
    relatorio_de_transacoes = []
    cont_vendas = 0
    for transacao in transacoes_verificadas:
        cont_vendas += 1
        status_transacao = 'Falha'
        motivo_status_transacao = ''

        if transacao['vendedor_validado'] is False:
            motivo_status_transacao += \
                '| O vendedor nAO foi validado em nosso sistema'

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
                'vendedor_do_produto': transacao['vendedor'],
                }}])
    return relatorio_de_transacoes


def get_relatorio():
    """
    Pega o relatório formatado e retorna
    """
    relatorio_transacoes = \
        transforma_em_relatorio(transacoes_efetudas_e_verificadas)

    return relatorio_transacoes
