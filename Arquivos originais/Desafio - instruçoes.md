# Desafio Lighthouse - https://academy.indicium.tech/path-player?courseid=desafio-lighthouse-dadosai\&unit=69b998463843651e6b08b858Unit

# Dados e IA

## Leia as instruções com atenção.





### Introdução

Este desafio tem como objetivo avaliar sua aptidão para atuar na jornada de dados da LH Nautical, testando sua capacidade analítica, domínio técnico, visão de negócio e pragmatismo. Buscamos entender seu raciocínio de ponta a ponta: desde o tratamento de dados brutos e modelagem SQL até a geração de insights estratégicos e aplicação de lógica preditiva.

Não avaliamos apenas o código, mas a sua habilidade de transformar dados desorganizados em soluções que gerem valor real para a operação. Responda a todas as etapas com base no contexto fictício da LH Nautical descrito abaixo, seguindo as orientações do Tech Lead, Gabriel Santos.



#### ⚠️ ATENÇÃO: LEIA ANTES DE COMEÇAR ⚠️

#### ESTE QUESTIONÁRIO TEM APENAS UMA TENTATIVA E NÃO SALVA RESPOSTAS AUTOMATICAMENTE. VOCÊ TEM 7 DIAS PARA PREPARAR SUAS RESPOSTAS E PODE ACESSAR ESTE ENUNCIADO QUANTAS VEZES QUISER DURANTE ESSE PERÍODO. NO ENTANTO, NÃO PREENCHA OS CAMPOS NEM CLIQUE EM "ENVIAR" SEM ESTAR COM TUDO FINALIZADO, POIS AS RESPOSTAS NÃO FICARÃO SALVAS. RECOMENDAMOS FORTEMENTE QUE VOCÊ PREPARE SUAS RESPOSTAS EM UM RASCUNHO E SÓ PREENCHA AQUI QUANDO ESTIVER PRONTO PARA ENVIAR. AO ENVIAR, NÃO SERÁ POSSÍVEL EDITAR OU TENTAR NOVAMENTE.

#### 

### Contexto Fictício

#### Sobre a Empresa

A LH Nautical é uma empresa líder no varejo de peças e acessórios para embarcações, operando em um modelo híbrido com loja física em Florianópolis e um e-commerce de alcance nacional. Recentemente, a empresa viveu um crescimento acelerado que trouxe grandes desafios operacionais e analíticos. 



#### 

#### O Cenário Atual

Atualmente, a LH Nautical enfrenta o que chamamos de "caos dos dados":Desorganização: O controle de estoque ainda é feito em planilhas manuais e "sujas". Desconexão: O banco de dados do e-commerce não conversa com o sistema financeiro. Decisões no "Feeling": A diretoria deseja implementar Inteligência Artificial para prever vendas, mas hoje tem dificuldade para consolidar o faturamento diário. 





#### Stakeholders Principais

Durante o desafio, você interagirá com as necessidades de três perfis centrais da empresa: 

Gabriel Santos (Tech Lead): O mentor técnico que valoriza a organização, a documentação e a clareza do raciocínio acima de códigos complexos. 

Marina Costa (Gerente de Negócios): Focada em resultados práticos, margens de lucro e performance de vendas. 

Sr. Almir (Fundador): Representa a visão old school; ele desconfia da "nuvem" e precisa ser convencido por dados sólidos e análises precisas. 

#### 

#### Seu Objetivo

Sua missão é atuar como o profissional de dados que transformará esse cenário. Você receberá bases brutas (como o catálogo de produtos e históricos de vendas) e deverá realizar desde a limpeza e modelagem (Engenharia de Dados e SQL) até a geração de insights preditivos e sistemas de recomendação (Ciência de Dados e IA).



Você acaba de receber um e-mail do Gabriel Santos, Tech Lead da LH Nautics. A empresa vai lançar uma campanha na semana que vem, mas os dados estão uma bagunça. Sua missão é limpar as bases, estruturar as tabelas e gerar os relatórios que a diretoria exige. Mas o Gabriel avisou: "Eu valorizo mais a organização e a explicação do que o código rodando sem eu entender nada."



#### Formato de Entrega:

As entregas foram separadas em frentes de:

1. EDA
2. Tratamento de dados
3. Análise de vendas
4. Análise de Clientes
5. Previsão de demandas
6. Sistemas de recomendações



E as solicitações estão organizadas nas questões desse desafio, você deve interpretar as perguntas e responder cada questão com base nas suas análises seguindos as premissas obrigatórias.

Ao final do desafio, você poderá enviar um material complementar com visualizações que ajudem a comunicar os principais resultados das análises realizadas no desafio.

O formato do envio final é livre (dashboard, notebook, PDF ou apresentação).

#### Sugestões de visuais:

Distribuição ou ranking de prejuízos por produto (questão 4)

Gráfico dos clientes com maior lucro acumulado (questão 5)

Vendas médias por dia da semana considerando dias sem venda (questão 6)

Explorações adicionais relevantes

O objetivo é demonstrar como você organiza e comunica insights a partir dos dados.



Link: 









Questões:



##### Questão 1 - EDA

Cenário



Antes de qualquer análise, modelagem ou tomada de decisão, é fundamental entender o que existe nos dados. O Sr. Almir quer uma resposta simples: “Posso confiar nesses dados para tomar decisões?”



Sua missão é realizar uma análise exploratória inicial do dataset *vendas\_2023\_2024.csv* e responder perguntas básicas, porém críticas, sobre volume, distribuição e qualidade dos dados.



**Premissas obrigatórias**

* Utilize apenas o dataset *vendas\_2023\_2024.csv*
* Não faça limpeza nem tratamento dos dados
* Apenas observe, agregue e descreva



**Tarefas:** 

**Parte 1** — Visão geral do dataset

Informe:

* Quantidade total de linhas
* Quantidade total de colunas
* Intervalo de datas analisado (data mínima e máxima)

**Parte 2** — Análise de valores numéricos

Para a coluna "total", calcule:

* Valor mínimo
* Valor máximo
* Valor médio

**Parte 3** — Interpretação

Responda de forma resumida:

Com base na análise exploratória realizada, escreva um breve diagnóstico sobre a confiabilidade do dataset *vendas\_2023\_2024.csv* para análises futuras.

Comente sobre:

* possíveis outliers em "total",
* qualidade dos dados (valores nulos ou inconsistentes),
* e se você considera que o dataset está pronto para análises ou se exigiria tratamento prévio.



###### Questão 1.1 - SQL

Código calculando:

* Quantidade total de linhas
* Quantidade total de colunas
* Intervalo de datas analisado (data mínima e máxima)
* Valor mínimo
* Valor máximo
* Valor médio



###### Questão 1.2 - Validação

* Qual é o valor máximo registrado na coluna "total"?



###### Questão 1.3 - Interpretação

Com base na análise exploratória realizada, escreva um breve diagnóstico sobre a confiabilidade do dataset vendas\_2023\_2024.csv para análises futuras. Comente sobre:

* Possíveis outliers em "total",
* Qualidade dos dados (valores nulos ou inconsistentes),
* e se você considera que o dataset está pronto para análises ou se exigiria tratamento prévio.



##### Questão 2 - Produtos

Cenário



Gabriel percebeu que seus dados estão desorganizados e sem um padrão definido e isso pode tornar o trabalho de análise mais trabalhoso. Precisamos melhorar isso utilizando o Python.



Sua missão é realizar uma normalização dos dados presentes no arquivo produtos\_raw.csv.



Premissas obrigatórias

* Utilize apenas o CSV *produtos\_raw.csv*
* Utilize **obrigatoriamente** **Python 3**



Tarefas: 

**Parte 1** — Padronize os nomes das categorias de produtos em: eletrônicos, propulsão e ancoragem.

**Parte 2** — Converta os valores para o tipo numérico.

**Parte 3** — Remova as duplicatas.



###### Questão 2.1 - Upload do código em Python da tarefa



###### Questão 2.2 - Validação

* Quantos produtos duplicados foram removidos?



##### Questão 3 - Custos de Importação

Cenário



Além dos dados de produtos, Gabriel percebeu também que o arquivo custos\_importacao.json tem todos os dados históricos dos preços de compra aninhados num único campo. Para facilitar a análise dessa informação no banco de dados é necessário melhorarmos isso.



Premissas obrigatórias

* Utilize apenas o JSON *custos\_importacao.json*
* Utilize **obrigatoriamente Python 3**



Tarefa: 

* Carregue o arquivo JSON e gere um novo arquivo CSV organizando-o de acordo com a definição na imagem Questão 3 figura 1.



###### Questão 3.1 - Upload do código em Python da tarefa



###### Questão 3.2 - Validação

* Quantas entradas de importação o CSV recebeu ao todo após a normalização?

##### 

##### Questão 4 - Dados Públicos

Cenário



O Sr. Almir identificou que alguns produtos podem ter sido vendidos abaixo do custo, possivelmente por erro operacional.



O problema é que:

* O sistema de vendas (*vendas\_2023\_2024.csv*) registra valores em **real BRL**
* O catálogo de fornecedores (*custos\_importacao.json*) registra custos unitários em **dollar USD**
* O câmbio varia diariamente



Até hoje, ninguém cruzou o custo em dólar do dia da venda com o valor de venda em reais.

Sua missão é abrir essa “caixa preta” financeira e identificar onde houve prejuízo real.



Premissas obrigatórias:

* O custo em USD é unitário
* O custo em BRL deve ser calculado usando o câmbio da data da venda
* A taxa de câmbio deve ser considerada a média da cotação de venda do dia (Banco Central)
* A receita total do produto considera todas as vendas (inclusive as sem prejuízo)
* **Ignore impostos e frete**



Tarefas:

**Parte 1** — Cálculo e modelagem

* Calcule o custo total em BRL por transação
* Identifique transações com prejuízo
* Agregue os dados por id\_produto, gerando:
1. Receita total (BRL)
2. Prejuízo total (BRL)
3. Percentual de perda (prejuízo\_total / receita\_total)

**Parte 2** — Análise visual

* Gere um gráfico que represente o prejuízo total por produto, considerando apenas produtos que tiveram prejuízo. (Inserir o gráfico no relatório/dashboard final)

Parte 3 —  Análise objetiva Responda objetivamente:

* Qual produto concentra o maior prejuízo absoluto?
* O produto com maior prejuízo absoluto também é o que possui a maior porcentagem de perda? (Sim ou Não)



###### Questão 4.1 - Código SQL

Código calculando:

* custo em R$ (custo\_usd \* taxa\_cambio\_data) - Se atentar ao cambio do dia
* agregação por id\_produto contendo:
1. Receita total (soma do valor de venda em reais),
2. Prejuízo total (soma apenas das perdas),
3. Percentual de perda (prejuízo\_total / receita\_total).



###### Questão 4.2 - Validação

* Qual é o id\_produto que apresentou a maior porcentagem de perda financeira relativa (maior % de prejuízo sobre sua receita) no período analisado?



###### Questão 4.3 - Interpretação

Explicação sobre o desenvolvimento:

* Qual data de câmbio você utilizou?
* Como definiu o prejuízo?
* Alguma suposição relevante?



##### Questão 5 - Análise de clientes

Cenário



A Diretoria da LH Nautical deseja identificar os clientes fieis. Diferente de quem compra muito uma única vez, o cliente fiel é o cliente que possui um gasto médio alto por transação e navega por diversas categorias da loja. O objetivo é mapear o que esses clientes de elite estão consumindo para replicar o comportamento em outros segmentos.





Premissas obrigatórias:

* Faturamento Total: Soma da coluna total por cliente.
* Frequência: Contagem total de transações (IDs de venda) por cliente.
* Ticket Médio: Faturamento Total / Frequência.
* Diversidade de Categorias: Quantidade de categorias distintas que o cliente comprou.
* Nota: É necessário limpar os nomes das categorias no *arquivo produtos\_raw.csv* (ex: consolidar "Ancorajen", "Encoragem" e "Ancoragem" como uma única categoria).
* Filtro de Elite: **Apenas clientes que compraram produtos de 3 ou mais categorias distintas devem ser considerados no ranking.**
* Desempate: **Em caso de empate no Ticket Médio, utilize o id\_cliente em ordem crescente**.



Tarefa:

1. Realize a limpeza das categorias de produtos para evitar duplicidade por erro de grafia.
2. Calcule o Ticket Médio e a Diversidade de Categorias para cada id\_cliente.
3. Filtre os 10 clientes com o maior Ticket Médio que atendam ao critério de diversidade (3+ categorias).
4. Para este grupo específico de 10 clientes, identifique qual categoria de produto concentra a maior quantidade total de itens comprados (sum(qtd)).



###### Questão 5.1 - Código SQL

Código calculando:

* O Ticket Médio e a Diversidade de categorias por cliente.
* A identificação e filtro dos 10 clientes "Fiéis" (maior Ticket Médio entre aqueles com diversidade >= 3 categorias).
* A categoria mais vendida (em quantidade total de itens) considerando apenas o histórico desses 10 clientes.





###### Questão 5.2 - Validação

* Considerando apenas as compras realizadas pelos Top 10 Clientes selecionados (Critério: Maior Ticket Médio com 3+ categorias): Qual foi a categoria de produtos mais vendida para eles (maior quantidade total de itens)?



###### Questão 5.3 - Explique:

1. Como você realizou a limpeza das categorias?
2. Qual lógica utilizou para filtrar os clientes com diversidade mínima?
3. Como garantiu que a contagem de itens refletisse apenas os Top 10?



##### Questão 6 - Dimensão de calendário

Cenário



O Sr. Almir quer saber: "Qual é o dia da semana (Segunda, Terça...) que temos a pior média de vendas?" para decidir se vale a pena fechar a loja nesses dias.



Um estagiário fez um GROUP BY dia\_semana direto na tabela de vendas e disse que a Terça-feira era ótima, com média de R$5.000,00. 



O problema: O estagiário esqueceu que em muitas terças-feiras a loja abriu mas vendeu zero. Como esses dias não existem na tabela de vendas (*vendas\_2023\_2024.csv*), eles foram ignorados no cálculo da média, inflando o resultado. Precisamos corrigir isso utilizando um calendário de datas (dimensão de datas)





Premissas obrigatórias:

* O período de análise deve considerar todas as datas entre a menor e a maior data\_venda presentes no arquivo.
* A loja esteve aberta em todos os dias do período (inclusive fins de semana).
* Dias sem registro na tabela de vendas devem ser considerados como valor\_venda = 0.
* “Vendas diárias” correspondem à soma de valor\_venda por dia.
* A média de vendas por dia da semana deve considerar todos os dias do calendário, inclusive os dias sem venda.
* O nome do dia da semana deve ser apresentado em português (Segunda-feira, Terça-feira, etc.).



Tarefa:

1. Construa uma dimensão de datas utilizando sql
2. Cruze a dimensão de datas com a tabela de vendas para análise (não esqueça de considerar os dias sem vendas).

###### 

###### Questão 6.1 - Código SQL

Código com:

* Desenvolvimento de um calendário com os dias da semana (em portugues)
* LEFT JOIN entre o calendário e a tabela de vendas
* agregação de vendas por dia (soma de valor\_venda),
* substituição de valores nulos por zero para dias sem vendas



###### Questão 6.2 - Validação

* Após considerar os dias zerados no cálculo: Qual é o Dia da Semana (ex: Domingo, Segunda...) que apresenta a menor média de vendas histórica, e qual é o valor dessa média arredondada para 2 casas decimais?



###### Questão 6.3 - Explique:

1. Por que é necessário utilizar uma tabela de datas (calendário) em vez de agrupar diretamente a tabela de vendas? 
2. O que aconteceria com a média de vendas se um dia da semana tivesse muitos dias sem nenhuma venda registrada?



##### Questão 7 - Previsão de demanda

Cenário



O Sr. Almir está furioso. No último verão, o estoque de "Coletes Salva-Vidas" acabou em 10 dias, e a empresa perdeu milhares de reais em vendas. Por outro lado, compraram "Âncoras" demais e elas estão enferrujando no galpão. Gabriel Santos, o Tech Lead, disse que não dá mais para confiar no "feeling". Ele quer um modelo preditivo que diga exatamente quantas unidades venderemos no próximo mês para ajustar as compras com fornecedores.





Premissas obrigatórias:

* O período de treino deve incluir dados até 31/12/2023.
* O período de teste deve ser todo o mês de Janeiro de 2024.
* A previsão deve ser feita em base diária.
* Não é permitido utilizar dados futuros no treino (data leakage).
* Considere apenas o produto: "Motor de Popa Yamaha Evo Dash 155HP"



Tarefa:

1. Utilize o dataset *vendas\_2023\_2024.csv*
2. Construa um modelo baseline simples, utilizando: Média móvel dos últimos 7 dias de vendas (considerando apenas dados anteriores à data prevista).
3. Gere a previsão diária de vendas para Janeiro de 2024.
4. Compare as previsões com os valores reais do período de teste utilizando a métrica: MAE — Mean Absolute Error
5. Responda objetivamente:

&#x20;    a. O baseline é adequado para esse produto?

&#x20;    b. Cite uma limitação desse método.



###### Questão 7.1 - Código em python

Adicione o código python usado para construção do modelo.



###### Questão 7.2 - Validação

* Utilizando seu modelo treinado, qual é a soma total da previsão de vendas (arredondada para número inteiro) para o 'Motor de Popa Yamaha Evo Dash 155HP' durante a primeira semana de Janeiro de 2024 (01/01 a 07/01)?



###### Questão 7.3 - Explique:

1. Como o baseline foi construído?
2. Como evitou data leakage?
3. Uma limitação do modelo proposto



##### Questão 8 - Sistema de recomendação

Cenário



A Marina percebeu que clientes que compram lanchas quase sempre esquecem de levar a defensa (proteção lateral). Ela quer implementar uma vitrine de "Quem comprou isso, também levou..." no site. 



Como não temos ferramentas de Big Data caras, você precisará criar um motor de recomendação, baseado na similaridade de compra dos clientes. 



Identificar qual produto deve ser recomendado junto ao item “GPS Garmin Vortex Maré Drift”, com base na similaridade de comportamento de compra dos clientes.





Tarefa:

1\. Crie uma matriz de interação Usuário × Produto obedecendo às regras abaixo:

&#x20;    a. Linhas: id\_cliente

&#x20;    b. Colunas: id\_produto

&#x20;    c. Valor da célula:

&#x20;    d. 1 se o cliente comprou ao menos uma vez o produto

&#x20;    e. 0 caso contrário

&#x20;    f. Ignore a quantidade comprada (presença/ ausência apenas)

2\. Cálculo de Similaridade entre Produtos

&#x20;    a. Calcule a Similaridade de Cosseno (Cosine Similarity) entre os vetores dos produtos

&#x20;    b. A similaridade deve ser calculada produto × produto, com base nos clientes que compraram cada item

3\. Ranking de Produtos Similares

&#x20;    a. Considere o produto “GPS Garmin Vortex Maré Drift” como item de referência

&#x20;    b. Gere um ranking com os 5 produtos mais similares a ele

&#x20;    c. Desconsidere o próprio GPS no ranking



###### Questão 8.1 - Código em python

Script em python que:

* Constrói a matriz usuário–item
* Calcula a similaridade de cosseno
* Gera o ranking de similaridade
* Bibliotecas permitidas:

&#x20;    - pandas

&#x20;    - numpy

&#x20;    - sklearn (opcional, para cosine similarity)



###### Questão 8.2 - Validação

* Qual é o id\_produto com MAIOR similaridade ao “GPS Garmin Vortex Maré Drift”?



###### Questão 8.3 - Explique:

1. Como a matriz foi construída?
2. O que significa a similaridade de cosseno nesse contexto?
3. Uma limitação desse método de recomendação.





**Pag. 23** - Relatório - arquivo



**Pag. 24** links (acredito que por GitHub)





