# Instruções

Nesta Sprint foi realizado o desafio de criar um script em Python para analisar uma base de dados e enviar os arquivos e fazer o download de uma base de dados a partir do serviço em nuvem: AWS S3. O desafio consistiu nas seguintes etapas:<br>

1. Escolha da base de dados no site do governo brasileiro: http://dados.gov.br<br>
2. Construção do script para analisar os dados do database em CSV. Foi utilizado em um primeiro momento o Google Colab em conjunto com a biblioteca **Pandas** e depois este arquivo foi exportado como .py para o VScode<br>
3. Construção do script para criar um bucket no S3 e fazer o upload da base de dados<br>
4. Configuração das variáveis para ter acesso às credenciais da conta AWS

## Resumo

**Python:** Aprendi mais funções da linguagem, como realizar importações de script e utilizar as bibliotecas: OS e Boto3

**AWS S3:** Como utilizar os serviços em nuvem para armazenamento de arquivos

**AWS EC2:** Como criar e configurar instâncias

**AWS Dynamo DB**: Como configurar bancos de dados NOSQL

**IAM**: Como gerenciar usuários e grupos de usuários

# Certificados

Certificados do Curso de AWS:
[Certificado AWS 1](certificados/aws-cloud-quest-cloud-practitioner.png)<br>
Link para a badge: https://www.credly.com/badges/3764c6fe-d862-4342-81df-e12aaf0f66cb/public_url

# Exercícios

[Pasta Exercicios](exercicios/)

Link para o endpoint do bucket: http://exercicio-1.s3-website-us-east-1.amazonaws.com

Arquivos inseridos no bucket:
![Arquivos no bucket](exercicios/Arquivos_bucket.png/)

Execução da página index.html:
![Execução](exercicios/Execucao_bucket.png/)

Instância no EC2 em execução:
![Instância](exercicios/Instancia_execucao.png)

## Apresentação do desafio

[Desafio](desafio/README.md)


## Evidências

Database no Excel
![Database no Excel](evidencias/Database.png)

Salvamento e visualização do dataframe
![Evidencia 1](evidencias/01.png)

Renomeação das colunas do dataframe
![Evidencia 2](evidencias/02.png) 

Renomeação dos dados da coluna 'Descrição da conta'
![Evidencia 3](evidencias/03.png)

Substituição de ',' por '.' e conversão dos valores das colunas
![Evidencia 4](evidencias/04.png)

Remoção dos espaços em vazio na coluna 'Descrição da conta'
![Evidencia 5](evidencias/05.png)

Verificação de valores nulos ou duplicados
![Evidencia 6](evidencias/06.png)

Verificação dos maiores e menores valores
![Evidencia 7](evidencias/07.png)

Verificação de quais valores são maiores que 0 e menores que 1 milhão 
![Evidencia 8](evidencias/08.png)

Classificação do dataframe por data
![Evidencia 9](evidencias/09.png)

Formatando a visualização dos números
![Evidencia 10](evidencias/10.png)

Divisão dos valores por 1 milhão
![Evidencia 11](evidencias/11.png)

Verificação do maior e menor valor positivo
![Evidencia 12](evidencias/12.png)

Verificação dos valores únicos das contas e suas respectivas descrições
![Evidencia 13](evidencias/13.png)

Verificação de quais descrições de contas possuem mais de um valor atribuido para 'conta'
![Evidencia 14](evidencias/14.png)

Função de conversão de valores na coluna 'Origem'
![Evidencia 15](evidencias/15.png)

Cláusula que filtra dados usando ao menos dois operadores lógicos
![Evidencia 16](evidencias/16.png)

Primeira função de agregação (group by) e somar os valores da conta '87-3' por ano
![Evidencia 17](evidencias/17.png)

Conversão de series para dataframe
![Evidencia 18](evidencias/18.png)

Utilização da segunda função de agregação (sum)
![Evidencia 19](evidencias/19.png)

Adicionar uma observação 
![Evidencia 20](evidencias/20.png)

Obter a data atual através de uma função e adicionar outra observação ao final do dataframe final
![Evidencia 21](evidencias/21.png)

Erro ao não converter series para dataframe
![Evidencia 22](evidencias/Err_01.png)
![Evidencia 23](evidencias/Err_02.png)

Erros de definição de credenciais
![Evidencia 24](evidencias/Err_03.png)
![Evidencia 25](evidencias/Err_04.png)

Erros de localização de arquivo local
![Evidencia 26](evidencias/Err_05.png)

Primeiro teste bem sucedido de acesso das credenciais à conta AWS
![Evidencia 27](evidencias/Exec_00.png)

Execução das chaves de acesso no terminal do VScode
![Evidencia 28](evidencias/Exec_01.png)

Execução do script **Desafio5.py**
![Evidencia 29](evidencias/Exec_01.png)
![Evidencia 30](evidencias/Exec_02.png)
![Evidencia 31](evidencias/Exec_03.png)
![Evidencia 32](evidencias/Exec_04.png)
![Evidencia 33](evidencias/Exec_05.png)


[Arquivos do Desafio](desafio/)