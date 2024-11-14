arquivo_entrada = 'D:/Users/mario/Documents/Compass/S3/Exercicios/actors.csv'
arquivo_saida = 'C:/Users/mario/Github/Sprint03/exercicios/ExercicioII/Etapa-1.txt'

maior_quantidade_filmes = 0
ator_mais_filmes = ""

with open(arquivo_entrada, mode='r') as csv:
    cabecalho = csv.readline().strip().split(',')
    indice_ator = cabecalho.index("Actor")
    indice_num_filmes = cabecalho.index("Number of Movies")

    for linha in csv:
        colunas = linha.strip().split(',')
        nome_ator = colunas[indice_ator]
        try:
            quantidade_filmes = int(colunas[indice_num_filmes].strip())
            if quantidade_filmes > maior_quantidade_filmes:
                maior_quantidade_filmes = quantidade_filmes
                ator_mais_filmes = nome_ator
        except ValueError:
            print(f"Valor inválido encontrado na linha para o ator {nome_ator}: {colunas[indice_num_filmes].strip()}")
            continue

resultado = f"O ator com a maior quantidade de filmes é {ator_mais_filmes} com {maior_quantidade_filmes} filmes."
with open(arquivo_saida, mode='w') as arquivo_saida:
    arquivo_saida.write(resultado)
print("Resultado salvo com sucesso em 'etapa-1.txt'")