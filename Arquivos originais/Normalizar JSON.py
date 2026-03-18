# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:53:55 2026

@author: ricardojfrancisco
"""

import pandas as pd
import sqlite3
import json

# Carregar o arquivo
with open('custos_importacao.json', encoding='utf-8') as f:
    data = json.load(f)

# "Achata" o JSON: transforma a lista historic_data em linhas, 
# mantendo as informações do produto em cada linha.
df_flat = pd.json_normalize(
    data, 
    record_path=['historic_data'], 
    meta=['product_id', 'product_name', 'category']
)

# Conectar e salvar
conn = sqlite3.connect('C:/Users/ricardojfrancisco/Desktop/Desafio Indicium/DB/custos_importacao.db')
df_flat.to_sql('historico_precos', conn, if_exists='replace', index=False)
conn.close()