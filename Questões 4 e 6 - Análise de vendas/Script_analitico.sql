/*Comparar o valor da venda em reais com o valor do custo, convertido em reais com base no dolar do dia.
	Demonstrar o saldo da operação, em busca das operações de lucvro e prejuizo*/
WITH calculo_operacoes AS (
	--Primeira Query que retornou valore s de lucro e prejuizo
	SELECT
		-- tirando o ticket da venda
		v.id AS id_venda,
		v.sale_date,
		v.id_product,
		v.qtd,
		v.total AS valor_recebido_em_brl,
		--buscar o custo em dolar e fazer a conversão
		(ci.usd_price * v.qtd *hd.cotacao_venda) AS custo_operacao_brl,
		-- Saldo da operação, positivo é lucro, negativo é prejuizo
		v.total - (ci.usd_price * v.qtd *hd.cotacao_venda) AS saldo_operacao_brl
	FROM
		vendas_2023_2024 v -- v para resumir
	-- join entre custos_importação e produto especíco da venda	
	JOIN custos_importacao ci ON v.id_product = ci.product_id 
	-- join entre a data da cotação e a da venda
	JOIN historico_dolar hd ON v.sale_date = hd.data_cotacao 
)
-- subquery dentro da primeira, quesinaliza cusot e saldo da operaçaõ
SELECT
	*,
	-- condicional que aponta prejuzio
	CASE 
		WHEN saldo_operacao_brl < 0 THEN 'Sim'
		ELSE 'Não'
	END AS possui_prejuizo, -- separa essa condicional em uma coluna própria
	-- converte os negativos em positivos, afim de poder trabalhar melhor o calculo
	CASE
		WHEN saldo_operacao_brl < 0 THEN ABS(saldo_operacao_brl)
		ELSE 0
	END AS valor_do_prejuizo -- valor do prejuuizo, agora em positivo
FROM calculo_operacoes --campo da subquery
WHERE saldo_operacao_brl < 0 --Filtrando apenas os prejuizos
ORDER BY saldo_operacao_brl ASC;

-- Agregação por produto e respostas ao stakeholder
WITH calculo_operacoes2 AS (
	--Primeira Query que retornou valore s de lucro e prejuizo
	SELECT
		-- tirando o ticket da venda
		v.id AS id_venda,
		v.sale_date,
		v.id_product,
		v.qtd,
		v.total AS valor_recebido_em_brl,
		--buscar o custo em dolar e fazer a conversão
		(ci.usd_price * v.qtd *hd.cotacao_venda) AS custo_operacao_brl,
		-- Saldo da operação, positivo é lucro, negativo é prejuizo
		v.total - (ci.usd_price * v.qtd *hd.cotacao_venda) AS saldo_operacao_brl
	FROM
		vendas_2023_2024 v -- v para resumir
	-- join entre custos_importação e produto especíco da venda	
	JOIN custos_importacao ci ON v.id_product = ci.product_id 
	-- join entre a data da cotação e a da venda
	JOIN historico_dolar hd ON v.sale_date = hd.data_cotacao 
)
-- subquery dentro da primeira, de onde se obtem os percentuais a partir do produto
SELECT
	id_product, --elemento agregador
	-- Receita total
	ROUND(SUM(valor_recebido_em_BRL), 2) AS receita_total_brl,
	-- Prejuízo Total
	--  condicional converte apenas os negativos em positivos, afim de poder trabalhar melhor o calculo
	ROUND(SUM(CASE
		WHEN saldo_operacao_brl < 0 THEN ABS(saldo_operacao_brl) 
		ELSE 0
	END), 2) AS prejuizo_total_brl,
	-- percentual de perda
	ROUND(
		(SUM(CASE WHEN saldo_operacao_brl < 0 THEN ABS(saldo_operacao_brl) ELSE 0 END) /
		SUM(valor_recebido_em_brl)) * 100, 2
	) AS percentual_perda
FROM calculo_operacoes2 
GROUP BY id_product
ORDER BY percentual_perda DESC;