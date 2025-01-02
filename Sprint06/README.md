# Instruções

Nesta Sprint foi realizada a primeira etapa do desafio final: upload dos arquivos CSV sem tratamento para um Bucket na AWS. Também foram executados exercícios para a prática dos serviços AWS.<br>

## Resumo

**Amazon Athena:** Como criar bancos de dados e executar consultas

**AWS Lambda:** Como criar e executar funções

**Docker:** Como copiar arquivos e instalar bibliotecas

# Certificados

[Introdução ao Amazon Athena](certificados/Amazon-Athena.pdf)

[Amazon EMR Getting Started](certificados/Amazon-EMR.pdf)

[Amazon Redshift Getting Started](certificados/Amazon-Redshift.pdf)

[Noções básicas de Analytics na AWS - Parte 1](certificados/Analytics1.pdf)

[Fundamentos de Analytics na AWS - Parte 2](certificados/Analytics2.pdf)

[AWS Glue Getting Started](certificados/AWS-Glue.pdf)

[Melhores práticas para Data Warehousing com Amazon Redshift](certificados/DWAmazon-Redshift.pdf)

[Amazon Quicksight - Getting Started](certificados/QuickSight.pdf)

[Serverless Analytics](certificados/Serverless-Analytics.pdf)


# Exercícios

[Pasta Exercicios](exercicios/)

Exercício 1 - Lab AWS S3
![Lab AWS S3](exercicios/01_01.png)
![Lab AWS S3](exercicios/01_02.png)

Link para o endpoint do bucket: http://s6-exercicio01.s3-website-us-east-1.amazonaws.com

Exercicio 2 - Lab AWS Athena
![Lab AWS Athena](exercicios/02_01.png)
![Lab AWS Athena](exercicios/02_02.png)

Código da consulta utilizada:
```
WITH Decadas AS (
    SELECT 
        Nome,
        Sexo,
        (Ano / 10) * 10 AS Decada,  -- Cálculo da Década
        SUM(Total) AS Total_usos
    FROM nomes
    WHERE Ano >= 1950
    GROUP BY Nome, Sexo, (Ano / 10) * 10
),
TopNomes AS (
    SELECT 
        Nome,
        Sexo,
        Decada,
        Total_usos,
        ROW_NUMBER() OVER (PARTITION BY Decada ORDER BY Total_usos DESC) AS rank
    FROM Decadas
)
SELECT 
    Decada,
    Sexo,
    Nome,
    Total_usos
FROM TopNomes
WHERE rank <= 3
ORDER BY Decada, rank;
```
CSV com os resultados:
[Resultados](exercicios/Ex2-Resultados.csv)

Exercicio 3 - Lab AWS Lambda

![Lab AWS Lambda](exercicios/03_01.png)
![Lab AWS Lambda](exercicios/03_02.png)
![Lab AWS Lambda](exercicios/03_03.png)
![Lab AWS Lambda](exercicios/03_04.png)

## Apresentação do desafio

[Desafio](desafio/README.md)

## Evidências

[Arquivos do Desafio](desafio/)

Códigos do Script em Python:
![Evidencia 1](evidencias/01.png)<br>
![Evidencia 2](evidencias/02.png)<br>
![Evidencia 3](evidencias/03.png)<br>
![Evidencia 4](evidencias/04.png)<br>
![Evidencia 5](evidencias/05.png)<br>
![Evidencia 6](evidencias/06.png)<br>
![Evidencia 7](evidencias/07.png)<br>
![Evidencia 8](evidencias/08.png)<br>
![Evidencia 9](evidencias/09.png)

Código do arquivo Dockerfile
![Evidencia 10](evidencias/10.png)

Construindo a imagem
![Evidencia 11](evidencias/Exec_01.png)
![Evidencia 12](evidencias/Exec_02.png)

Executando e construindo um novo container com a imagem criada
![Evidencia 13](evidencias/Exec_03.png)
![Evidencia 14](evidencias/Exec_04.png)

Arquivos salvos no Bucket na AWS S3
![Evidencia 15](evidencias/Exec_05.png)
![Evidencia 16](evidencias/Exec_06.png)

Erro de credenciais não localizadas
![Evidencia 17](evidencias/Err_01.png)