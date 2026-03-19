# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:01:12 2026

@author: ricardojfrancisco
"""

# Normalização da tabela produtos_raw: 
    #Parte 1 — Padronize os nomes das categorias de produtos em: eletrônicos, propulsão e ancoragem.
    #Parte 2 — Converta os valores para o tipo numérico.
    #Parte 3 — Remova as duplicatas.


import pandas as pd
import numpy as np

produtos_original = pd.read_csv(r'C:/Users/ricardojfrancisco/Desktop/Desafio Indicium/Arquivos originais/produtos_raw.csv')

# Verifica a estrutiura básica e valores da tabela
print(produtos_original.info())
print(produtos_original.isnull().sum())

#Categorizas precisa ser normalizado
total_categorias = produtos_original['actual_category'].nunique() # temos 39 categorias
    
lista_categorias = (produtos_original['actual_category'].unique()) # retorna as ocorrÊncias

lista_contagem = produtos_original['actual_category'].value_counts()
lista_contagem.columns = ['categoria', 'quantidade']

#Normalização das categorias - todas em caixa baixa
produtos_original['actual_category'] = produtos_original['actual_category'].str.strip().str.lower()
produtos_original['actual_category'].unique()

#criando listas para uniformizar o cadastro

produtos_original['actual_category'] = produtos_original['actual_category'].replace(['eletronicos', 'e l e t r ô n i c o s', 'eletrunicos', 'eletronicoz', 'eletrônicos', 'eletroniscos'], 'eletrônicos') 
produtos_original['actual_category'] = produtos_original['actual_category'].replace(['propulsao', 'propulção', 'prop', 'propulssão', 'p r o p u l s ã o', 'propução', 'propulsão', 'propulçao', 'propulsam'], 'propulsão')
produtos_original['actual_category'] = produtos_original['actual_category'].replace(['ancoragem', 'encoragem','ancoraguem', 'ancorajm', 'a n c o r a g e m', 'ancorajem', 'encoragi', 'ancorajen', 'ancoragen'], 'ancoragem')
produtos_original['actual_category'].unique()

#São dois campos numéricos (price e code), porém price precisa ser convertido
produtos_original['price'] = produtos_original['price'].str.replace('R$', '', regex=False).str.strip().astype(float)

produtos_original['price'].head()

#remover registros duplicados
total_produtos = produtos_original['name'].nunique() # temos 150 produtos, mas 157 registros
produtos_duplicados = produtos_original[produtos_original.duplicated(keep=False)] #rRepetidos
produtos_limpa = produtos_original.drop_duplicates()

#salvar as variáveis que precisarão ser demonstradas na analise, e fgerando a tabela de produtos limpa
exports = {
    'produtos_duplicados.csv': produtos_duplicados,
    'produtos_clean.csv': produtos_limpa
    }

for nome_arquivo, data in exports.items():
    data.to_csv(nome_arquivo, index=False, sep=',', encoding='utf-8-sig')
    print(f"✅ Arquivo {nome_arquivo} exportado com sucesso!")

