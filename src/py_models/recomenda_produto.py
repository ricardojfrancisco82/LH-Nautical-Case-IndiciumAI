# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:18:53 2026

@author: ricardojfrancisco
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# importando os dados de trabalho
vendas_23_24 = pd.read_csv('data/processed/Q4_vendas_23_24_datas.csv')
lista_produtos =  pd.read_csv('data/processed/Q2_produtos_clean.csv')
alvo = lista_produtos[lista_produtos['name'].str.contains('GPS Garmin Vortex Maré Drift')]
    

# 1.Criar matriz de interação Ususário x Produto
    # Regras:
    # Linhas: vendas_23_24['id_client']
    # Colunas: vendas_23_24['id-product']
    # Valores das células:
        # 1 se cliente comprou;
        # 0 se cliente não comprou;
  
# Criando uma matriz Cliente x Produto
matriz_interacao = pd.crosstab(vendas_23_24['id_client'], vendas_23_24['id_product'])

# Convertendo os valores maiores que zero em True, pra depoios convertê-los em 1
matriz_binaria = (matriz_interacao > 0).astype(int) 

# 2.Cálculo de similaridade entre poodutos
    # Regras:Calcule a similaridade de cosseno (Cosine Similarity - scikitlearn)
    # Similaridade produto x produto, com base nas compras dos clientes

# Transpondo a matriz para termos os prosutos em linhas (é como cosine_similarity trabalha)
matriz_produtos = matriz_binaria.T

# Calculando a similaridade do cosseno
similaridade_matriz = cosine_similarity(matriz_produtos)

# Convertendo num dataframe para melhor visulaização do que foi feito
similaridade = pd.DataFrame(similaridade_matriz, index=matriz_produtos.index, columns=matriz_produtos.index)

# 3.Ranking de poodutos similares
    # Regras:
    # Considere o produto “GPS Garmin Vortex Maré Drift” como item de referência
    # Similaridade produto x produto, com base nas comprtas dos clientes
    
# Seta um alvo, cria um rank a partir dele, e exclui o proprio alvo, já que ele vai ser 1    
id_alvo = 27
rank_similares = similaridade[id_alvo].sort_values(ascending=False).drop(id_alvo)

rank_similares.to_csv('data/processed/Q8_rank_similares.csv')
