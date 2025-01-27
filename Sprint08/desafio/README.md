# Desafio
Este desafio consiste de realizar a 3ª etapa do desafio final, limpar os dados oriundos da camada RAW para a camada TRUSTED.<br>
Para isso foram criados 2 scripts: 1 para tratar os dados referentes aos CSVs locais: movies e series, e outro script para os dados adquiridos da API do TMDB.<br>
A execução dos scripts foram feitos através do AWS Glue e posteriormente foi criado um banco de dados no Crawler

## Etapas

### Tema do desafio a ser respondido

**Análise de métricas dos filmes e séries e o impacto destas nas notas de avaliação e arrecadação de bilheteria**

Questionamentos:<br>
1- Qual foi o ano de lançamento em que os filmes tiveram a maior nota média?<br>
2- Qual foi o ano de lançamento em que as séries tiveram a maior nota média?<br>
3- Qual ator teve o filme com a maior nota média?<br>
4- O ator que teve o filme com a maior nota média atuou em quais filmes? Quais foram as notas desses filmes?<br>
5- Os filmes que tem mais de 120 minutos de duração tem nota média maior que os filmes menores de 120 minutos?<br>
6- As series com mais de 2 anos de duração possuem nota média maior que as séries que tem 2 anos ou menos de duração?<br>
7- Quais foram os 10 filmes com maior arrecadação de bilheteria e a sua lucratividade em relação ao orçamento no últimos 10 anos?<br>
8- Os filmes com mais votos dos últimos 10 anos tem maior orçamento em comparação com outros?

### Criando o código para os dados dos CSVs movies e series

1. Primeiramente todos os códigos foram desenvolvidos na ambiente local (VSCode), para depois serem colocados no AWS Glue. Nesta etapa é feita a importação das bibliotecas necessárias para executar o código
![Evidencia 1](../evidencias/01.png)<br>

2. São definidos os parâmetros para execução correta do script, entre eles: Caminhos de entrada dos arquivos e o caminho de saída para os arquivos no formato parquet
![Evidencia 2](../evidencias/02.png)<br>

3. Os caminhos para os arquivos são armazenados em variáveis e após é impresso o caminho de entrada para movies e series
![Evidencia 3](../evidencias/03.png)<br>

4. Função para verificar o número de colunas no dataframe e remover as linhas nulas
![Evidencia 4](../evidencias/04.png)<br>

5. Variável para armazenar a leitura do csv movies, contendo os parâmetros necessários
![Evidencia 5](../evidencias/05.png)<br>

6. Conversão do dataframe movies para um dataframe do spark e realizar os procedimentos necessários
![Evidencia 6](../evidencias/06.png)<br>

7. Contagem do número de colunas no dataframe e chamada da função para fazer a limpeza no dataframe
![Evidencia 7](../evidencias/07.png)<br>

8. Conversão de volta para o DynamicFrame, para ser convertido para o formato parquet
![Evidencia 8](../evidencias/08.png)<br>

9. Conversão dos dados para o formato parquet, contendo todos os parâmetros necessários
![Evidencia 9](../evidencias/09.png)<br>

10. Variável para armazenar a leitura do csv series, contendo os parâmetros necessários
![Evidencia 10](../evidencias/10.png)<br>

11. Conversão do dataframe series para um dataframe do spark e realizar os procedimentos necessários
![Evidencia 11](../evidencias/11.png)<br>

12. Contagem do número de colunas no dataframe e chamada da função para fazer a limpeza no dataframe
![Evidencia 12](../evidencias/12.png)<br>

13. Conversão de volta para o DynamicFrame, para ser convertido para o formato parquet
![Evidencia 13](../evidencias/13.png)<br>

14. Conversão dos dados para o formato parquet, contendo todos os parâmetros necessários
![Evidencia 14](../evidencias/14.png)<br>

### Criando o código para os dados JSON vindos do TMDB

15. Importação das bibliotecas para executar o script no AWS Glue<br>
![Evidencia 15](../evidencias/15.png)<br>

16. Definição dos parâmetros para iniciar o job<br>
![Evidencia 16](../evidencias/16.png)<br>

17. Definição dos caminhos de entrada e saída dos arquivos<br>
![Evidencia 17](../evidencias/17.png)<br>

18. Leitura dos arquivos JSON, de origem da API do TMDB. Armazenamento em um dynamic dataframe<br>
![Evidencia 18](../evidencias/18.png)<br>

19. Transforma o dynamic dataframe para um dataframe comum, para que possam ser feitos outros procedimentos<br>
![Evidencia 19](../evidencias/19.png)<br>

20. Remoção dos registros com valores nulos e duplicados<br>
![Evidencia 20](../evidencias/20.png)<br>

21. Transforma o dataframe que teve os dados tratados no formato parquet<br>
![Evidencia 21](../evidencias/21.png)<br>

### Configurações na AWS

22. Utilização do AWS IAM para configurar o acesso de leitura e escrita no bucket para o job dos CSVs locais
![Evidencia 22](../evidencias/22.png)

23. Configuração do Job para os arquivos CSV locais: movies e series, contendo a função correta para o IAM ter acesso ao bucket
![Evidencia 23](../evidencias/23.png)

24. Definição das configurações do Job a serem utilizados, tais como versão do Glue, linguagem a ser utilizada, CPU e RAM
![Evidencia 24](../evidencias/24.png)

25. Definição das variáveis a serem utilizadas, sendo as entradas e saídas para os arquivos movies e series
![Evidencia 25](../evidencias/25.png)

26. Utilização do AWS IAM para configurar o acesso de leitura e escrita no bucket para o job dos json originados da API do TMDB
![Evidencia 26](../evidencias/26.png)

27. Definição das configurações do Job a serem utilizados, tais como versão do Glue, linguagem a ser utilizada, CPU e RAM
![Evidencia 27](../evidencias/27.png)

28. Definição das variáveis a serem utilizadas para a entrada e saída dos arquivos JSON
![Evidencia 28](../evidencias/28.png)

### Execução bem sucedida

29. Execução bem sucedida para o job de processamento dos CSVs
![Evidencia 29](../evidencias/29.png)

30. Execução bem sucedida para o job de processamento dos JSONs
![Evidencia 30](../evidencias/30.png)

31. Arquivos parquet para movies armazenados corretamente dentro do bucket 
![Evidencia 31](../evidencias/31.png)

32. Arquivos parquet para series armazenados corretamente dentro do bucket 
![Evidencia 32](../evidencias/32.png)

33. Arquivo parquet para os JSONs armazenado corretamente dentro do bucket 
![Evidencia 33](../evidencias/33.png)

### Criando um Data Catalog

34. Para criar um data catalog, é necessário criar um crawler, que foi identificado como: **desafio-sprint08** 
e conter o caminho para a criação da base de dados, que são os caminhos para os arquivos parquet de movies, 
series e os obtidos a partir do TMDB.
No print a seguir é possível ver que o serviço foi executado com sucesso
![Evidencia 34](../evidencias/34.png)

35. Através do Amazon Athena é possível realizar uma consulta simples para visualizar os dados dos 3 arquivos mencionados acima:
![Evidencia 35](../evidencias/35.png)
![Evidencia 36](../evidencias/36.png)
![Evidencia 37](../evidencias/37.png)

## Erros e problemas

Houveram alguns erros durante as execuções do script para processar os arquivos CSV, como pode-se ver a seguir

1. Através do log de erros no Cloudwatch, é possível ver que houve um erro ao tentar gravar
no bucket especificado. Posteriormente isso foi corrigido alterando as permissões do IAM
![Erro 01](../evidencias/Err_01.png)

2. Houveram erros na função de contagem de colunas pelo spark. Posteriormente o código foi adaptado e a execução foi bem sucedida
![Erro 02](../evidencias/Err_02.png)
![Erro 03](../evidencias/Err_03.png)