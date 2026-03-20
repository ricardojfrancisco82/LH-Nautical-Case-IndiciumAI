![SQLite](https://img.shields.io/static/v1?label=SQLite\&labelColor=003B57\&message=ok!%E2%9C%94\&style=plastic\&color=003B57\&logo=sqlite\&logoColor=80c6f1)


### Questão 5 - Análise de clientes



#### Cenário


A Diretoria da LH Nautical deseja identificar os clientes fieis. Diferente de quem compra muito uma única vez, o cliente fiel é o cliente que possui um gasto médio alto por transação e navega por diversas categorias da loja. O objetivo é mapear o que esses clientes de elite estão consumindo para replicar o comportamento em outros segmentos.

#### Premissas obrigatórias:
* Faturamento Total: Soma da coluna total por cliente.
* Frequência: Contagem total de transações (IDs de venda) por cliente.
* Ticket Médio: Faturamento Total / Frequência.
* Diversidade de Categorias: Quantidade de categorias distintas que o cliente comprou.
* Filtro de Elite: *Apenas clientes que compraram produtos de 3 ou mais categorias distintas devem ser considerados no ranking.*
* Desempate: *Em caso de empate no Ticket Médio, utilize o _id_cliente_ em ordem crescente.*

#### Tarefas:

1. Calcule o Ticket Médio e a Diversidade de Categorias para cada id_cliente.
2. Filtre os 10 clientes com o maior Ticket Médio que atendam ao critério de diversidade (3+ categorias).
3. Para este grupo específico de 10 clientes, identifique qual categoria de produto concentra a maior quantidade total de itens comprados (sum(qtd)). *Propulsão, com 6030 *

#### Questão 5.1 - Código SQL
Código calculando:
* O Ticket Médio e a Diversidade de categorias por cliente.
* A identificação e filtro dos 10 clientes "Fiéis" (maior Ticket Médio entre aqueles com diversidade >= 3 categorias).
* A categoria mais vendida (em quantidade total de itens) considerando apenas o histórico desses 10 clientes.


#### Questão 5.2 - Validação
Considerando apenas as compras realizadas pelos Top 10 Clientes selecionados (Critério: Maior Ticket Médio com 3+ categorias): 
* Qual foi a categoria de produtos mais vendida para eles (maior quantidade total de itens)? *Propulsão, com 6030*

#### Questão 5.3 - Explique:
1. Como você realizou a limpeza das categorias?
*Havia sido feito em estágios anteriores com Python em sua maioria. A maior parte dos problemas encontrados foram por falta de normalização dos dados, bem como de uma padronização de formatos. Inicialmente, haviam mais de vinte categorias nos dados originais, porém eram repetições com erros de digitação e falta de acentuação das três únicas categorias existentes.
Inclusive, ao analisar as categorias em duas tabelas diferentes, pode-se observar que em produtos ela não estava normalizada, mas estava em custos importação. 
Outro ponto a observar, com essa observação, é sugerir a retirada da categoria na tabela de custos importação, podendo ser criada uma VIEW especificamente pra isso, o que melhoraria a velocidade do banco de dados.*
2. Qual lógica utilizou para filtrar os clientes com diversidade mínima?
*Como são poucas categorias, usei um **COUNT(DISTINCT)** olhando por campo **actual_category** dos produtos comprados pelo **id_client**, porém, exatamente por serem poucas, na segunda query que atua  como filtro na primeira, em GROUP BY foram colocados dois critérios de agrupamento (primeiro pelo ticket médio, do maior ao menor; e segundo pelo id do cliente, do menor ao maior, já que se supõe que quanto menor o id do cliente, mais antigo ele é)*
3. Como garantiu que a contagem de itens refletisse apenas os Top 10? 
*usando LIMIT 10*
