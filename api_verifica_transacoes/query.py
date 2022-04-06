import requests
import numpy as np

lista_de_vendedores_validados = [
    'alencar',
    'vierinha',
    'machado', 
    'Mamazinho',
    'Tiagao', 
    'Vitao', 
    'Diogao', 
    'Pedrão',
    'Luccao',
    'Lari',
    'Nina',
    'Zélia',
    'Raul',
]

lista_de_produtos_existentes = [
'bolsa',
'tenis',
'bola',
'chapéu',
'boné',
'jaqueta',
'violao',
'guitarra',
'meias',
'corda',
'barra',
'suplemento'
]

lista_precos_fora_padrao = [x for x in np.arange(0.01, 1, 0.01)]
