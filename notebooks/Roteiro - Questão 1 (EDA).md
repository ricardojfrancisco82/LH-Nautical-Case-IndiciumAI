![SQLite](https://img.shields.io/static/v1?label=SQLite&labelColor=003B57&message=ok!%E2%9C%94&style=plastic&color=003B57&logo=sqlite&logoColor=80c6f1)


##### Questão 1 - EDA

Cenário



Antes de qualquer análise, modelagem ou tomada de decisão, é fundamental entender o que existe nos dados. O Sr. Almir quer uma resposta simples: *“Posso confiar nesses dados para tomar decisões?”*

Sua missão é realizar uma análise exploratória inicial do *dataset* ***vendas\_2023\_2024.csv*** e responder perguntas básicas, porém críticas, sobre volume, distribuição e qualidade dos dados.



**Premissas obrigatórias**

* Utilize apenas o *dataset* ***vendas\_2023\_2024.csv***
* Não faça limpeza nem tratamento dos dados
* Apenas observe, agregue e descreva



**Tarefas:**

**Parte 1** — Visão geral do *dataset*

Informe:

* Quantidade total de linhas: *9895 linhas*
* Quantidade total de colunas: *6 colunas* 

> SELECT COUNT(*) FROM vendas_2023_2024 

COUNT(*)|
--------+
    9895|

1 row(s) fetched.


*PRAGMA table\_info('vendas\_2023\_2024')*

cid|name      |type       |notnull|dflt\_value|pk|

\---|----------|-----------|-------|----------|--|

&#x20; 0|id        |INTEGER    |      0|          | 0|

&#x20; 1|id\_client |INTEGER    |      0|          | 0|

&#x20; 2|id\_product|INTEGER    |      0|          | 0|

&#x20; 3|qtd       |INTEGER    |      0|          | 0|

&#x20; 4|total     |REAL       |      0|          | 0|

&#x20; 5|sale\_date |VARCHAR(50)|      0|          | 0|



* Intervalo de datas analisado (data mínima e máxima): *Os dados compreendem ao biênio 2023/2024, iniciando-se em 01/01/2023 e encerrando em 31/12/2024.*

**Parte 2** — Análise de valores numéricos

Para a coluna ***"total"***, calcule:

* Valor mínimo: *R$ 294,50*
* Valor máximo: *R$ 2.222.973,00*
* Valor médio: *R$ 263.797,83*

**Parte 3** — Interpretação

Responda de forma resumida:

Com base na análise exploratória realizada, escreva um breve diagnóstico sobre a confiabilidade do *dataset* ***vendas\_2023\_2024.csv*** para análises futuras.

Comente sobre:

* possíveis outliers em "total",
* qualidade dos dados (valores nulos ou inconsistentes),
* e se você considera que o *dataset* está pronto para análises ou se exigiria tratamento prévio.



###### Questão 1.1 - SQL - respondida em script

Código calculando:

* Quantidade total de linhas: *9895 linhas*
* Quantidade total de colunas:  *6 colunas* 
* Intervalo de datas analisado (data mínima e máxima):
* Valor mínimo: *R$ 294,50*
* Valor máximo: *R$ 2.222.973,00*
* Valor médio: *R$ 263.797,83*



###### Questão 1.2 - Validação  - respondida em script

* Qual é o valor máximo registrado na coluna "total"?  *R$ 2.222.973,00*



###### Questão 1.3 - Interpretação

Com base na análise exploratória realizada, escreva um breve diagnóstico sobre a confiabilidade do *dataset* vendas\_2023\_2024.csv para análises futuras. Comente sobre:

* Possíveis outliers em "total",
* Qualidade dos dados (valores nulos ou inconsistentes),
* e se você considera que o *dataset* está pronto para análises ou se exigiria tratamento prévio.



###### Texto a ser usado em relatório final, juntamente das análises numéricas até então apresentadas



Em primeira instância, partimos dos dados colhidos das vendas da loja, obtidos através de arquivo .CSV com 9895 registros de vendas, , exclusos aqui os registros nulos, contendo os seguintes campos:



&#x20;  NOME   |           DESCRIÇÃO            |TIPO DE DADO|NULOS? |

\----------|--------------------------------|------------|-------|

id        |Identificador único do registro |  INTEIRO   |  NÃO  |

id\_client |Identificador do cliente        |  INTEIRO   |  NÃO  |

id\_product|Identificador do produto        |  INTEIRO   |  NÃO  |

qtd       |Quantidade do item              |  INTEIRO   |  NÃO  |

total     |Valor total da venda            |    REAL    |  NÃO  |

sale\_date |Data da venda                   | CARACTERE  |  NÃO  |



Esses dados compreendem as vendas do biênio 2023/2024, iniciando-se em 01/01/2023 e encerrando em 31/12/2024.

É importante mencionar a ausência de campos nulos no cadastro, o que é uma característica positiva visto as observações repassadas em primeiro contato quanto da dificuldade em tratar da gestão dos negócios orientando-o aos dados. Partindo do pressuposto que equipamentos náuticos, em sua maioria, são itens de valor consideravelmente alto, tendo em vista que em uma busca rápida, as cinquenta maiores vendas referem-se a apenas dois itens (id do produto 73 e 76), cujo valor unitário passar de R$ 100 mil, e é adquirido em quantidades variadas (mínima de 1, máxima de 15). Com isso, a suposição de outliers fica inicialmente restrita quando vista apenas pelos dados das vendas, sem o conhecimento do catálogo, bem como da análise do cliente, no caso de itens vendidos por atacado. Um ponto negativo é que o tipo de dado usado para registrar as datas (CARACTERE) pode gerar erros, e deve ser ajustado para o formato de data.

Numericamente, temos os valores de venda distribuídos da seguinte maneira:

Referência|Valor da Venda |

\----------|---------------|

Mínimo    |*R$       294,50*|

Q1 (25%)  |*R$    23.138,20*|

Q2 (50%)  |*R$    82.225,00*|

Média     |*R$   263.797,83*|

Q3 (75%)  |*R$   339.168,00*|

Máximo    |*R$ 2.222.973,00*|

Vendo essas distribuições, podemos afirmar alguns pontos, a primeira é a de que, devido aos altos valores das vendas, a distribuição das mesmas  segue fortemente tensionada aso valores mais altos, a  grande diferença entre a média e a mediana comprova que  essa média não representa a maioria das vendas, num primeiro olhar.
Outro ponto é que, analisando os quartis, é possível dizer que é grande a probabilidade de termos possíveis erros de digitação de valores dentro de um determinado numero de vendas, tendo por base que o limite superior do terceiro quartil, quando aplicamos a regra de intervalo interquartil (IQR) indica que vendas maiores do que o valor de R$ 812.966,32 são possíveis outliers (ou podem tratar-se de vendas de embarcações inteiras). 
Quanto do volume de vendas, ao analisarmos as quantidades, temos o valor mínimo de 1 item, e o máximo de 15, sendo que a média encontrada pelos registros seria de 8, o que, de fato, descaracteriza uma possível venda de atacado, analisando apenas o quantitativo expresso nos dados. Novamente, sem avaliar a lista de produtos, para saber se pro exemplo, determinado item é vendido em caixas com grandes volumes, não é possível afirmar com certeza se a natureza da operação é estritamente reservada ao varejo.
Por fim, acreditamos que há a necessidade de um refinamento e um cruzamento dos dados, priorizando uma análise com maior valor para a gestão da empresa, bem como melhor controle das situações que abrangem o cotidiano da loja. Temos um volume de vendas consideravelmente robusto, E uma venda típica (obtida pela mediana) condizente com a realidade, porém , há a necessidade de auditar os grandes valores (outliers), bem como o faturamento médio.

