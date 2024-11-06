--Normalizando o banco de dados, criando novas tabelas e as relacionando
CREATE TABLE t_cidade(
	id_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
	cidade VARCHAR(50) NOT NULL
);
CREATE TABLE t_estado(
	id_estado INTEGER PRIMARY KEY AUTOINCREMENT,
	estado VARCHAR(20) NOT NULL
);
CREATE TABLE t_pais(
	id_pais INTEGER PRIMARY KEY AUTOINCREMENT,
	pais VARCHAR(50) NOT NULL
);
CREATE TABLE t_combustivel(
	id_combustivel INTEGER PRIMARY KEY AUTOINCREMENT,
	combustivel VARCHAR(20) NOT NULL
);
CREATE TABLE t_marca(
	id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
	marca VARCHAR(50) NOT NULL
);
CREATE TABLE cliente(
	id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(150) NOT NULL,
	cod_cidade SMALLINT NOT NULL,
	cod_estado SMALLINT NOT NULL,
	cod_pais SMALLINT NOT NULL,
	FOREIGN KEY (cod_cidade) REFERENCES t_cidade(id_cidade),
	FOREIGN KEY (cod_estado) REFERENCES t_estado(id_estado),
	FOREIGN KEY (cod_pais) REFERENCES t_pais(id_pais)
);
CREATE TABLE vendedor(
	id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(150) NOT NULL,
	sexo SMALLINT NOT NULL,
	cod_estado VARCHAR(20) NOT NULL,
	FOREIGN KEY (cod_estado) REFERENCES t_estado(id_estado)
);
CREATE TABLE carro(
	id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
	cod_marca SMALLINT NOT NULL,
	modelo VARCHAR(20) NOT NULL,
	ano SMALLINT(4) NOT NULL,
	cod_combustivel VARCHAR(20) NOT NULL,
	chassi_carro VARCHAR(50) NOT NULL,
	FOREIGN KEY (cod_marca) REFERENCES t_marca(id_marca),
	FOREIGN KEY (cod_combustivel) REFERENCES t_combustivel(id_combustivel)
);
CREATE TABLE locacao(
	id_locacao INTEGER PRIMARY KEY AUTOINCREMENT,
	cod_cliente SMALLINT NOT NULL,
	cod_vendedor SMALLINT NOT NULL,
	cod_carro SMALLINT NOT NULL,
	km_carro INT(7) NOT NULL,
	data_locacao DATETIME NOT NULL,
	hora_locacao DATETIME NOT NULL,
	qtd_diaria SMALLINT NOT NULL,
	valor_diaria DECIMAL NOT NULL,
	data_entrega DATETIME NOT NULL,
	hora_entrega DATETIME NOT NULL,
	FOREIGN KEY (cod_cliente) REFERENCES cliente(id_cliente),
	FOREIGN KEY (cod_vendedor) REFERENCES vendedor(id_vendedor),
	FOREIGN KEY (cod_carro) REFERENCES carro(id_carro)
);
--Inserindo dados nas tabelas, provenientes da tabela: tb_locacao
INSERT INTO t_cidade (cidade)
SELECT DISTINCT cidadeCliente
FROM tb_locacao
WHERE cidadeCliente NOT IN (
    SELECT cidade FROM t_cidade
);
INSERT INTO t_estado (estado)
SELECT DISTINCT estadoCliente
FROM tb_locacao
WHERE estadoCliente NOT IN (
    SELECT estado FROM t_estado
);
INSERT INTO t_pais (pais)
SELECT DISTINCT paisCliente
FROM tb_locacao
WHERE paisCliente NOT IN (
    SELECT pais FROM t_pais
);
INSERT INTO t_combustivel (combustivel)
SELECT DISTINCT tipoCombustivel
FROM tb_locacao
WHERE tipoCombustivel NOT IN (
    SELECT combustivel FROM t_combustivel
);
INSERT INTO t_marca (marca)
SELECT DISTINCT marcaCarro
FROM tb_locacao
WHERE marcaCarro NOT IN (
    SELECT marca FROM t_marca
);
INSERT INTO cliente (nome, cod_cidade, cod_estado, cod_pais)
SELECT DISTINCT tborigem.nomeCliente, t_cidade.id_cidade, t_estado.id_estado, t_pais.id_pais
FROM tb_locacao AS tborigem
JOIN t_cidade ON tborigem.cidadeCliente = t_cidade.cidade
JOIN t_estado ON tborigem.estadoCliente = t_estado.estado
JOIN t_pais ON tborigem.paisCliente = t_pais.pais
;
INSERT INTO vendedor (nome, sexo, cod_estado)
SELECT DISTINCT tborigem.nomeVendedor, tborigem.sexoVendedor, t_estado.id_estado
FROM tb_locacao AS tborigem
JOIN t_estado ON tborigem.estadoVendedor = t_estado.estado
;
INSERT INTO carro (cod_marca, modelo, ano, cod_combustivel, chassi_carro)
SELECT DISTINCT t_marca.id_marca, tborigem.modeloCarro, tborigem.anoCarro, t_combustivel.id_combustivel, tborigem.classiCarro 
FROM tb_locacao AS tborigem
JOIN t_marca ON tborigem.marcaCarro = t_marca.marca 
JOIN t_combustivel ON tborigem.tipoCombustivel = t_combustivel.combustivel 
;
INSERT INTO locacao (cod_cliente, cod_vendedor, cod_carro, km_carro, data_locacao, hora_locacao, 
	qtd_diaria, valor_diaria, data_entrega, hora_entrega)
SELECT DISTINCT cliente.id_cliente, vendedor.id_vendedor, carro.id_carro, tborigem.kmCarro, 
	tborigem.dataLocacao, tborigem.horaLocacao, tborigem.qtdDiaria, tborigem.vlrDiaria, 
	tborigem.dataEntrega, tborigem.horaEntrega
FROM tb_locacao AS tborigem
JOIN cliente ON tborigem.nomeCliente = cliente.nome 
JOIN vendedor ON tborigem.nomeVendedor = vendedor.nome 
JOIN carro ON tborigem.modeloCarro = carro.modelo 
;
--Tratando dados
UPDATE locacao
SET data_locacao = substr(data_locacao, 7, 2) || '/' || substr(data_locacao, 5, 2) || '/' || substr(data_locacao, 1, 4),
	data_entrega = substr(data_entrega, 7, 2) || '/' || substr(data_entrega, 5, 2) || '/' || substr(data_entrega, 1, 4)
;
UPDATE vendedor
SET sexo = CASE
    WHEN sexo = 0 THEN 'M'
    WHEN sexo = 1 THEN 'F'
END
;
