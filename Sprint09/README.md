# Instruções

Nesta Sprint foi realizada a 4ª etapa do desafio final, que consistiu em unir arquivos, limpar dados e criar o modelo dimensional necessário para a análise futura. <br>

## Resumo

**AWS Glue:** Executar jobs para unir e limpar dados, gerar arquivos

**AWS Glue Data Catalog:** Executar Crawler, criar tabelas

**AWS Athena:** Realizar consultas para visualizar dados

## Apresentação do desafio

[Desafio](desafio/README.md)

## Evidências

[Arquivos do Desafio](desafio/)

Modelagem para filmes<br>
![Evidencia 1](evidencias/modelagem_filmes.png)<br>

Modelagem para séries<br>
![Evidencia 2](evidencias/modelagem_series.png)<br>

Inicialização do script para modelagem de filmes<br>
![Evidencia 3](evidencias/01.png)<br>

Variáveis que contém o caminho dos arquivos na camada Trusted<br>
![Evidencia 4](evidencias/02.png)<br>

Variável que contém o caminho para a saída dos arquivos no S3<br>
![Evidencia 5](evidencias/03.png)<br>

Leitura dos arquivos parquet do CSV e dos JSONs<br>
![Evidencia 6](evidencias/04.png)<br>

Renomeação da coluna TituloPrincipal <br>
![Evidencia 7](evidencias/05.png)<br>

Coluna 'id' é renomeada para 'id_filme' para melhor identificação<br>
![Evidencia 8](evidencias/06.png)<br>

Seleção das colunas necessárias com origem nos JSONs<br>
![Evidencia 9](evidencias/07.png)<br>

Seleção dos gêneros requeridos<br>
![Evidencia 10](evidencias/08.png)<br>

Junção dos dataframes<br>
![Evidencia 11](evidencias/09.png)<br>

Seleção das colunas necessárias e conversão de tipos de dados<br>
![Evidencia 12](evidencias/10.png)<br>

Criação de uma coluna de id para artistas<br>
![Evidencia 13](evidencias/11.png)<br>

Criação de dataframes para as dimensões<br>
![Evidencia 14](evidencias/12.png)<br>

Criação de dataframe para a fato<br>
![Evidencia 15](evidencias/13.png)<br>

Conversão de dataframe spark para dynamic frame do Glue<br>
![Evidencia 16](evidencias/14.png)<br>

Salvamento dos dados em parquet no S3<br>
![Evidencia 17](evidencias/15.png)<br>

Inicialização do script para modelagem de series<br>
![Evidencia 18](evidencias/16.png)<br>

Definição dos caminhos de entrada e saída<br>
![Evidencia 19](evidencias/17.png)<br>

Leitura do arquivo csv <br>
![Evidencia 20](evidencias/18.png)<br>

Renomeação da coluna TituloPrincipal <br>
![Evidencia 21](evidencias/19.png)<br>

Seleção das colunas necessárias do CSV<br>
![Evidencia 22](evidencias/20.png)<br>

Seleção dos gêneros requeridos<br>
![Evidencia 23](evidencias/21.png)<br>

Seleção e conversão de tipos de dados<br>
![Evidencia 24](evidencias/22.png)<br>

Criação do dataframe para a dimensão título<br>
![Evidencia 25](evidencias/23.png)<br>

Criação do dataframe para a tabela fato<br>
![Evidencia 26](evidencias/24.png)<br>

Conversão de dataframe spark para dynamic frame do Glue<br>
![Evidencia 27](evidencias/25.png)<br>

Salvamento dos dados em parquet no S3<br>
![Evidencia 28](evidencias/26.png)<br>

Script para o job de modelagem dos filmes<br>
![Evidencia 29](evidencias/27.png)<br>

Configurações para o job<br>
![Evidencia 30](evidencias/28.png)<br>
![Evidencia 31](evidencias/29.png)<br>
![Evidencia 32](evidencias/30.png)<br>

Definição dos paths de entrada e saída<br>
![Evidencia 33](evidencias/31.png)<br>

Execução bem sucedida do job de modelagem dos filmes<br>
![Evidencia 34](evidencias/32.png)<br>

Arquivos salvos no S3 no local especificado<br>
![Evidencia 35](evidencias/33.png)<br>
![Evidencia 36](evidencias/34.png)<br>
![Evidencia 37](evidencias/35.png)<br>

Script para o job de modelagem das series<br>
![Evidencia 38](evidencias/36.png)<br>

Configurações para o job<br>
![Evidencia 39](evidencias/37.png)<br>
![Evidencia 40](evidencias/38.png)<br>
![Evidencia 41](evidencias/39.png)<br>

Definição dos paths de entrada e saída<br>
![Evidencia 42](evidencias/40.png)<br>

Execução bem sucedida do job de modelagem das series<br>
![Evidencia 43](evidencias/41.png)<br>

Arquivos salvos no S3 no local especificado<br>
![Evidencia 44](evidencias/42.png)<br>
![Evidencia 45](evidencias/43.png)<br>

Criação do banco de dados para a modelagem de filmes<br>
![Evidencia 46](evidencias/44.png)<br>

Crawler para criar as tabelas<br>
![Evidencia 47](evidencias/45.png)<br>

Visualização das tabelas no Athena<br>
![Evidencia 48](evidencias/46.png)<br>
![Evidencia 49](evidencias/47.png)<br>
![Evidencia 50](evidencias/48.png)<br>

Criação do banco de dados para a modelagem de series<br>
![Evidencia 51](evidencias/49.png)<br>

Crawler para criar as tabelas<br>
![Evidencia 52](evidencias/50.png)<br>

Visualização das tabelas no Athena<br>
![Evidencia 53](evidencias/51.png)<br>
![Evidencia 54](evidencias/52.png)<br>

Erro de digitação no script ao nomear incorretamente a variável do dataframe<br>
![Erro 01](evidencias/Err_1.png)<br>

Erro ao não definir corretamente os caminhos de entrada dos arquivos<br>
![Erro 02](evidencias/Err_2.png)<br>

Erro ao sobrescrever dados no S3<br>
![Erro 03](evidencias/Err_3.png)<br>

Erro de sintaxe no script<br>
![Erro 04](evidencias/Err_4.png)<br>