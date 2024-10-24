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

1-Cria pasta vendas em ecommerce e verifica se ela já existe para não causar erro na criação<br>
if [ ! -d "/home/mario/ecommerce/vendas" ]; then   mkdir -p "/home/mario/ecommerce/vendas"; fi

2-Copia o arquivo dados_de_vendas.csv para a pasta vendas<br>
cp -u /home/mario/ecommerce/dados_de_vendas.csv /home/mario/ecommerce/vendas

3-Muda para o diretório vendas<br>
cd vendas

4-Se ainda não existir, cria a pasta backup<br>
if [ ! -d "/home/mario/ecommerce/vendas/backup" ]; then   mkdir -p "/home/mario/ecommerce/vendas/backup"; fi

5-Copia o arquivo dados_de_vendas.csv para a pasta backup<br>
cp -u /home/mario/ecommerce/dados_de_vendas.csv /home/mario/ecommerce/vendas/backup

6-Muda para a pasta backup<br>
cd backup

7-Renomeia o arquivo dados_de_vendas.csv para o mesmo nome com a inclusão da data<br>
mv /home/mario/ecommerce/vendas/dados_de_vendas.csv /home/mario/ecommerce/vendas/dados_de_vendas-$(date +%Y%m%d).csv

8-Renomeia o arquivo dados_de_vendas.csv com a inclusão da data para relatorio com data e hora, além de armazenar em uma variável<br>
mv /home/mario/ecommerce/vendas/backup/dados_de_vendas* /home/mario/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d>OUTPUT_FILE="/home/mario/ecommerce/vendas/backup/relatorio_$(date +"%Y%m%d_%H%M%S").txt"

9-Cria o txt com arquivo que está na variável<br>
touch "$OUTPUT_FILE"

10-Coloca a data e hora no arquivo txt<br>
date +"%Y/%m/%d %H:%M" > "$OUTPUT_FILE"

11-Copia a segunda linha do csv para o arquivo txt<br>
sed -n '2p' /home/mario/ecommerce/dados_de_vendas.csv | cut -d',' -f5 >> "$OUTPUT_FILE"

12-Copia a última linha do csv para o arquivo txt<br>
sed -n '67p' /home/mario/ecommerce/dados_de_vendas.csv | cut -d',' -f5 >> "$OUTPUT_FILE"

13-Soma a quantidade total de itens únicos e incorpora ao arquivo txt<br>
tail -n +2 /home/mario/ecommerce/dados_de_vendas.csv | cut -d',' -f2 | sort | uniq | wc -l >> "$OUTPUT_FILE"

14-Mostra as 10 primeiras linhas do arquivo csv e incrementa ao arquivo txt<br>
tail -n +2 /home/mario/ecommerce/dados_de_vendas.csv | head -n 10 /home/mario/ecommerce/dados_de_vendas.csv >> "$OUTPUT>echo >> "$OUTPUT_FILE"

15-Comprime o arquivo csv que está dentro da pasta backup<br>
gzip /home/mario/ecommerce/vendas/backup/backup-dados*

16-Remove o arquivo csv que está dentro da pasta backup<br>
rm -f /home/mario/ecommerce/vendas/backup/*.csv

17-Muda para um diretorio anterior<br>
cd ..

18-Remove o arquivo csv da pasta vendas<br>
rm -f /home/mario/ecommerce/vendas/dados_de_vendas*

5. Após a codificação do script processamento_de_vendas.sh, foi realizado o agendamento de sua execução através do comando: crontab -e, executando um simples comando, para ser executado na quinta e sexta-feira as 14:00 e 15:00

6. Descrição do crontab:

1- Executa o script as quintas e sexta-feiras as 14:00<br>
00 14 * * 4,5 /home/mario/ecommerce/processamento_de_vendas.sh

2- Executa o script as quintas e sexta-feiras as 15:00<br>
00 15 * * 4,5 /home/mario/ecommerce/processamento_de_vendas.sh

7. Após a criação do script de agendamento, foi criado o script de consolidação dos relatórios: consolidador_de_processamento_de_vendas.sh

8. Descrição do script consolidador_de_processamento_de_vendas.sh:

1-Copia todo o conteúdo de todos os arquivos txt armazenados na pasta backup para o arquivo relatorio_final.txt<br>
(cat /home/mario/ecommerce/vendas/backup/*.txt; printf "\n") >> /home/mario/ecommerce/relatorio_final.txt