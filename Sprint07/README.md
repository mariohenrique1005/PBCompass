# Instruções

Nesta Sprint foi realizada a segunda etapa do desafio final: obter novos dados na API do TMDB para realizar a futura análise de dados. Também foram executados exercícios para a prática dos serviços AWS.<br>

## Resumo

**AWS Glue:** Como utilizar o serviço para executar jobs

**AWS Lambda:** Como configurar, criar e executar funções

**Apache Spark:** Como utilizá-lo e executar suas funções

# Exercícios

[Pasta Exercicios](exercicios/)

Exercício 1 - Apache Spark
![Apache Spark](exercicios/Exercicio01/01.png)
![Apache Spark](exercicios/Exercicio01/02.png)
![Apache Spark](exercicios/Exercicio01/03.png)
![Apache Spark](exercicios/Exercicio01/04.png)
![Apache Spark](exercicios/Exercicio01/05.png)
![Apache Spark](exercicios/Exercicio01/06.png)

Exercicio 2 - TMDB<br>
[Código](exercicios/Exercicio02/Ex2.py)
![TMDB](exercicios/Exercicio02/01.png)

Exercicio 3 - Lab AWS Glue

[Código](exercicios/Exercicio02/Ex3.py)<br>
[Saída](exercicios/Exercicio02/Saida.csv)
![Lab AWS Glue](exercicios/Exercicio03/01.png)
![Lab AWS Glue](exercicios/Exercicio03/02.png)
![Lab AWS Glue](exercicios/Exercicio03/03.png)
![Lab AWS Glue](exercicios/Exercicio03/04.png)
![Lab AWS Glue](exercicios/Exercicio03/05.png)
![Lab AWS Glue](exercicios/Exercicio03/06.png)
![Lab AWS Glue](exercicios/Exercicio03/07.png)
![Lab AWS Glue](exercicios/Exercicio03/08.png)
![Lab AWS Glue](exercicios/Exercicio03/09.png)
![Lab AWS Glue](exercicios/Exercicio03/10.png)
![Lab AWS Glue](exercicios/Exercicio03/11.png)
![Lab AWS Glue](exercicios/Exercicio03/12.png)

## Apresentação do desafio

[Desafio](desafio/README.md)

## Evidências

[Arquivos do Desafio](desafio/)

Testes no Google Collab
![Evidencia 1](evidencias/01.png)

Script para obter dados dos filmes
![Evidencia 2](evidencias/02.png)
![Evidencia 3](evidencias/03.png)

Teste de obtenção de dados
![Evidencia 4](evidencias/04.png)

Primeira parte do código
![Evidencia 5](evidencias/05.png)

Função que processa os dados do CSV armazenado no serviço S3
![Evidencia 6](evidencias/06.png)

Função assíncrona, que busca a ID do filme no TMDB, a partir da ID constante no IMDB
![Evidencia 7](evidencias/07.png)

Função para buscar as informações requeridas dos filmes 
![Evidencia 8](evidencias/08.png)

Função que divide os dados em lotes menores
![Evidencia 9](evidencias/09.png)

Função para salvar os arquivos no bucket
![Evidencia 10](evidencias/10.png)

Função principal, que chama as outras funções auxiliares
![Evidencia 11](evidencias/11.png)

Função lambda_handler
![Evidencia 12](evidencias/12.png)

Dockerfile para criação de arquivos de bibliotecas
![Evidencia 13](evidencias/13.png)

Arquivos gerados pelo container
![Evidencia 14](evidencias/14.png)
![Evidencia 15](evidencias/15.png)

Criação da camada
![Evidencia 16](evidencias/16.png)

Permissão no IAM de acesso de leitura e escrita no Bucket definido
![Evidencia 17](evidencias/17.png)

Configurações da função Lambda
![Evidencia 18](evidencias/18.png)
![Evidencia 19](evidencias/19.png)
![Evidencia 20](evidencias/20.png)

Mensagem de sucesso após execução no Lambda
![Evidencia 21](evidencias/21.png)

Arquivos salvos no Bucket
![Evidencia 22](evidencias/22.png)

Erro de carregamento de ID do CSV
![Erro 01](evidencias/Err_01.png)

Erro de ID não encontrada
![Erro 02](evidencias/Err_02.png)