# Instruções

Nesta Sprint foram realizados alguns exercícios no Python e no Spark, com operações referentes a consulta e inserção de dados em dataframes utilizando o Spark SQL. <br>
Também foi executada a terceira parte do desafio, tratando os dados da camada RAW e enviando-os para a camada TRUSTED, convertendo e limpando os arquivos para o formato parquet.

## Resumo

**AWS Glue:** Utilizar o serviço para executar jobs e criar catálogos de dados

**Amazon Athena:** Consultar dados a partir do catálogo criado

**Apache Spark:** Executar funções de consulta e inserção de dados

**Python:** Executar scripts para criar arquivos de dados

# Exercícios

[Pasta Exercicios](exercicios/)

Exercício 1 - Geração e massa de dados. Dividido em 3 etapas, entre as quais:

Etapa 1 - Criação de uma lista de 250 números aleatórios<br>
[Código](exercicios/Exercicio01/Etapa1.py)
![Print 01](exercicios/Exercicio01/Etapa1.png)

Etapa 2 - Criação de uma lista contendo 20 animais e geração de um arquivo CSV contendo estes<br>
[Código](exercicios/Exercicio01/Etapa2.py)<br>
[Arquivo](exercicios/Exercicio01/animais.csv)<br>
![Print 02](exercicios/Exercicio01/Etapa2.png)

Etapa 3 - Criação de um arquivo txt contendo 10 milhões de nomes aleatórios<br>
[Código](exercicios/Exercicio01/Etapa3.py)
![Print 03](exercicios/Exercicio01/Etapa3.png)
O arquivo era pesado para ser carregado no Github (140 MB), então um print do arquivo local foi gerado:
![Print 04](exercicios/Exercicio01/Etapa3-nomes_aleatorios.png)

Exercicio 2 - Apache Spark. Utilização do Spark para inserir e consultar dados em dataframe<br>
[Código](exercicios/Exercicio02/Exercicio02.ipynb)
![Print 01](exercicios/Exercicio02/01.png)
![Print 02](exercicios/Exercicio02/02.png)
![Print 03](exercicios/Exercicio02/03.png)
![Print 04](exercicios/Exercicio02/04.png)
![Print 05](exercicios/Exercicio02/05.png)
![Print 06](exercicios/Exercicio02/06.png)
![Print 07](exercicios/Exercicio02/07.png)
![Print 08](exercicios/Exercicio02/08.png)
![Print 09](exercicios/Exercicio02/09.png)
![Print 10](exercicios/Exercicio02/10.png)
![Print 11](exercicios/Exercicio02/11.png)
![Print 12](exercicios/Exercicio02/12.png)
![Print 13](exercicios/Exercicio02/13.png)

Exercicio 3 - Exercício TMDB. Obtenção de dados a partir da API do TMDB<br>

[Código](exercicios/Exercicio03/Exercicio03.py)<br>
![Print 01](exercicios/Exercicio03/01.png)


## Apresentação do desafio

[Desafio](desafio/README.md)

## Evidências

[Arquivos do Desafio](desafio/)

Importação das bibliotecas necessárias para executar o código de processamento dos CSVs
![Evidencia 1](evidencias/01.png)<br>

Parâmetros para execução correta do script, incluindo os paths
![Evidencia 2](evidencias/02.png)<br>

Definição dos paths de entrada e saída<br>
![Evidencia 3](evidencias/03.png)<br>

Função para limpar inconsistências no dataframe
![Evidencia 4](evidencias/04.png)<br>

Parâmetros para ler o CSV do arquivo movies<br>
![Evidencia 5](evidencias/05.png)<br>

Conversão para um dataframe do Spark<br>
![Evidencia 6](evidencias/06.png)<br>

Contagem do número de colunas no dataframe e chamada da função
![Evidencia 7](evidencias/07.png)<br>

Conversão do dataframe movies para dynamic dataframe
![Evidencia 8](evidencias/08.png)<br>

Conversão de movies para o formato parquet<br>
![Evidencia 9](evidencias/09.png)<br>

Parâmetros para ler o CSV do arquivo series<br>
![Evidencia 10](evidencias/10.png)<br>

Conversão para um dataframe do Spark<br>
![Evidencia 11](evidencias/11.png)<br>

Contagem do número de colunas no dataframe e chamada da função
![Evidencia 12](evidencias/12.png)<br>

Conversão do dataframe series para dynamic dataframe
![Evidencia 13](evidencias/13.png)<br>

Conversão de series para o formato parquet e fim do job<br>
![Evidencia 14](evidencias/14.png)<br>

Importação das bibliotecas necessárias para executar o código de processamento dos JSONs
![Evidencia 15](evidencias/15.png)<br>

Parâmetros para execução correta do script, incluindo os paths
![Evidencia 16](evidencias/16.png)<br>

Definição dos paths de entrada e saída<br>
![Evidencia 17](evidencias/17.png)<br>

Parâmetros para ler os arquivos JSON<br>
![Evidencia 18](evidencias/18.png)<br>

Conversão para um dataframe do spark<br>
![Evidencia 19](evidencias/19.png)<br>

Remoção dos registros com valores duplicados e nulos<br>
![Evidencia 20](evidencias/20.png)<br>

Conversão para o formato parquet<br>
![Evidencia 21](evidencias/21.png)<br>

Configuração do IAM
![Evidencia 22](evidencias/22.png)<br>

Configuração do IAM no job Glue para processamento dos CSVs
![Evidencia 23](evidencias/23.png)<br>

Detalhes da configuração do job Glue 
![Evidencia 24](evidencias/24.png)<br>

Definição das variáveis para o job
![Evidencia 25](evidencias/25.png)<br>

Configuração do IAM no job Glue para processamento dos JSONs
![Evidencia 26](evidencias/26.png)<br>

Detalhes da configuração do job Glue 
![Evidencia 27](evidencias/27.png)<br>

Definição das variáveis para o job
![Evidencia 28](evidencias/28.png)<br>

Execução bem sucedida para o job de processamento dos CSVs
![Evidencia 29](evidencias/29.png)<br>

Execução bem sucedida para o job de processamento dos JSONs
![Evidencia 30](evidencias/30.png)<br>

Arquivos parquet no bucket para o CSV Movies
![Evidencia 31](evidencias/31.png)<br>

Arquivos parquet no bucket para o CSV Series
![Evidencia 32](evidencias/32.png)<br>

Arquivo parquet no bucket para os JSONs
![Evidencia 33](evidencias/33.png)<br>

Criação do catálogo de dados com o Crawler
![Evidencia 34](evidencias/34.png)<br>

Dados visualizados no Amazon Athena para movies, series e os JSONs do TMDB
![Evidencia 35](evidencias/35.png)
![Evidencia 36](evidencias/36.png)
![Evidencia 37](evidencias/37.png)

Log de erro ao tentar gravar no bucket especificado
![Erro 01](evidencias/Err_01.png)

Log de erros na função de contagem de colunas pelo spark
![Erro 02](evidencias/Err_02.png)
![Erro 03](evidencias/Err_03.png)