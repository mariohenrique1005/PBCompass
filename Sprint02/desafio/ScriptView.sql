--Dimensão Carro
CREATE VIEW dim_carro AS
SELECT id_carro AS codCarro,
	marca AS marca,
	modelo AS modelo,
	ano AS ano,
	combustivel AS combustivel,
	km_carro AS quilometragem,
	chassi_carro AS chassi
FROM d_carro
;
--Dimensão Cliente
CREATE VIEW dim_cliente AS
SELECT id_cliente AS codCliente,
	nome AS nome,
	cidade AS cidade,
	estado AS estado,
	pais AS pais
FROM d_cliente
;
--Dimensão Vendedor
CREATE VIEW dim_vendedor AS
SELECT id_vendedor AS codVendedor,
	nome AS nome,
	sexo AS sexo,
	estado AS estado
FROM d_vendedor
;
--Tabela Fato Locação
CREATE VIEW ft_locacao AS
SELECT id_locacao AS codLocacao,
	cod_cliente AS codCliente,
	cod_vendedor AS codVendedor,
	cod_carro AS codCarro,
	data_locacao AS data_locacao,
	hora_locacao AS hora_locacao,
	qtd_diaria AS qtd_diaria,
	valor_diaria AS valor_diaria,
	data_entrega AS data_entrega,
	hora_entrega AS hora_entrega
FROM f_locacao
JOIN d_cliente ON f_locacao.cod_cliente = d_cliente.id_cliente
JOIN d_vendedor ON f_locacao.cod_vendedor = d_vendedor.id_vendedor 
JOIN d_carro ON f_locacao.cod_carro = d_carro.id_carro 
;