csv = 'D:/Users/mario/Documents/Compass/S3/Exercicios/actors.csv'
arquivo_saida = 'C:/Users/mario/Github/Sprint03/exercicios/ExercicioII/Etapa-4.txt'

contador_filmes = {}

with open(csv, mode='r') as csv:
    cabecalho = csv.readline().strip().split(',')
    indiceFilme1 = cabecalho.index("#1 Movie")

    for linha in csv:
        colunas = linha.strip().split(',')
        filme = colunas[indiceFilme1].strip()

        if filme in contador_filmes:
            contador_filmes[filme] += 1
        else:
            contador_filmes[filme] = 1

filmes_ordenados = sorted(contador_filmes.items(), key=lambda x: (-x[1], x[0]))
with open(arquivo_saida, mode='w') as arquivo_saida:
    for filme, quantidade in filmes_ordenados:
        arquivo_saida.write(f"O filme {filme} aparece {quantidade} vez(es) no dataset\n")

print("Resultado salvo com sucesso em 'etapa-4.txt'")