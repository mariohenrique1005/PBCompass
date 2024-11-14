csv = 'D:/Users/mario/Documents/Compass/S3/Exercicios/actors.csv'
arquivo_saida = 'C:/Users/mario/Github/Sprint03/exercicios/ExercicioII/Etapa-2.txt'

soma_gross = 0
contador = 0

with open(csv, mode='r') as csv:
    cabecalho = csv.readline().strip().split(',')
    indice_receita= cabecalho.index("Gross")
       
    for linha in csv:
        colunas = linha.strip().split(',')
        valores_gross = float(colunas[indice_receita].strip())
        soma_gross += valores_gross
        contador += 1

if contador > 0:
    media_gross = soma_gross / contador
    print(f"A média de Gross é: {media_gross:.2f}")
else:
    print("Não há dados válidos para calcular a média.")
resultado=f"A média de receita de bilheteria bruta dos principais filmes é de: {media_gross:.2f}"

with open(arquivo_saida, mode='w') as arquivo_saida:
    arquivo_saida.write(resultado)
print("Resultado salvo com sucesso em 'etapa-2.txt'")