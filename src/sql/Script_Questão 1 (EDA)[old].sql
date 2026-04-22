/* Verificar o numero total de registros*/

SELECT COUNT (*) AS total_registros FROM vendas_2023_2024;

-- Verificar o número de colunas da tabela e seus rótulos

DESCRIBE vendas_2023_2024;

-- Verificar o intervalo de datas em sales_date

SELECT 
    MIN(sale_date) AS data_inicio, 
    MAX(sale_date) AS data_final   
FROM vendas_2023_2024;

-- Verificar o intervalo de datas em sales_date

SELECT 
    MIN(total) AS valor_minimo, 
    MAX(total) AS valor_maximo,
    AVG(total) AS valor_medio
FROM vendas_2023_2024;

/*Deste ponto, estamos levantando dados adicionais com a finalizadade eespecifica de embasar as questões formuladas em 1.3*/

-- Selecionando quartis na coluna 

WITH Quartis AS (
    SELECT 
        total, -- cria-se uma tabela temporária (CTE)
        NTILE(4) OVER (ORDER BY total) as quartil -- coloca os preços em ordem crescente com order by e divide em 4 parte chadas quartil1-4 com NTILE
    FROM vendas_2023_2024
)
SELECT  -- pontos de corte de cada parte extraída com NTILE
    MAX(CASE WHEN quartil = 1 THEN total END) as Q1, -- pega o valor final do primeiro quertil (25%)
    MAX(CASE WHEN quartil = 2 THEN total END) as Mediana, -- pega o valor final do segundo quartil quertil (50%)
    MAX(CASE WHEN quartil = 3 THEN total END) as Q3 -- pega o valor final do terceiro quertil (75%)
FROM Quartis;

-- Verificando as quantidades em busca de possíveis vendas de atacado

SELECT 
    MIN(qtd) AS valor_minimo, 
    MAX(qtd) AS valor_maximo,
    AVG(qtd) AS valor_medio
FROM vendas_2023_2024;

-- Verificando se os bens vendidos são de grande monta

SELECT *, 
       (total / CAST(qtd AS REAL)) AS valor_unitario -- uso de CAST AS REAL para garantir que a divisão não seja arredondada
FROM vendas_2023_2024 
ORDER BY valor_unitario DESC --ordenando à partir do maior valor
LIMIT 50; --limitando aos vinte maiores registros