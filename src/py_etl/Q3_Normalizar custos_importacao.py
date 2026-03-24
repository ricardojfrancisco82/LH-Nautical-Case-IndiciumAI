# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:53:55 2026

@author: ricardojfrancisco
"""

import pandas as pd
import json

# Carregar o arquivo
with open('data/raw/custos_importacao.json', encoding='utf-8') as f:
    data = json.load(f)

# "Achata" o JSON: transforma a lista historic_data em linhas, 
# mantendo as informações do produto em cada linha.
# Mantendo assim cada linha de registro a variação de preço em dolar de um produto
custos_importacao = pd.json_normalize(
    data, 
    record_path=['historic_data'], 
    meta=['product_id', 'product_name', 'category']
)

# Inspecionando nomes das colunas se condizem com o solicitado
# R: 'start_date', 'usd_price', 'product_id', 'product_name', 'category'
custos_importacao.columns

# REordenar colunas
custos_importacao = custos_importacao.reindex(
    columns=['product_id', 'product_name', 'category', 'start_date', 'usd_price']
)

#Confirmando a tipagem do dataframe
# R: 
#product_id       object
#product_name     object
#category         object
#start_date       object
#usd_price       float64

custos_importacao.dtypes

# Converter coluna para datetime, respeitando formato DD/MM/YY
custos_importacao['start_date'] = pd.to_datetime(custos_importacao['start_date'], format='%d/%m/%Y')

print(custos_importacao.dtypes)

# importar novo arquivo em CSV
custos_importacao.to_csv('data/processed/Q3_custos_importacao_normalizado.csv', index=False, sep=',', encoding='utf-8-sig')
