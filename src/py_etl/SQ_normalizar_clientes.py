# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:13:55 2026

@author: ricardojfrancisco
"""

import pandas as pd
import numpy as np
import re

# EDA dda lista de clientes da Nautical

clientes = pd.read_json('data/raw/clientes_crm.json')

# Normatizar: Município e UF

# Lista de UFs para validação
ufs = "AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO"

def limpar_localidade(texto):
    
    if pd.isna(texto): return None, None
    
    # 1. Padronização básica: tudo maiúsculo e remove espaços extras nas pontas
    texto = texto.upper().strip()
    
    # 2. Regex para encontrar a UF (2 letras maiúsculas isoladas)
    # (\b(?:{ufs})\b) -> Procura por uma das siglas de UF isolada
    # (.*) -> Captura o restante como sendo a cidade
    # Procuramos por siglas que estejam no início, fim ou após um separador
    match_uf = re.search(fr'\b({ufs})\b', texto)
    
    if match_uf:
        uf = match_uf.group(1)
        # Remove a UF e caracteres especiais comuns para isolar a cidade
        cidade = re.sub(fr'\b{uf}\b', '', texto)
        cidade = re.sub(r'[/\-_\,]', ' ', cidade).strip()
        # Remove espaços duplos resultantes da limpeza
        cidade = re.sub(r'\s+', ' ', cidade)
        return cidade, uf
    
    return texto, None

# Aplicando e criando novas colunas
clientes[['municipio_limpo', 'uf_limpa']] = clientes['location'].apply(lambda x: pd.Series(limpar_localidade(x)))

#Limpando colunas de e-mail
clientes['email'] = clientes['email'].str.replace('#', '@', regex=False)

# Excluindo a antiga location
clientes = clientes.drop('location', axis=1)

#Colocando os codigos de cliente p no incio da tabela
coluna_para_mover = clientes.pop('code')
clientes.insert(0, 'code', coluna_para_mover)

# renomear colunas para client_id, client_name, client_email, client_city, client_UF
clientes.columns = ['client_id', 'client_name', 'client_email', 'client_city', 'client_UF']

# checar duplicatas - não há, apenas nomes parecidos
clientes_duplicados = clientes.duplicated()

# =============================================================================
# Resultado da EDA da tabela Clientes
#* 49 clientes num toal em cinco colunas.
#* Exceto pela coluna de código de  cliente, todas as outras são strings.
#* Foram normalizados a Loacalização de cada cliente para um padrão logicamente melhor aplicável (separando municípiop de UF)
#* Foram renomeadas as colunasd para melhoir dientificação, de maneira análoga ao relizado em produtos

# Proposições de Melhorias
# * Criação de dimensões abordando o completo registro de endereço do cliente
# * Usar o CEP como uma dimensão para endereço, visto as necessidades de frete do e-commerce
# * Essas dimensionalidades podem ser udsadas em todas as tabelas com endereços (funcinarios, fornecedores, clientes, etc.)
# * Tal prática permite a redução do tamanho do banco de dados (ao inves de armazenar uma rua com 50 caracteres, 8 serrão o suficiente para identificá-la)
# * Manter  contatos telefônicos nos bancos de dados, até para auxiliar nos avisos de promoçõpes (via SMS/WhatsApp)  
# * Também pode-se fazer necessário um campo espec´[ifico para distritos/praias, tendo em vista que nem sempre são identificados prontamente pelo endereço do CEP]
# =============================================================================
