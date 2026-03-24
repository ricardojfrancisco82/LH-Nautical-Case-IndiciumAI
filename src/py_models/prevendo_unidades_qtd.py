# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:34:09 2026

@author: ricardojfrancisco
"""

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
from prophet import Prophet
#### Tarefa:

# Para fins de identificação do produto (code 54)
 # Considere apenas o produto: "Motor de Popa Yamaha Evo Dash 155HP".
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
serie_treino = base_treino.groupby('sale_date')['qtd'].sum().reset_index()
serie_treino.columns = ['ds', 'y']
model = Prophet(yearly_seasonality=True, daily_seasonality=False)
model.fit(serie_treino)

#3.Gere a previsão diária de vendas para Janeiro de 2024.
datas_jan = pd.date_range(start='2024-01-01', end='2024-01-31') #cria datas exatas do mes a ser previsto
future = pd.DataFrame({'ds': datas_jan}) #força a previsão a seguir o mês elecionado
forecast = model.predict(future)
previsao_jan = forecast.copy() # aqui já temos os 31 duias de Jan/24
   
#4.Compare as previsões com os valores reais do período de teste utilizando a métrica: MAE — Mean Absolute Error
vendas_reais_jan = base_prev.groupby('sale_date')['qtd'].sum().reindex(datas_jan, fill_value=0).reset_index()
vendas_reais_jan.columns = ['ds', 'y_real']
mae = mean_absolute_error(vendas_reais_jan['y_real'], previsao_jan['yhat'])

#5.Responda objetivamente:
    #a. O baseline é adequado para esse produto? Não, visto que que o MAE ficou muito longe da realidade
    #b. Cite uma limitação desse método? Esse modelo não é bom com varios dias com vendas zero.
    
# Criar uma tabela comparativa simples para leitura
comparativo_final = pd.DataFrame({
    'Data': datas_jan,
    'Venda_Real': vendas_reais_jan['y_real'],
    'Previsao_Prophet': previsao_jan['yhat'].round(2) # Arredondado para facilitar a leitura
})

# Calcular a diferença (erro) de cada dia
comparativo_final['Erro_Absoluto'] = abs(comparativo_final['Venda_Real'] - comparativo_final['Previsao_Prophet'])

comparativo_final.to_csv('data/processed/Q7_prev_und_qtd_prophet.csv')

