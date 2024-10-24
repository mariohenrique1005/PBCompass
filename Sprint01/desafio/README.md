# Desafio
Para a execução deste desafio foram realizados vários testes antes de implementar o código final

## Etapas

1. Primeiramente foi criada uma pasta de teste para testar alguns comandos do ambiente Linux, como pode ser visto em: [Evidencia 2](../evidencias/Teste_comandos.png)
| [Evidencia 3](../evidencias/Teste_comandos2.png)
| [Evidencia 4](../evidencias/Teste_comandos_txt.png)

2. Depois foi criada a pasta ecommerce e copiado o arquivo csv para dentro desta: [Evidencia 1](../evidencias/Copiando_csv.png)

3. Então foi criado o código para o script: processamento_de_vendas
Para realizar a codificação, foram feitas partes do código no notepad(ambiente windows), para depois copiar o conteúdo para o editor de textos nano no ambiente Linux. Desta forma seria mais fácil ter acesso ao código, já que estava sendo usado ambiente WSL

4. Descrição do código processamento_de_vendas.sh:
[Processamento_de_vendas.sh](../evidencias/Processamento_de_vendas.txt)


5. Após a codificação do script processamento_de_vendas.sh, foi realizado o agendamento de sua execução através do comando: crontab -e, executando um simples comando, para ser executado na quinta e sexta-feira as 14:00 e 15:00

6. Descrição do crontab:
[Crontab](../evidencias/Crontab.txt)

7. Após a criação do script de agendamento, foi criado o script de consolidação dos relatórios: consolidador_de_processamento_de_vendas.sh

8. Descrição do script consolidador_de_processamento_de_vendas.sh:
[Consolidador_de_Processamento_de_vendas.sh](../evidencias/Consolidador_de_processamento_de_vendas.txt)