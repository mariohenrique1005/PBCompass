--Criando tabelas para o banco de dados dimensional

CREATE TABLE d_cliente(
	id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(150) NOT NULL,
	cidade VARCHAR(50) NOT NULL,
	estado VARCHAR(20) NOT NULL,
	pais VARCHAR(20) NOT NULL
);
CREATE TABLE d_vendedor(
	id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(150) NOT NULL,
	sexo VARCHAR(10) NOT NULL,
	estado VARCHAR(20) NOT NULL
);
CREATE TABLE d_carro(
	id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
	marca VARCHAR(20) NOT NULL,
	modelo VARCHAR(20) NOT NULL,
	ano SMALLINT(4) NOT NULL,
	combustivel VARCHAR(20) NOT NULL,
	km_carro INT(7) NOT NULL,
	chassi_carro VARCHAR(50) NOT NULL
);
CREATE TABLE f_locacao(
	id_locacao INTEGER PRIMARY KEY AUTOINCREMENT,
	cod_cliente SMALLINT NOT NULL,
	cod_vendedor SMALLINT NOT NULL,
	cod_carro SMALLINT NOT NULL,
	data_locacao DATETIME NOT NULL,
	hora_locacao DATETIME NOT NULL,
	qtd_diaria SMALLINT NOT NULL,
	valor_diaria DECIMAL NOT NULL,
	data_entrega DATETIME NOT NULL,
	hora_entrega DATETIME NOT NULL,
	FOREIGN KEY (cod_cliente) REFERENCES d_cliente(id_cliente),
	FOREIGN KEY (cod_vendedor) REFERENCES d_vendedor(id_vendedor),
	FOREIGN KEY (cod_carro) REFERENCES d_carro(id_carro)
);

--Inserindo dados nas tabelas, provenientes das tabelas normalizadas

INSERT INTO d_cliente (nome, cidade, estado, pais)
SELECT DISTINCT cliente.nome, t_cidade.cidade, t_estado.estado, t_pais.pais
FROM cliente
JOIN t_cidade ON cliente.cod_cidade = t_cidade.id_cidade
JOIN t_estado ON cliente.cod_estado = t_estado.id_estado
JOIN t_pais ON cliente.cod_pais = t_pais.id_pais
;
INSERT INTO d_vendedor (nome, sexo, estado)
SELECT DISTINCT vendedor.nome, vendedor.sexo, t_estado.estado
FROM vendedor
JOIN t_estado ON vendedor.cod_estado = t_estado.id_estado
;
INSERT INTO d_carro (marca, modelo, ano, combustivel, km_carro, chassi_carro)
SELECT DISTINCT t_marca.marca, carro.modelo, carro.ano, t_combustivel.combustivel, locacao.km_carro, carro.chassi_carro
FROM carro
JOIN t_marca ON carro.cod_marca = t_marca.id_marca 
JOIN t_combustivel ON carro.cod_combustivel = t_combustivel.id_combustivel
JOIN locacao ON carro.id_carro = locacao.cod_carro
;
INSERT INTO f_locacao (cod_cliente, cod_vendedor, cod_carro, data_locacao, hora_locacao, qtd_diaria, 
	valor_diaria, data_entrega, hora_entrega)
SELECT DISTINCT d_cliente.id_cliente, d_vendedor.id_vendedor, d_carro.id_carro, locacao.data_locacao, 
	locacao.hora_locacao, locacao.qtd_diaria, locacao.valor_diaria, locacao.data_entrega, locacao.hora_entrega
FROM locacao
JOIN d_cliente ON locacao.cod_cliente = d_cliente.id_cliente 
JOIN d_vendedor ON locacao.cod_vendedor = d_vendedor.id_vendedor
JOIN d_carro ON locacao.cod_carro = d_carro.id_carro
;