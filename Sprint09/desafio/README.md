# Desafio
Esta é a 4ª etapa do desafio final. Nesta sprint foi realizada a modelagem dimensional e a limpeza dos dados, unindo os arquivos JSON contendo os dados originados da API do TMDB em conjunto com o arquivo CSV, advindos da camada TRUSTED.<br>
Foram criados 2 scripts para refinar e modelar os dados necessários para a futura análise: um para filmes e outro para séries. Os novos dados refinados e modelados foram salvos na camada REFINED no AWS S3.<br>
Posteriormente, foi executado 2 crawlers (um para filmes e outro para séries) para criar as tabelas nos bancos de dados respectivos.

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

### Modelagem dos dados

A primeira etapa do desafio consiste em fazer a modelagem dimensional dos dados, sendo uma para filme e outra para séries:<br>

1. Criação da modelagem para filmes, contendo as 2 tabelas para dimensão: **dim_filme** e **dim_artista** e 1 tabela fato: **fato_filmes**<br>
![Evidencia 1](../evidencias/modelagem_filmes.png)<br>

2. Criação da modelagem para séries, contendo 1 tabela para dimensão: **dim_titulo** e 1 tabela fato: **fato_series**<br>
![Evidencia 2](../evidencias/modelagem_series.png)<br>

### Script para filmes

Para obter apenas os dados necessários da camada TRUSTED, refiná-los e criar as tabelas para o modelo dimensional foi necessário a execução de um job no Glue. A seguir está o código necessário para a implementação:<br>

3. O script é iniciado com a importação das bibliotecas, variáveis de ambiente e definição de parâmetros para executar o Glue<br>
![Evidencia 3](../evidencias/01.png) <br>

4. Definição das variáveis que contém o caminho dos arquivos na camada Trusted<br>
![Evidencia 4](../evidencias/02.png)<br>

5. Definição da variável que contém o caminho para a saída dos arquivos no S3<br>
![Evidencia 5](../evidencias/03.png)<br>

6. Nesta primeira parte do código são juntados os arquivos CSV e JSON e selecionadas as colunas necessárias para a futura análise.
Nesta parte do código são lidos os arquivos parquet do CSV e dos JSONs e armazenados em uma lista<br>
![Evidencia 6](../evidencias/04.png)<br>

7. Há uma coluna com o nome errado, então esta é renomeada<br>
![Evidencia 7](../evidencias/05.png)<br>

8. São selecionadas apenas as colunas necessárias do CSV para a futura análise. A coluna 'id' é renomeada para 'id_filme' para melhor identificação<br>
![Evidencia 8](../evidencias/06.png)<br>

9. Apenas as colunas necessárias para análise são selecionadas dos arquivos JSON. A coluna 'id_IMDB' é renomeada para 'id_filme' para corresponder às IDs do CSV no momento de unir os arquivos<br>
![Evidencia 9](../evidencias/07.png)<br>

10. Padronização dos atributos da coluna 'genero' em minúsculas e filtragem pelos gêneros **animação** ou **comédia**<br>
Obs: Os gêneros estão em inglês na fonte de dados<br>
![Evidencia 10](../evidencias/08.png)<br>

11. Junção dos dataframes que contém os dados em CSV e os JSONs, relacionando com as ids dos filmes<br>
![Evidencia 11](../evidencias/09.png)<br>

12. Nesta segunda parte do código são executados comandos para criar os dados conforme modelo dimensional. São selecionadas as colunas
necessárias e convertidas para os tipos de dados requeridos<br>
![Evidencia 12](../evidencias/10.png)<br>

13. Aqui é criada uma coluna 'id_artista' no dataframe para relacionar os nomes dos artistas e suas profissões à uma ID única gerada pelo Spark<br>
![Evidencia 13](../evidencias/11.png)<br>

14. Criação dos dataframes para criar as dimensões: filmes e artistas, contendo os respectivos campos necessários e eliminação de linhas duplicadas<br>
![Evidencia 14](../evidencias/12.png)<br>

15. Criação do dataframe para criar a tabela fato de filmes, contendo os campos necessários e a ligação com as ids de artistas, vindo da tabela dimensional de artistas<br>
![Evidencia 15](../evidencias/13.png)<br>

16. Conversão dos dataframes do spark para o dynamic frame do Glue<br> 
![Evidencia 16](../evidencias/14.png)<br>

17. Armazenamento dos arquivos parquet, de cada dataframe, no caminho especificado no S3 e finalização do job<br>
![Evidencia 17](../evidencias/15.png)<br>

### Script para séries

O script para refinar os dados de séries é mais simplificado, pois para esta análise não há dados do TMDB para serem unificados com os dados
já fornecidos. A modelagem também é simplificada, com apenas 2 tabelas.<br>

18. O script é iniciado com a importação das bibliotecas, variáveis de ambiente e definição de parâmetros para executar o Glue<br>
![Evidencia 18](../evidencias/16.png)<br>

19. Definição das variáveis que contém o caminho de entrada do arquivo CSV que está na TRUSTED, e o caminho de saída para REFINED<br>
![Evidencia 19](../evidencias/17.png)<br>

20. Leitura dos dados CSV que estão em formato parquet<br>
![Evidencia 20](../evidencias/18.png)<br>

21. Correção do nome da coluna 'TituloPrincipal', renomeando-a<br>
![Evidencia 21](../evidencias/19.png)<br>

22. Seleção das colunas necessárias para a análise dos dados e renomeação da coluna 'id' para 'id_serie'<br>
![Evidencia 22](../evidencias/20.png)<br>

23. Padronização dos atributos da coluna 'genero' em minúsculas e filtragem pelos gêneros **animação** ou **comédia**<br>
![Evidencia 23](../evidencias/21.png)<br>

24. Seleção das colunas necessárias e conversão para os tipos de dados requeridos<br>
![Evidencia 24](../evidencias/22.png)<br>

25. Criação da tabela dimensão título, contendo os campos requeridos e eliminação de linhas duplicadas<br>
![Evidencia 25](../evidencias/23.png)<br>

26. Criação da tabela fato series, contendo os campos requeridos e eliminação de linhas duplicadas<br>
![Evidencia 26](../evidencias/24.png)<br>

27. Conversão dos dataframes do spark para o dynamic frame do Glue<br> 
![Evidencia 27](../evidencias/25.png)<br> 

28. Armazenamento dos arquivos parquet, de cada dataframe, no caminho especificado no S3 e finalização do job<br>
![Evidencia 28](../evidencias/26.png)<br> 

### Execução dos jobs no Glue

**Script para filmes**

29. O código digitado localmente no VSCode é colado no espaço de script do AWS Glue para poder executar o job que é nomeado como: modelagem_filmes<br>
![Evidencia 29](../evidencias/27.png)<br>

30. Configurações são definidas para o job, como: IAM Role, worker type, número de workers, e o timeout do job<br>
![Evidencia 30](../evidencias/28.png)<br>
![Evidencia 31](../evidencias/29.png)<br>
![Evidencia 32](../evidencias/30.png)<br>

31. Em job parameters, são definidas as variáveis locais para os caminhos de entrada dos arquivos necessários para o script e o caminho de
saída dos arquivos parquet. Após todas as configurações definidas, o job é salvo e executado<br>
![Evidencia 33](../evidencias/31.png)<br>

32. Após a execução do job, o console exibe se a execução foi bem sucedida e os arquivos são armazenados no local especificado no S3<br>
![Evidencia 34](../evidencias/32.png)<br>
![Evidencia 35](../evidencias/33.png)<br>
![Evidencia 36](../evidencias/34.png)<br>
![Evidencia 37](../evidencias/35.png)<br>

**Script para series**

33. O código digitado localmente no VSCode é colado no espaço de script do AWS Glue para poder executar o job que é nomeado como: modelagem_series<br>
![Evidencia 38](../evidencias/36.png)<br>

34. Configurações são definidas para o job, como: IAM Role, worker type, número de workers, e o timeout do job<br>
![Evidencia 39](../evidencias/37.png)<br>
![Evidencia 40](../evidencias/38.png)<br>
![Evidencia 41](../evidencias/39.png)<br>

35. Em job parameters, são definidas as variáveis locais para o caminho de entrada dos arquivos necessários para o script e o caminho de
saída dos arquivos parquet. Após todas as configurações definidas, o job é salvo e executado<br>
![Evidencia 42](../evidencias/40.png)<br>

36. Após a execução do job, o console exibe se a execução foi bem sucedida e os arquivos são armazenados no local especificado no S3<br>
![Evidencia 43](../evidencias/41.png)<br>
![Evidencia 44](../evidencias/42.png)<br>
![Evidencia 45](../evidencias/43.png)<br>

### Criando catálogo de dados

**Para filmes**

37. Um banco de dados é criado com o nome: modelagem_filmes<br>
![Evidencia 46](../evidencias/44.png)<br>

38. Após a criação do banco de dados, é criado um crawler com o caminho especificado dos dados. Então as 3 tabelas são criadas a partir dos dados fornecidos<br>
![Evidencia 47](../evidencias/45.png)<br>

39. Ao clicar em 'Table data' de cada tabela, como pode-se ver no print do passo 37, o Athena é aberto com uma consulta simples para exibir os dados das 3 tabelas. Abaixo encontram-se respectivamente: dim_artista, dim_filme e fato_filmes<br>
![Evidencia 48](../evidencias/46.png)<br>
![Evidencia 49](../evidencias/47.png)<br>
![Evidencia 50](../evidencias/48.png)<br>

**Para séries**

40. Um banco de dados é criado com o nome: modelagem-series<br>
![Evidencia 51](../evidencias/49.png)<br>

41. Após a criação do banco de dados, é criado um crawler com o caminho especificado dos dados. Então as 2 tabelas são criadas a partir dos dados fornecidos<br>
![Evidencia 52](../evidencias/50.png)<br>

42. Ao clicar em 'Table data' de cada tabela, como pode-se ver no print do passo 40, o Athena é aberto com uma consulta simples para exibir os dados das 2 tabelas. Abaixo encontram-se respectivamente: dim_titulo e fato_series<br>
![Evidencia 53](../evidencias/51.png)<br>
![Evidencia 54](../evidencias/52.png)<br>

## Erros e problemas

Ocorreram alguns problemas na execução dos jobs no Glue por erros simples de digitação, tais como atribuições de variáveis, caminhos dos arquivos, entre outros que foram prontamente corrigidos

1. Ao executar o primeiro job no Glue houve um erro de digitação no script ao nomear incorretamente a variável do dataframe que continha os filmes<br>
![Erro 01](../evidencias/Err_1.png)<br>

2. Um erro foi gerado ao não definir corretamente os caminhos de entrada dos arquivos CSV e JSONs<br>
![Erro 02](../evidencias/Err_2.png)<br>

3. Ao reexecutar um job para sobreescrever os dados que estavam incorretos no S3, um erro foi apresentado por não ter definido a política de exclusão de arquivos do S3 no IAM<br>
![Erro 03](../evidencias/Err_3.png)<br>

4. Houve um erro de sintaxe na digitação do script para a modelagem de series, ao não colocar ',' após as colunas desejadas para o dataframe<br>
![Erro 04](../evidencias/Err_4.png)<br>