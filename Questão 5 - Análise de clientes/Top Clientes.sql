/* Premissas obrigatórias:
* Faturamento Total: Soma da coluna total por cliente.
* Frequência: Contagem total de transações (IDs de venda) por cliente.
* Ticket Médio: Faturamento Total / Frequência.
* Diversidade de Categorias: Quantidade de categorias distintas que o cliente comprou. join produto
* Filtro de Elite: *Apenas clientes que compraram produtos de 3 ou mais categorias distintas devem ser considerados no ranking.*
* Desempate: *Em caso de empate no Ticket Médio, utilize o _id_cliente_ em ordem crescente.*/

-- descrição das tabelas

PRAGMA table_info(vendas_2023_2024)

PRAGMA table_info(produtos)

PRAGMA tabele_info(clientes_crm)

-- CTE (Top 10 x Ticket médio x Categorias)

WITH metricas_clientes AS (
    SELECT
    	--todos cahamdos aqui emn função do group by GROUP BY
        v.id_client,
        SUM(v.total) AS faturamento_total, 
        COUNT(v.id) AS frequencia,
        (SUM(v.total) / COUNT(v.id)) AS ticket_medio,
        COUNT(DISTINCT p.actual_category) AS diversidade_categorias
    FROM vendas_2023_2024 v
    JOIN produtos p ON v.id_product = p.code --id do produto nas duas tabelas. produtos e vendas
    GROUP BY v.id_client
)
-- filtro da primeira pesquisa, pegando o top 10 por maior ticket médio, e mais baixa id_do cliente (critério de desempate 
SELECT 
    id_client,
    faturamento_total,
    frequencia,
    ticket_medio,
    diversidade_categorias
FROM metricas_clientes
WHERE diversidade_categorias >= 3
ORDER BY ticket_medio DESC, id_client ASC
LIMIT 10;

-- CTE Categoria com mais itens para o grupo Top 10

WITH metricas_clientes2 AS (
    SELECT 
        v.id_client,
        (SUM(v.total) / COUNT(v.id)) AS ticket_medio,
        COUNT(DISTINCT p.actual_category) AS diversidade_categorias
    FROM vendas_2023_2024 v
    JOIN produtos p ON v.id_product = p.code
    GROUP BY v.id_client
),
-- rankeamento dos clientes, aprtindo da primeira query com o fim de pegar o top 10 com3 categorias eos menores client_id
clientes_elite AS (
    SELECT id_client
    FROM metricas_clientes2
    WHERE diversidade_categorias >= 3
    ORDER BY ticket_medio DESC, id_client ASC
    LIMIT 10
)
SELECT -- Essa query é pra filtrar o principal resultado pelo totla de itrens comprados
    p.actual_category AS categoria_campea,
    SUM(v.qtd) AS total_itens_comprados
FROM vendas_2023_2024 v
JOIN produtos p ON v.id_product = p.code
JOIN clientes_elite ce ON v.id_client = ce.id_client
GROUP BY p.actual_category
ORDER BY total_itens_comprados DESC
LIMIT 1;







