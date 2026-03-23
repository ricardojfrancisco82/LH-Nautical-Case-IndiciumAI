![Python3](https://img.shields.io/static/v1?label=Python3\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=python\&logoColor=lightblue)
![SQLite](https://img.shields.io/static/v1?label=SQLite\&labelColor=003B57\&message=ok!%E2%9C%94\&style=plastic\&color=003B57\&logo=sqlite\&logoColor=80c6f1)
![BCB Olinda](https://img.shields.io/static/v1?label=BCB\&labelColor=003366\&message=Olinda%20API\&style=plastic\&color=FFD700\&logo=google-cloud\&logoColor=FFD700)
![Pandas](https://img.shields.io/static/v1?label=Pandas\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=pandas\&logoColor=lightblue)
![NumPy](https://img.shields.io/static/v1?label=NumPy\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=numpy\&logoColor=lightblue)




### Questão 4 - Dados Públicos



#### Cenário



O Sr. Almir identificou que alguns produtos podem ter sido vendidos abaixo do custo, possivelmente por erro operacional.



O problema é que:

* O sistema de vendas (vendas\_2023\_2024.csv) registra valores em real BRL
* O catálogo de fornecedores (custos\_importacao.json) registra custos unitários em dollar USD
* O câmbio varia diariamente



Até hoje, ninguém cruzou o custo em dólar do dia da venda com o valor de venda em reais.

Sua missão é abrir essa “caixa preta” financeira e identificar onde houve prejuízo real.



Premissas obrigatórias:

* O custo em USD é unitário
* O custo em BRL deve ser calculado usando o câmbio da data da venda
* A taxa de câmbio deve ser considerada a média da cotação de venda do dia (Banco Central, disponibilizado em https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/)
* A receita total do produto considera todas as vendas (inclusive as sem prejuízo)
* Ignore impostos e frete



#### Tarefas:



**Parte 1 — Cálculo e modelagem**

* Calcule o custo total em BRL por transação
* Identifique transações com prejuízo
* Agregue os dados por id\_produto, gerando:
* Receita total (BRL)
* Prejuízo total (BRL)
* Percentual de perda (prejuízo\_total / receita\_total)

**Parte 2 — Análise visual**

Gere um gráfico que represente o prejuízo total por produto, considerando apenas produtos que tiveram prejuízo. (Inserir o gráfico no relatório/dashboard final)

**Parte 3 —  Análise objetiva Responda objetivamente:**

1. Qual produto concentra o maior prejuízo absoluto?  *76|Motor Diesel Honda Aero 205HP*
2. O produto com maior prejuízo absoluto também é o que possui a maior porcentagem de perda? *Não, seu índice é de 28,7%* 



#### Questão 4.1 - Código SQL

1. Código calculando:
* custo em R$ (custo\_usd \* taxa\_cambio\_data) - Se atentar ao cambio do dia

2\. Agregação por id\_produto contendo:

* Receita total (soma do valor de venda em reais),
* Prejuízo total (soma apenas das perdas),
* Percentual de perda (prejuízo\_total / receita\_total).



#### Questão 4.2 - Validação

Qual é o id\_produto que apresentou a maior porcentagem de perda financeira relativa (maior % de prejuízo sobre sua receita) no período analisado? *42|Transponder Lowrance Axis, com 47,96%*



#### Questão 4.3 - Interpretação

Explicação sobre o desenvolvimento:

* Qual data de câmbio você utilizou?

*O resgate fora efetuado à partir de dados resgatados do banco central, conforme mencionado anteriormente (uma media entre quatro coletas do mesmo dia), para fins analíticos, todas as datas foram equiparadas, sem horário específico, a fim de que não houvesse problemas com as junções em SQL.*

* Como definiu o prejuízo?

*Depois de convertidos os valores em Reais (BRL) definiu-se prejuízo como o saldo negativo existente entre a operação de venda e o valor do produto com cambio convertido na cotação do dólar do dia.*

* Alguma suposição relevante?

Analisando as perdas percentuais (prejuízo relativo), Pode-se verificar que sete itens tiveram prejuízo relativo igual ou maior de 40%, seno destes os dois maiores em eletrônicos, seguidos por três de propulsão. 
Já em valores totais, três dos cinco itens (sete entre os dez primeiros) que mais deram prejuízo são da categoria propulsão, o que faz bastante sentido dado o alto valor agregado de tais itens. 

**Nota:** Efetuar uma analise mais aprofundada em python com os csv resultados das consultas.


Nota para relatório, sobre obtenção de histórico do dólar comercial



Para o biênio 2023/2024,o valor que a API do BCB entrega (via Olinda/PTAX) não é uma extração pontual de um único momento, mas sim uma média calculada.



Aqui estão os detalhes técnicos para você ter segurança no seu histórico:



A API retorna a taxa PTAX, que é a taxa de referência do mercado de câmbio no Brasil. Ela é calculada através de quatro janelas de consulta ao longo do dia com as instituições financeiras, pelo Banco Central.

O valor final diário que aparece na API é a média aritmética dessas 4 consultas.

Por ser uma média do dia, ela é considerada a taxa oficial para contratos, balanços e para o cálculo de impostos na importação.



Fonte: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2023'\&@dataFinalCotacao='12-31-2024'\&$top=1000\&$skip=0\&$format=text/csv\&$select=cotacaoVenda,dataHoraCotacao

Consultado Às 14h00 deo dia 19-03-26


Recomposto o banco de dados com suas relações em arquivo único, normalizadas as datas presentes em *vendas23_24_datas.csv* para compatibilidade com demais datas, bem como exclusão de registros nulos. 
