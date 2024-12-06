# Instruções

Nesta Sprint foi realizado o desafio de criar e executar imagens e containers do Docker, executando 2 scripts distintos do Python. O desafio foi executado com as seguintes etapas:<br>

1. Construção da primeira imagem e execução do script: "Carguru.py" em um container<br>
2. Reutilização de um container<br>
3. Construção da segunda imagem e execução do script que cria hashs para strings, através do algoritmo SHA-1, em um novo container

## Resumo

**Python:** Aprendi mais funções da linguagem, como utilizar funções lambda, map, list

**Docker:** Como criar e utilizar: containers e imagens

# Exercícios

[Pasta Exercicios](exercicios/)

## Evidências

Arquivo Dockerfile para criar a imagem de carguru.py
![Evidencia 1](evidencias/01.png)

Criando a primeira imagem e nomeando-a
![Evidencia 2](evidencias/02.png) 

Criando um container
![Evidencia 3](evidencias/03.png)

Comprovando que o container foi executado
![Evidencia 4](evidencias/04.png)

Reiniciando um container
![Evidencia 5](evidencias/05.png)

Exibindo que o container foi reiniciado
![Evidencia 6](evidencias/06.png)

Script Python para gerar uma hash para a string de entrada
![Evidencia 7](evidencias/07.png)

Arquivo Dockerfile para criar a imagem de mascarar-dados.py
![Evidencia 8](evidencias/08.png)

Criando a segunda imagem e nomeando-a
![Evidencia 9](evidencias/09.png)

Criando o container e executando-o de forma interativa
![Evidencia 10](evidencias/10.png)

Container da imagem mascarar-dados em execução
![Evidencia 11](evidencias/11.png)

Saindo do terminal e encerrando a execução do container
![Evidencia 12](evidencias/12.png)

Erro ao executar a imagem sem o -it
![Evidencia 13](evidencias/13.png)

Utilização do algoritmo incorreto
![Evidencia 14](evidencias/14.png)

Hashs criadas de forma incorreta (256 bits no lugar de 160 bits)
![Evidencia 15](evidencias/15.png)

Projeto completo com os arquivos:
[Arquivos do Desafio](desafio/)

## Apresentação do desafio

[Desafio](desafio/README.md)

# Certificados

Certificados do Curso de AWS:
[Certificado AWS 1](certificados/AWS1.pdf) | [Certificado AWS 2](certificados/AWS2.pdf)