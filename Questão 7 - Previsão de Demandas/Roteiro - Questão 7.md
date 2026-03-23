![Python3](https://img.shields.io/static/v1?label=Python3\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=python\&logoColor=lightblue)
![Pandas](https://img.shields.io/static/v1?label=Pandas\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=pandas\&logoColor=lightblue)
![NumPy](https://img.shields.io/static/v1?label=NumPy\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=numpy\&logoColor=lightblue)
![Scikit-learn](https://img.shields.io/static/v1?label=Scikit-learn\&labelColor=navy\&message=ok!%E2%9C%94\&style=plastic\&color=lightblue\&logo=scikitlearn\&logoColor=lightblue)
![Prophet](https://img.shields.io/static/v1?label=Prophet&labelColor=006699&message=ok!%E2%9C%94&style=plastic&color=008080&logo=facebook&logoColor=white)

### Questão 7 - Previsão de demanda


#### Cenário

O Sr. Almir está furioso. No último verão, o estoque de "Coletes Salva-Vidas" acabou em 10 dias, e a empresa perdeu milhares de reais em vendas. Por outro lado, compraram "Âncoras" demais e elas estão enferrujando no galpão. Gabriel Santos, o Tech Lead, disse que não dá mais para confiar no "feeling". Ele quer um modelo preditivo que diga exatamente quantas unidades venderemos no próximo mês para ajustar as compras com fornecedores.

#### Premissas obrigatórias:
* O período de treino deve incluir dados até 31/12/2023.
* O período de teste deve ser todo o mês de Janeiro de 2024.
* A previsão deve ser feita em base diária.
* Não é permitido utilizar dados futuros no treino (data leakage).
* Considere apenas o produto: "Motor de Popa Yamaha Evo Dash 155HP"

#### Tarefa:
1.Utilize o dataset vendas_2023_2024.csv
2.Construa um modelo baseline simples, utilizando: Média móvel dos últimos 7 dias de vendas (considerando apenas dados anteriores à data prevista).
3.Gere a previsão diária de vendas para Janeiro de 2024.
4.Compare as previsões com os valores reais do período de teste utilizando a métrica: MAE — Mean Absolute Error
5.Responda objetivamente:
     a. O baseline é adequado para esse produto?
	*Sim, tendo em vista que a MAE é próxima de um, que este é um produto de alto valor agregado e não pode gerar encalhe no estoque, e também não pode ser vitimado por explosões em vendas.*
     b. Cite uma limitação desse método.
	*O efeito de atraso, como, por exemplo, um evento náutico só aparecerá nas estatísticas sete dias após ocorrer.

#### Questão 7.1 - Código em python
Adicione o código python usado para construção do modelo.

#### Questão 7.2 - Validação
Utilizando seu modelo treinado, qual é a soma total da previsão de vendas (arredondada para número inteiro) para o 'Motor de Popa Yamaha Evo Dash 155HP' durante a primeira semana de Janeiro de 2024 (01/01 a 07/01)? *zero*

#### Questão 7.3 - Explique:
Como o baseline foi construído?
*Primeiro, fora destacadas as vendas diárias do motor, alvo da analise.*
Como evitou data leakage?
*Optei por criar variáveis fixando o período de teste, e o período de previsão, separadas e exatamente dentro do período estabelecido (teste com os dados de 2023, , previsão do mês de Janeiro de 2024)*
Uma limitação do modelo proposto
*O efeito de atraso, como, por exemplo, um evento náutico só aparecerá nas estatísticas sete dias após ocorrer.*


