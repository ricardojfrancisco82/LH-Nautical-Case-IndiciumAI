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
from thefuzz import process, fuzz

produtos_original = pd.read_csv('data/raw/produtos_raw.csv')

# Verifica a estrutiura básica e valores da tabela
print(produtos_original.info())
print(produtos_original.isnull().sum())

#Categorizas precisa ser normalizado
total_categorias = produtos_original['actual_category'].nunique() # temos 39 categorias  
lista_categorias = (produtos_original['actual_category'].unique()) # retorna as ocorrÊncias

# Separa as ocorrências de erro para demostração futura
lista_contagem = produtos_original['actual_category'].value_counts()
lista_contagem.columns = ['categoria', 'quantidade']

#Normalização das categorias - todas em caixa baixa
produtos_original['actual_category'] = produtos_original['actual_category'].str.strip().str.lower()
produtos_original['actual_category'].unique()

#criando listas para uniformizar o cadastro, usando replace para uniformizar  as variantes

produtos_original['actual_category'] = produtos_original['actual_category'].replace(['eletronicos', 'e l e t r ô n i c o s', 'eletrunicos', 'eletronicoz', 'eletrônicos', 'eletroniscos'], 'eletrônicos') 
produtos_original['actual_category'] = produtos_original['actual_category'].replace(['propulsao', 'propulção', 'prop', 'propulssão', 'p r o p u l s ã o', 'propução', 'propulsão', 'propulçao', 'propulsam'], 'propulsão')
produtos_original['actual_category'] = produtos_original['actual_category'].replace(['ancoragem', 'encoragem','ancoraguem', 'ancorajm', 'a n c o r a g e m', 'ancorajem', 'encoragi', 'ancorajen', 'ancoragen'], 'ancoragem')

#Confirmando a normalização das categorias
produtos_original['actual_category'].unique()

#São dois campos numéricos (price e code), porém price precisa ser convertido
produtos_original['price'] = produtos_original['price'].str.replace('R$', '', regex=False).str.strip().astype(float)
produtos_original['price'].head()

#remover registros duplicados
total_produtos = produtos_original['name'].nunique() # temos 150 produtos, mas 157 registros

# Guardar os repetidos, pois é preciso verificar a necesidade de correção aqui, na tabela de vendas e na tabela de preços em dólar
produtos_duplicados = produtos_original[produtos_original.duplicated(keep=False)]

# Remover as duplicadas da original (coirreção aqui, pois aqui são valores totalmente duplicados)
produtos_limpa = produtos_original.drop_duplicates()

# Confirmar se há algum produto igual com nome levemente diferente, usando Lógica difusa
# primeiro tirar acentos e deixar tudo em minusculas, e uma lista para armazenas as duplicatas suspeitas
nome_limp = produtos_limpa['name'].str.lower().str.strip()
duplicatas_suspeitas = []

#Use um for percorrendo nossa serie para fazer a verificação
for nome in nome_limp:
    # Compara o 'nome' com todos os outros, exceto ele mesmo
    matches = process.extract(nome, nome_limp, scorer=fuzz.token_sort_ratio)
    # Filtra matches com similaridade alta, mas que não sejam idênticos
    for match, score, _ in matches:
        if 75 <= score < 100:
            duplicatas_suspeitas.append((nome, match, score))

# Transforma em DataFrame para analisar visualmente nomes silmilares
produtos_suspeitos = pd.DataFrame(duplicatas_suspeitas, columns=['Original', 'Suspeito', 'Score'])
   
#salvar as variáveis que precisarão ser demonstradas na analise, e fgerando a tabela de produtos limpa
exports = {
    'data/processed/Q2_produtos_duplicados.csv': produtos_duplicados,
    'data/processed/Q2_produtos_clean.csv': produtos_limpa,
    'data/processed/Q2_produtos_suspeitos.csv': produtos_suspeitos
    }

for nome_arquivo, data in exports.items():
    data.to_csv(nome_arquivo, index=False, sep=',', encoding='utf-8-sig')
    print(f"✅ Arquivo {nome_arquivo} exportado com sucesso!")

