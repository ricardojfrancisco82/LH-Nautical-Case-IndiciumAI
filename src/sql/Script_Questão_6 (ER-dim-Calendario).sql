-- Criar uma tabela de Dimensão Calendário
CREATE TABLE dim_calendario (
    data_id DATE PRIMARY KEY,
    ano INTEGER,
    mes INTEGER,
    dia_semana_num INTEGER,
    dia_semana_nome TEXT,
    eh_final_semana INTEGER
);

 --Gerar e inserir os dados usando uma CTE Recursiva
INSERT INTO dim_calendario
WITH RECURSIVE gera_datas(d) AS (
    -- Data de início baseada no seu contexto (vendas_2023_2024)
    VALUES('2023-01-01')
    UNION ALL
    -- Adiciona 1 dia sucessivamente até o fim de 2024
    SELECT date(d, '+1 day') FROM gera_datas WHERE d < '2024-12-31'
)
SELECT 
    d AS data_id,
    strftime('%Y', d) AS ano,
    strftime('%m', d) AS mes,
    strftime('%w', d) AS dia_semana_num, -- 0=Domingo, 1=Segunda, ..., 6=Sábado
    CASE strftime('%w', d)
        WHEN '0' THEN 'Domingo'
        WHEN '1' THEN 'Segunda-feira'
        WHEN '2' THEN 'Terça-feira'
        WHEN '3' THEN 'Quarta-feira'
        WHEN '4' THEN 'Quinta-feira'
        WHEN '5' THEN 'Sexta-feira'
        WHEN '6' THEN 'Sábado'
    END AS dia_semana_nome,
    CASE WHEN strftime('%w', d) IN ('0', '6') THEN 1 ELSE 0 END AS eh_final_semana
FROM gera_datas;

-- LEFT JOIN entre vendas e calendario, para as vendas totais diárias

SELECT
	dc.data_id, 
	dc.dia_semana_nome,
	--COALESCE Substituui Nulos por zero, caso não haja vendas (efeito de media)
	COALESCE(SUM(v.total), 0) AS faturamento_diario -- soma o campo total de vendas, agrupados por dia
FROM dim_calendario dc 
-- calendarioa a esquerda para conter todos os dias do ano
LEFT JOIN vendas_2023_2024 v ON dc.data_id = v.sale_date 
GROUP BY dc.data_id, dc.dia_semana_nome
ORDER BY dc.data_id 


-- Que vira um subconsulta para obtermos as medias de vendas por dia da semana

SELECT 
    dia_semana_nome,
    ROUND(AVG(faturamento_diario), 2) AS media_vendas
FROM (
    -- LEFT JOIN entre vendas e calendario, para as vendas totais diárias
    SELECT
        dc.data_id, 
        dc.dia_semana_nome,
        dc.dia_semana_num,
        COALESCE(SUM(v.total), 0) AS faturamento_diario 
    FROM dim_calendario dc 
    LEFT JOIN vendas_2023_2024 v ON dc.data_id = v.sale_date
    GROUP BY dc.data_id, dc.dia_semana_nome, dc.dia_semana_num
) AS faturamento_por_data
GROUP BY dia_semana_nome, dia_semana_num
ORDER BY dia_semana_num DESC;