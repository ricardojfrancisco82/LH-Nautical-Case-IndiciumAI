![Python3](https://img.shields.io/static/v1?label=Python3\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=python\&logoColor=lightblue)
![SQLite](https://img.shields.io/static/v1?label=SQLite\&labelColor=003B57\&message=ok!%E2%9C%94\&style=plastic\&color=003B57\&logo=sqlite\&logoColor=80c6f1)
![BCB Olinda](https://img.shields.io/static/v1?label=BCB\&labelColor=003366\&message=Olinda%20API\&style=plastic\&color=FFD700\&logo=google-cloud\&logoColor=FFD700)
![Pandas](https://img.shields.io/static/v1?label=Pandas\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=pandas\&logoColor=lightblue)
![NumPy](https://img.shields.io/static/v1?label=NumPy\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=numpy\&logoColor=lightblue)


### Questão 6 - Dimensão de calendário

#### Cenário

O Sr. Almir quer saber: "Qual é o dia da semana (Segunda, Terça...) que temos a pior média de vendas?" para decidir se vale a pena fechar a loja nesses dias.

Um estagiário fez um GROUP BY dia_semana direto na tabela de vendas e disse que a Terça-feira era ótima, com média de R$5.000,00.

O problema: O estagiário esqueceu que em muitas terças-feiras a loja abriu mas vendeu zero. Como esses dias não existem na tabela de vendas (vendas_2023_2024.csv), eles foram ignorados no cálculo da média, inflando o resultado. Precisamos corrigir isso utilizando um calendário de datas (dimensão de datas)


#### Premissas obrigatórias:
* O período de análise deve considerar todas as datas entre a menor e a maior data_venda presentes no arquivo.
* A loja esteve aberta em todos os dias do período (inclusive fins de semana).
* Dias sem registro na tabela de vendas devem ser considerados como valor_venda = 0.
* “Vendas diárias” correspondem à soma de valor_venda por dia.
* A média de vendas por dia da semana deve considerar todos os dias do calendário, inclusive os dias sem venda.
* O nome do dia da semana deve ser apresentado em português (Segunda-feira, Terça-feira, etc.).

#### Tarefa:
* Construa uma dimensão de datas utilizando sql 
* Cruze a dimensão de datas com a tabela de vendas para análise (não esqueça de considerar os dias sem vendas).

#### Questão 6.1 - Código SQL
Código com:
* Desenvolvimento de um calendário com os dias da semana (em portugues)
* LEFT JOIN entre o calendário e a tabela de vendas
* agregação de vendas por dia (soma de valor_venda),
* substituição de valores nulos por zero para dias sem vendas

#### Questão 6.2 - Validação
Após considerar os dias zerados no cálculo: Qual é o Dia da Semana (ex: Domingo, Segunda...) que apresenta a menor média de vendas histórica, e qual é o valor dessa média arredondada para 2 casas decimais? *domingo*

#### Questão 6.3 - Explique:
Por que é necessário utilizar uma tabela de datas (calendário) em vez de agrupar diretamente a tabela de vendas?
*Primeiro ponto, a dimensão calendário é uma espécie de âncora balizadora das questões de data no banco de dados, evitando assim uma descentralização exageradas dessas mesmas datas, o que ocasionaria problemas e divergências entre registros e determinadas consultas onde o fator dia fosse preponderante. Outro ponto seriam os "dias vazios" em que não houvesse venda, ou registros, que poderiam gerar quebras em analises lineares, ou até mesmo interferir negativamente em medias.* 

O que aconteceria com a média de vendas se um dia da semana tivesse muitos dias sem nenhuma venda registrada?

*Haveria distorção da média, pois esses dias não seriam contabilizados como dias de venda.*

dia_semana_nome|media_vendas|
---------------+------------+
Sábado         |  3710540.55|
Sexta-feira    |  3715003.41|
Quinta-feira   |  3626232.44|
Quarta-feira   |  3535265.63|
Terça-feira    |  3627045.76|
Segunda-feira  |  3465137.71|
Domingo        |  3319503.57|

7 row(s) fetched.
