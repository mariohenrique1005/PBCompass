csv = 'D:/Users/mario/Documents/Compass/S3/Exercicios/actors.csv'
arquivo_saida = 'C:/Users/mario/Github/Sprint03/exercicios/ExercicioII/Etapa-3.txt'

maior_media = 0
ator_maior = ""

with open(csv, mode='r') as csv:
    cabecalho = csv.readline().strip().split(',')
    indice_average = cabecalho.index("Average per Movie")
    indice_ator = cabecalho.index("Actor")

    for linha in csv:
        colunas = linha.strip().split(',')
        average_per_movie = float(colunas[indice_average].strip())

        if average_per_movie > maior_media:
            maior_media = average_per_movie
            ator_maior = colunas[indice_ator].strip()

resultado=f"O ator com a maior média de receita de bilheteira bruta por filme é: {ator_maior} com uma média de {maior_media:.2f}"
print(resultado)

with open(arquivo_saida, mode='w') as arquivo_saida:
    arquivo_saida.write(resultado)
print("Resultado salvo com sucesso em 'etapa-3.txt'")