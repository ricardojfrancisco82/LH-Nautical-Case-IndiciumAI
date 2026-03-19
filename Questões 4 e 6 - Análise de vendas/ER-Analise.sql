--Criando as  tabelas, capos e suas relaçoes

CREATE TABLE produtos (
    code INTEGER PRIMARY KEY,
    name TEXT,
    actual_category TEXT,
    price REAL
);

CREATE TABLE custos_importacao (
    product_id INTEGER,
    name TEXT,
    category TEXT,
    usd_price REAL,
    start_date TEXT,
    -- relaçoes externas
    FOREIGN KEY (product_id) REFERENCES produtos(code)
);

CREATE TABLE historico_dolar (
    data_cotacao TEXT PRIMARY KEY,
    cotacao_venda REAL,
    id INTEGER
);

CREATE TABLE clientes_crm (
    code INTEGER PRIMARY KEY,
    full_name TEXT,
    location TEXT,
    email TEXT
);

CREATE TABLE vendas_2023_2024 (
	id INTEGER PRIMARY KEY,
	id_client INTEGER,
	id_product INTEGER,
	qtd INTEGER,
	total REAL,
	sale_date TEXT,
	--relaçoes externas
	FOREIGN KEY (id_product) REFERENCES produtos(code),
	FOREIGN KEY (id_client) REFERENCES clientes_crm(code)
);

