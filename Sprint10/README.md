# Instruções

Nesta Sprint foi realizada a etapa final do desafio, que consiste em realizar a análise de dados com o Quicksight.<br>
Para realizar o desafio, foram visualizados tutoriais da AWS e cursos fornecidos pela trilha da Sprint 10.

## Resumo

**AWS Glue:** Utilizar o serviço para executar jobs de ETL

**AWS Quicksight:** Realizar análises, criando dashboard interativo com gráficos de diversos tipos

## Apresentação do desafio

[Desafio](desafio/README.md)

## Evidências

[Arquivos do Desafio](desafio/)
[Análise em PDF](desafio/Analise.pdf)

### Configuração do conjunto de dados no Quicksight

Conjunto de dados para análise de filmes configurado<br>
![Evidencia 1](evidencias/01.png)<br>

Joins configurados: dim_filme com fato_filme e dim_filme com dim_artista<br>
![Evidencia 2](evidencias/02.png)<br>
![Evidencia 3](evidencias/03.png)<br>

Conjunto de dados para séries configurado: fato_series com dim_titulo<br>
![Evidencia 4](evidencias/04.png)<br>
![Evidencia 5](evidencias/05.png)<br>

### Criando o dashboard
Cabeçalho com 2 campos para imagens e 1 para o tema da análise<br>
![Evidencia 6](evidencias/06.png)<br>

Gráfico dos 10 filmes com maiores médias de avaliação, com filtros e ação de filtro para detalhamento de votos<br>
![Evidencia 7](evidencias/07.png)<br>
![Evidencia 8](evidencias/08.png)<br>
![Evidencia 9](evidencias/09.png)<br>
![Evidencia 10](evidencias/10.png)<br>
![Evidencia 11](evidencias/11.png)<br>
![Evidencia 12](evidencias/12.png)<br>
![Evidencia 13](evidencias/13.png)<br>

Gráfico de linha para votação por ano de lançamento e número de filmes lançados por ano<br>
![Evidencia 14](evidencias/14.png)<br>

Gráfico de barras horizontais para nota média por ano de lançamento de séries (top 10)<br>
![Evidencia 15](evidencias/15.png)<br>
![Evidencia 16](evidencias/16.png)<br>

Gráfico de barras duplas para os 10 filmes com maiores lucros, considerando o período de 2013 a 2022<br>
![Evidencia 17](evidencias/17.png)<br>
![Evidencia 18](evidencias/18.png)<br>
![Evidencia 19](evidencias/19.png)<br>
![Evidencia 20](evidencias/20.png)<br>

Gráfico de barras horizontais comparando notas médias de filmes com duração maior ou menor que 120 minutos<br>
![Evidencia 21](evidencias/21.png)<br>
![Evidencia 22](evidencias/22.png)<br>

Gráfico de dispersão para analisar a relação entre orçamento e número de votos<br>
![Evidencia 23](evidencias/23.png)<br>
![Evidencia 24](evidencias/24.png)<br>

Gráfico de barras horizontais para desempenho dos filmes conforme a quantidade de profissões dos atores<br>
![Evidencia 25](evidencias/25.png)<br>
![Evidencia 26](evidencias/26.png)<br>

Gráfico de barras horizontais para desempenho de séries com até 2 anos de duração ou mais<br>
![Evidencia 27](evidencias/27.png)<br>
![Evidencia 28](evidencias/28.png)<br>
![Evidencia 29](evidencias/29.png)<br>

### Painel da análise

Painel publicado para interação e exportação em PDF<br>
![Evidencia 30](evidencias/30.png)<br>

Notas Médias por Ano de Filmes<br>
![Evidencia 31](evidencias/31.png)<br>  

Votação e Lançamentos por Ano de Filmes<br> 
![Evidencia 32](evidencias/32.png)<br>

Notas Médias por Ano de Séries<br>  
![Evidencia 33](evidencias/33.png)<br>

Lucro e Bilheteria de Filmes<br>  
![Evidencia 34](evidencias/34.png)<br>

Votos x Orçamento de Filmes<br>
![Evidencia 35](evidencias/35.png)  

Avaliação por Duração de Filmes<br>  
![Evidencia 36](evidencias/36.png)<br>

Avaliação por profissão dos Artistas de Filmes<br>  
![Evidencia 37](evidencias/37.png)<br> 

Avaliação por Duração de Séries<br>  
![Evidencia 38](evidencias/38.png)<br>

### Interação com os gráficos

Ao passar o mouse, é exibido o maior crescimento dos votos a partir de 1983<br>
![Evidencia 39](evidencias/39.png)<br>

Controle deslizante com a exibição de 5 milhões de votos, alterando a exibição de avaliações anuais<br>
![Evidencia 40](evidencias/40.png)<br>

Seleção de 2022 mostra votos e lançamentos desse ano<br>
![Evidencia 41](evidencias/41.png)<br>

Seleção do filme com maior lucro revela orçamento e número de votos no outro gráfico<br>
![Evidencia 42](evidencias/42.png)<br>
![Evidencia 43](evidencias/43.png)<br>

### Erros e problemas

Modelagem dimensional da sprint 9 refeita<br>
![Erro 01](evidencias/modelagem.png)<br>