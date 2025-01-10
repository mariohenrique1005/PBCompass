# Importação das bibliotecas
import requests
import pandas as pd
import getpass
import boto3
from IPython.display import display

# Pega a chave da api
api_key=getpass.getpass('Digite sua chave api: ')

# Define os dados que serão requisitados
endpoint='top_rated'
parametros='language=pt-BR'
url=f'https://api.themoviedb.org/3/movie/{endpoint}?api_key={api_key}&{parametros}'

# Testa a conexão e armazena os dados em um json
response=requests.get(url)
data=response.json()

# Cria a lista com os dados dos filmes
filmes=[]

# Sessão de tratamento de erros
try:
    if response.status_code == 200:
        print("Conexão realizada com sucesso!")
    elif response.status_code == 401:
        raise ValueError ("Chave API inválida!")
    elif response.status_code == 422:
        raise ValueError ("Parâmetros inválidos!")
    else:
        raise ValueError (f"Erro inesperado! Código: {response.status_code}")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")

# Armazena na lista filmes[] os dados dos filmes
for movie in data['results']:
    df={
        'Titulo': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }
    filmes.append(df)

# Cria o dataframe com a lista filmes[]
df=pd.DataFrame(filmes)

# Exportando Database
nome_arquivo=input("Digite o nome do arquivo, sem extensão, que será salvo localmente e no bucket: ")
nome_arquivo=f'{nome_arquivo}.csv'
df.to_csv(nome_arquivo, index=False, encoding='UTF-8')