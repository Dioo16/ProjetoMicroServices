"""
arquivo pega dados para verificacao
"""
import numpy as np


estoque_produtos = [
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
    'suplemento',
    ]

precos_nao_existentes_no_estoque = list(np.arange(0.01, 1, 0.01))
