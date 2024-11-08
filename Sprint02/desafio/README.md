# Desafio
Para a execução deste desafio foram executados vários scripts SQL no ambiente do DBeaver

## Etapas

1. Primeiramente foram observados os dados da tabela e posteriormente criados as tabelas com os devidos relacionamentos
[Evidencia 1](../evidencias/01.png)

2. Logo após a criação das tabelas e seus relacionamentos, foram inseridos os dados, copiados da tabela principal: "tb_locacao" não-normalizada 
[Evidencia 2](../evidencias/02.png) | [Evidencia 3](../evidencias/03.png)

3. Foi realizada uma consulta simples, para verificar se os dados estavam todos corretos de acordo com a tabela principal 
[Evidencia 4](../evidencias/04.png) | [Evidencia 5](../evidencias/05.png)

4. Com o banco de dados normalizado, foram criadas novas tabelas para o formato dimensional, contendo 3 tabelas dimensão e 1 tabela fato
[Evidencia 6](../evidencias/06.png)

5. Os dados foram inseridos nas tabelas dimensionais, tendo o seu conteúdo originado do banco de dados normalizado. 
Após isso foi feita uma consulta para verificar se os dados estavam corretos
[Evidencia 7](../evidencias/07.png)

6. Com as tabelas dimensionais criadas foram criadas as views
[Evidencia 8](../evidencias/08.png)

7. Execução de um comando simples de consulta para verificar a view da tabela fato
[Evidencia 9](../evidencias/09.png)

8. Após constatar algumas inconsistências de dados, foram tratados os dados que continham datas e sexo (mais detalhes na seção de erros e problemas)
[Evidencia 10](../evidencias/10.png) | [Evidencia 11](../evidencias/11.png)

9. Com o script do banco de dados concluído, foram gerados os modelos: relacional e dimensional
[Modelo relacional](relacional.png) | [Modelo dimensional](dimensional.png)

## Erros e problemas

1. Os dados inconsistentes na tabela "tb_locacao" como os que continham data estavam inseridos como: "20151108", o que tornaria difícil a leitura.
Então foi inserido um comando para a tabela normalizada: "locacao" para separar o que é ano, mês e dia. 
Os dados como sexo estavam classificados apenas como: 0 ou 1, então foi criada uma classificação de condição, em que "0" se tornaria "M", e "1" se tranformaria em "F"

2. A execução de comandos equivocados na ordem dos caracteres da data fez com que os dados relacionados a data na tabela: "locacao"(normalizada)
se tornassem ilegíveis, então foi necessária a exclusão da tabela "locacao" e após este evento foram reexecutados os scripts de
 criação da tabela e inserção dos dados corretos oriundos da tabela: "tb_locacao"

3. A constatação de dados inconsistentes nas tabelas normalizadas: "locacao" e "vendedor", oriundos da tabela principal "tb_locacao"(não-normalizada)
 após ter realizado todos os procedimentos de dimensionalização fez com que fosse necessário a exclusão das tabelas dimensionais: 
 "f_locacao" e "d_cliente", após este evento foram reexecutados os scripts de criação das tabelas e inserção dos dados corretos oriundos das 
 tabelas: "locacao" e "vendedor"(normalizados).