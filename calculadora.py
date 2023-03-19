import numpy as np
import pandas as pd


comprimento = 100
largura = 20
altura = 10
peso_total = 50000
peso_carga = 10000
peso_combustivel = 5000
posicao_combustivel = 0.5
posicao_carga = 0.7

# Cálculo
peso_total = peso_total + peso_carga + peso_combustivel
centro_gravidade = ((peso_carga * posicao_carga) + (peso_combustivel * posicao_combustivel)) / peso_total
deslocamento = peso_total / 1000
centro_flutuacao = altura / 2

# Resultado
momento_estatico = (centro_gravidade - centro_flutuacao) * deslocamento
if momento_estatico > 0:
    print("Embarcação estável")
else:
    print("Embarcação instável")