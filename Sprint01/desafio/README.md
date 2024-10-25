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

## Erros e problemas

1. Ao tentar comprimir um arquivo para .zip houve um erro no terminal, mesmo após instalação e atualização dos pacotes, portanto, foi utilizado o gzip para a compactação dos arquivos:
Erro no zip: [Evidencia 5](../evidencias/Erro_zip.png)

2. Ocorreram alguns erros ao executar o script pela segunda vez, relacionados à criação de pastas - que já existiam e outros erros relacionados à criação de pastas com caracteres indesejados, pois foi testado a criação de um script diretamente no bloco de notas, dentro do ambiente windows, o que acabou por ser um método equivocado na criação do script:
[Evidencia 6](../evidencias/Erro_prim_teste.png)
| [Evidencia 7](../evidencias/Erros_prim_teste2.png)

3. Houve um erro ao adicionar conteúdo no arquivo txt, pois havia um erro no script que estava tentando copiar conteúdo do arquivo compactado, no lugar de copiar dados do arquivo csv:
[Evidencia 8](../evidencias/Erro_txt.png)

4. Erro no script, não estava conseguindo agendar execução do script, pois o cron estava no local errado e o caminho para criar o arquivo txt não estava preciso, conforme as exigências do cron:
[Evidencia 9](../evidencias/Erro_cron_txt.png)

5. Para poder executar o script conforme consta no desafio seria impossível, devido à falta de tempo restante, então, o cron foi programado para executar 4 vezes, sendo na quinta-feira e na sexta-feira às 14:00 e 15:00 (2 vezes ao dia)