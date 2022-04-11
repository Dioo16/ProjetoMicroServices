from query import estoque_produtos, precos_nao_existentes_no_estoque


def cria_dict_estoque():
    estoque_precos = {}
    estoque_precos['itens_do_estoque'] = [produto for produto in estoque_produtos]
        
    estoque_precos['precos_fora_do_padrao'] = [preco for preco in precos_nao_existentes_no_estoque]
        
        
    
    return estoque_precos