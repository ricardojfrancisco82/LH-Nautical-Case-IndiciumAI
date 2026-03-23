![Python3](https://img.shields.io/static/v1?label=Python3\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=python\&logoColor=lightblue)
![Pandas](https://img.shields.io/static/v1?label=Pandas\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=pandas\&logoColor=lightblue)
![NumPy](https://img.shields.io/static/v1?label=NumPy\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=numpy\&logoColor=lightblue)
![Scikit-learn](https://img.shields.io/static/v1?label=Scikit-learn\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=scikitlearn\&logoColor=lightblue)

### Questão 8 - Sistema de recomendação

#### Cenário

A Marina percebeu que clientes que compram lanchas quase sempre esquecem de levar a defensa (proteção lateral). Ela quer implementar uma vitrine de "Quem comprou isso, também levou..." no site.
Como não temos ferramentas de Big Data caras, você precisará criar um motor de recomendação, baseado na similaridade de compra dos clientes.
Identificar qual produto deve ser recomendado junto ao item “GPS Garmin Vortex Maré Drift”, com base na similaridade de comportamento de compra dos clientes.

#### Tarefa:

1. Crie uma matriz de interação Usuário × Produto obedecendo às regras abaixo:
     a. Linhas: id_cliente
     b. Colunas: id_produto
     c. Valor da célula:
     d. 1 se o cliente comprou ao menos uma vez o produto
     e. 0 caso contrário
     f. Ignore a quantidade comprada (presença/ ausência apenas)
2. Cálculo de Similaridade entre Produtos
     a. Calcule a Similaridade de Cosseno (Cosine Similarity) entre os vetores dos produtos
     b. A similaridade deve ser calculada produto × produto, com base nos clientes que compraram cada item
3. Ranking de Produtos Similares
     a. Considere o produto “GPS Garmin Vortex Maré Drift” como item de referência
     b. Gere um ranking com os 5 produtos mais similares a ele
     c. Desconsidere o próprio GPS no ranking

#### Questão 8.1 - Código em python

Script em python que:
1.Constrói a matriz usuário–item
2.Calcula a similaridade de cosseno
3.Gera o ranking de similaridade
4.Bibliotecas permitidas:
     - pandas
     - numpy
     - sklearn (opcional, para cosine similarity)

#### Questão 8.2 - Validação

Qual é o id_produto com MAIOR similaridade ao “GPS Garmin Vortex Maré Drift”? *94 - Motor de Popa Volvo Magnum 276HP*

#### Questão 8.3 - Explique:

* Como a matriz foi construída?
*Para construir um sistema de recomendação de produtos, com base no produto anterior selecionado e por similaridades, o primeiro passo é criar uma matriz que relaciona as aquisições dos clientes e os produtos em si. O resultado dessa matriz, é no caso uma linha que registra a quantidade de ocorrências de compra dos produtos, que situam-se nas colunas.*
*O próximo passo foi converter os valores registrados em booleano, pois só queríamos saber da convergência (haver compras relacionados) ou não dos produtos.*
* O que significa a similaridade de cosseno nesse contexto?
*Nesse contexto, a similaridade de cosseno é o resultado da relação existente entre as vendas de produtos, com a conversão das ocorrências como um vetor, onde um ângulo de zero representa que os vetores apontam para a mesma direção, ou seja, são 100%$ compatíveis entre si* 
* Uma limitação desse método de recomendação.
Produtos que tenham uma venda muito maior que outros, dentro do segmento, como o pão numa padaria, tendem a ser compatíveis com quase todos os outros proudtos da análise , por uma questão de popularidade, assim como produtos novos tendem a não se relacionar com os outros durante um tempo, porque terão muitos registros zerados. 


