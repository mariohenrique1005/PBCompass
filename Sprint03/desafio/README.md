# Desafio
Para a execução deste desafio foi criado um código na linguagem Python, com o auxílio das bibliotecas Pandas e Matplotlib no ambiente de desenvolvimento online: Google Colab, um notebook semelhante ao Jupyter

## Etapas

1. Para a correta execução do desafio, primeiro foi necessário importar as bibliotecas Pandas e Numpy, e posteriormente fazer o upload do arquivo CSV, que contém todos os dados utilizados
![Evidencia 1](../evidencias/01.png)

2. Então o arquivo csv é lido e armazenado em uma variável e por sua vez armazenando em um Dataframe(df)
![Evidencia 2](../evidencias/02.png)

3. Visualizar as primeiras 10 linhas do arquivo para entender a estrutura dos dados e visualizar as colunas
![Evidencia 3](../evidencias/03.png) 
![Evidencia 4](../evidencias/04.png)

4. Visualizando informações sobre os tipos de dados de cada coluna, será necessário converter os tipos de dados de todas as colunas, que estão como **object**, exceto por Rating que já está em float
![Evidencia 5](../evidencias/05.png)

5. Eliminando as linhas duplicadas, armazenando em um novo dataframe(df2), para tornar o primeiro dataframe como um backup, e visualizando o resultado. O dataframe(df2) foi reduzido de 10841 linhas para 10358
![Evidencia 6](../evidencias/06.png)
![Evidencia 7](../evidencias/07.png)

6. Visualizando informações sobre o novo dataframe(df2) sem linhas duplicadas
![Evidencia 8](../evidencias/08.png)

7. Verificando as linhas que estavam duplicadas no dataframe inicial(df)
![Evidencia 9](../evidencias/09.png)

8. Conferindo se a linha toda realmente estava duplicada, a partir do exemplo de visualização do aplicativo: "AAFP" em df. Pode-se constatar que a linha 10768 é uma cópia da 2515
![Evidencia 10](../evidencias/10.png)

9. Visualizando os valores únicos de Category e Rating. Das execuções [10] a [13] foram feitas verificações de valores únicos em suas respectivas colunas para detectar valores inconsistentes ou fora do padrão
![Evidencia 11](../evidencias/11.png)

10. Ao detectar uma linha fora do padrão em 'Reviews', foi executado o comando para visualizar esta linha e  constatou-se que os valores estavam todos fora do lugar. Então em [14] foi feita uma copia do df2 para o df3 (pois grandes mudanças foram feitas, por segurança df2 foi mantido como um backup e as alterações feitas em df3), e feitas as alterações nos campos desta linha 10472
![Evidencia 12](../evidencias/12.png)
![Evidencia 13](../evidencias/13.png)
Linha corrigida:
![Evidencia 14](../evidencias/14.png)

11. De [15] a [27] foram feitas verificações de valores únicos em suas respectivas colunas para detectar valores inconsistentes ou fora do padrão
![Evidencia 15](../evidencias/15.png)
![Evidencia 16](../evidencias/16.png)

12. Cópia do df3 para o df4 para realizar as futuras mudanças nos atributos e conversão dos tipos de dados nos campos. De [29] a [55] foram realizadas as mudanças necessárias, como substituição de valores e conversão de tipos de dados
![Evidencia 17](../evidencias/17.png)
Aqui é possível verificar as colunas e seus tipos de dados em df4:
![Evidencia 18](../evidencias/18.png)

13. Plotagem do primeiro gráfico, de barras, com os 5 aplicativos mais instalados. Antes da plotagem do gráfico é necessário criar o vetor com os 5 aplicativos mais instalados, extraídos da coluna 'Installs'
![Evidencia 19](../evidencias/19.png)
Gráfico:
![Evidencia 20](../evidencias/20.png)

14. Plotagem do segundo gráfico, de pizza, e exibição da representação (em %) de aplicativos por categoria em relação ao total
![Evidencia 21](../evidencias/21.png)
Gráfico:
![Evidencia 22](../evidencias/22.png)

15. Mostrando o aplicativo mais caro, através da seleção do maior valor de 'Price'
![Evidencia 23](../evidencias/23.png)
![Evidencia 24](../evidencias/24.png)

16. Mostrando quantos aplicativos são classificados como Mature 17+ Para exibir apenas o valor, é necessário que seja exibido apenas o primeiro valor do vetor, com: shape[0]
![Evidencia 25](../evidencias/25.png)

17. Exibindo os 10 aplicativos por maior número de reviews, juntamente com a quantidade de reviews que possuem. Foi necessário selecionar os únicos, pois haviam aplicativos repetidos
![Evidencia 26](../evidencias/26.png)

**A partir desta seção a escolha das operações efetuadas ficaram a critério do desenvolvedor**

18. Foi escolhida a exibição dos 5 aplicativos mais instalados da categoria 'Food and drink' e exibido as respectivas quantidades de instalações em formato de valor e depois de lista
![Evidencia 28](../evidencias/28.png)

19. Foi escolhido a exibição do aplicativo pago mais baixado e sua respectiva categoria, primeiro em formato de valor e depois de lista
![Evidencia 29](../evidencias/29.png)
![Evidencia 30](../evidencias/30.png)

20. Criação de um novo gráfico, do tipo dispersão, exibindo os 10 aplicativos com maior números de reviews e seu respectivo rating.
![Evidencia 31](../evidencias/31.png)
Podemos notar que para um número de reviews acima de 50 milhões apenas 1 aplicativo possui nota maior ou igual 4.5, porém o conjunto de dados ainda é pequeno para tirar alguma conclusão concreta. Gráfico:
![Evidencia 32](../evidencias/32.png)

21. Criação de um gráfico do tipo linha, exibindo os 5 aplicativos mais instalados da categoria 'Food and drink' e seu respectivo rating
![Evidencia 33](../evidencias/33.png)
Aqui todos os aplicativos selecionados possuem o mesmo número de instalações. Podemos verificar que há um salto na nota quando saímos das duas versões de 'Mc Donald's' para outros aplicativos de outras marcas. Gráfico:
![Evidencia 34](../evidencias/34.png)

## Erros e problemas

1. Para que fosse possível fazer as alterações na linha 10472 em [Evidencia 12](../evidencias/12.png) foram feitas várias reexecuções no código com várias modificações até acertar as colunas correspondentes para as mudanças corretas

2. Foi necessário selecionar os valores únicos de 'Reviews', pois apenas selecionando os 10 aplicativos por maior número de reviews, os valores estavam aparecendo duplicados, como pode ser visto em:
![Evidencia 27](../evidencias/27.png)