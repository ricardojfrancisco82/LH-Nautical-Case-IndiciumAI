# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:53:13 2026

@author: ricardojfrancisco
"""
#### Premissas obrigatórias:
   
    # A previsão deve ser feita em base diária.
    # Não é permitido utilizar dados futuros no treino (data leakage).
    #Considere apenas o produto: "Motor de Popa Yamaha Evo Dash 155HP"

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error

#### Tarefa:

# Para fins de identificação do produto (code 54)
lista_produtos =  pd.read_csv('data/processed/Q2_produtos_clean.csv')
alvo = lista_produtos[lista_produtos['name'].str.contains('Motor de Popa Yamaha Evo Dash 155HP')]
id_alvo = 54
    
#1.Utilize o dataset vendas_2023_2024.csv
# importando os dados de trabalho
    # Premissas obrigatórias
    # Garantindo que a coluna ['sale_date'] seja interpretada como data
    # O período de treino deve incluir dados até 31/12/2023.
    # O período de teste deve ser todo o mês de Janeiro de 2024.
vendas_23_24 = pd.read_csv('data/processed/Q4_vendas_23_24_datas.csv')
vendas_23_24['sale_date'] = pd.to_datetime(vendas_23_24['sale_date'])
vendas_motor = vendas_23_24[vendas_23_24['id_product'] == id_alvo].copy()
base_treino =vendas_motor[vendas_motor['sale_date'].dt.year == 2023]
base_prev = vendas_motor[(vendas_motor['sale_date'] .dt.year == 2024) & (vendas_motor['sale_date'] .dt.month == 1)]

#2.Construa um modelo baseline simples, utilizando: 
    # Média móvel dos últimos 7 dias de vendas (considerando apenas dados anteriores à data prevista)
    # A previsão deve ser feita em base diária.
    # Não é permitido utilizar dados futuros no treino (data leakage).
    # Considere apenas o produto: "Motor de Popa Yamaha Evo Dash 155HP".
vendas_diarias = vendas_motor.groupby('sale_date')['qtd'].sum().reset_index()
calendario = pd.date_range(start='2023-01-01', end='2024-01-31')
df_baseline = pd.DataFrame({'sale_date': calendario}) #cria um calendario, evita pular dias sem venda
df_baseline = pd.merge(df_baseline, vendas_diarias, on='sale_date', how='left').fillna(0) #tras as vendas no calendário, preenche com zero dias sem venda

#3.Gere a previsão diária de vendas para Janeiro de 2024.
df_baseline['previsao'] = df_baseline['qtd'].shift(1).rolling(window=7).mean().fillna(0) #calcula média móvel de 7 dias (sem data leakage)
janeiro_2024 = df_baseline[(df_baseline['sale_date'].dt.year == 2024) & (df_baseline['sale_date'].dt.month == 1)] #seppara os meses de janeiro

#4.Compare as previsões com os valores reais do período de teste utilizando a métrica: MAE — Mean Absolute Error
comparativo = janeiro_2024[['sale_date', 'qtd', 'previsao']].copy()
comparativo.columns = ['Data', 'Venda_Real', 'Previsao_MM7']
comparativo['Erro_Absoluto'] = abs(comparativo['Venda_Real'] - comparativo['Previsao_MM7'])
mae_final = mean_absolute_error(comparativo['Venda_Real'], comparativo['Previsao_MM7'])

comparativo.to_csv('data/processed/Q7_prev_und.csv')

print(comparativo.iloc[0:6])
