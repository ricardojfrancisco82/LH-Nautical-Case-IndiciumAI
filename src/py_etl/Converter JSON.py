# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:32:23 2026

@author: ricardojfrancisco
"""

import pandas as pd
import sqlite3
import json

# 1. Carregar o JSON
# Se o JSON for uma lista simples: [{"col1": 1}, {"col1": 2}]
df = pd.read_json('data/raw/clientes_crm.json')

# 2. Conectar ao banco que você criou no DBeaver
# Use o caminho completo do arquivo .db
conn = sqlite3.connect('data/processed/DB/clientes_crm.db')

# 3. Criar a tabela automaticamente
# O nome da tabela será o que você definir em 'name'
df.to_sql(name='tabela_vinda_do_json', con=conn, if_exists='replace', index=False)

conn.close()
print("Sucesso! A tabela foi criada.")