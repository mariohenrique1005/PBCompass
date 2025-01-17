# Importação das bibliotecas
import pandas as pd
import json
import os
import aiohttp
import asyncio
import boto3
from datetime import datetime

# Configuração da API, obtendo a chave e a base da URL para outros endereços da API
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.themoviedb.org/3'

# Bucket S3 e prefixo de caminho
bucket_name = os.getenv('BUCKET_NAME')
s3_path = f"Raw/TMDB/JSON/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/"   # Armazena os dados no caminho especificado, de acordo com a data

# Inicializando o cliente do S3
s3_client = boto3.client('s3')

# Limitar o número de requisições para 4 simultâneas
semaphore = asyncio.Semaphore(4)

# Carregar IDs do IMDb do arquivo CSV que está no S3
def processar_csv_from_s3(s3_bucket, s3_key):
    # Baixar o arquivo CSV do S3 para o diretório temporário
    local_csv_path = '/tmp/movies.csv'  # Caminho temporário no Lambda
    s3_client.download_file(s3_bucket, s3_key, local_csv_path)
    
    # Ler o arquivo CSV usando pandas
    df = pd.read_csv(local_csv_path, delimiter='|', usecols=['id', 'genero', 'anoLancamento'])  # Usar apenas as colunas necessárias
    df['anoLancamento'] = pd.to_numeric(df['anoLancamento'], errors='coerce')   # Conversões de tipos
    df = df.dropna(subset=['anoLancamento'])
    df['anoLancamento'] = df['anoLancamento'].astype(int)
    filtro_df = df[ # Filtrar dados de acordo com os requisitos: Gênero comédia e animação e ano de lançamento dos filmes
        ((df['genero'].str.contains('Comedy', case=False)) | (df['genero'].str.contains('Animation', case=False))) &
        (df['anoLancamento'] >= 2013)
    ]
    imdb_ids = filtro_df['id'].unique().tolist()
    return imdb_ids # Retorna uma lista com as IDS do IMDB requisitadas

# Função para buscar ID do TMDB a partir do ID do IMDb
async def get_tmdb_id(session, imdb_id):
    url = f"{BASE_URL}/find/{imdb_id}"  # URL que busca filmes de acordo com a ID do IMDB
    params = {'api_key': API_KEY, 'external_source': 'imdb_id'}
    async with semaphore:   # Envolve o código para fazer o número de tarefas simultâneas de acordo com o semaphore
        async with session.get(url, params=params) as response: # Realiza uma requisição para a URL especificada, junto com os parâmetros buscados
            if response.status == 200:  # Verifica se a resposta foi OK
                data = await response.json()    # Processa a resposta do servidor
                if 'movie_results' in data and len(data['movie_results']) > 0:  # Verifica se 'movie_results' está no JSON da API e se contém pelo menos 1 item
                    return data['movie_results'][0]['id']   # Retorna a ID do primeiro item da lista
    return None

# Função assíncrona para buscar informações do filme pelo ID do TMDB
async def get_movie_info(session, tmdb_id):
    url = f"{BASE_URL}/movie/{tmdb_id}"
    params = {'api_key': API_KEY}
    async with semaphore:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return {    # Dados requisitados dos filmes
                    'Id': data.get('id'),
                    'Id_IMDB': data.get('imdb_id'),
                    'Titulo': data.get('title'),
                    'Orcamento': data.get('budget'),
                    'Bilheteria': data.get('revenue')
                }
    return None

# Função para dividir os dados em lotes menores
def chunk_data(data, batch_size):
    #Divide a lista de dados em lotes menores
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]    # Retorna a parte da lista

# Salvar os resultados no S3
def save_to_s3(data, bucket_name, s3_prefix, batch_size=100):
    #Salva os dados no S3 em arquivos com um número fixo de registros
    for i, batch in enumerate(chunk_data(data, batch_size), 1):
        # Converte o lote atual em JSON
        batch_data = json.dumps(batch, indent=4)
        
        # Define o nome do arquivo no S3
        s3_key = f"{s3_prefix}movies_batch_{i}.json"
        
        # Faz upload para o S3, com tratamento de erros
        try:
            s3_client.put_object(Body=batch_data, Bucket=bucket_name, Key=s3_key)
            print(f"Arquivo {s3_key} carregado com sucesso para o S3!")
        except boto3.exceptions.S3UploadFailedError as e:
            print(f"Erro ao salvar {s3_key}: {e}")

# Função principal para processamento assíncrono
async def main(event, context):
    # Configuração do caminho do CSV no S3
    s3_key_csv = 'Raw/Local/CSV/Movies/2025/1/2/movies3.csv'  # Caminho para o arquivo CSV no S3
    
    imdb_ids = processar_csv_from_s3(bucket_name, s3_key_csv)  # Chama a função de processamento do CSV
    print(f'Quantidade de Ids carregadas: {len(imdb_ids)}') # Mostra quantas IDS foram carregadas
    total_ids = len(imdb_ids)
    print(f"Total de IDs a serem processados: {total_ids}") # Mostra quantas IDS serão processadas

    async with aiohttp.ClientSession() as session:  # Sessão assíncrona para realizar várias execuções ao mesmo tempo
        movies_data = []    # Lista para armazenar dados dos filmes
        for index, imdb_id in enumerate(imdb_ids, start=1): # Iteração sobre a lista  de IDS do IMDB
            print(f"Processando ID {index}/{total_ids} ({total_ids - index} restantes)")    # Exibe qual ID está sendo processada e quantas restam
            
            tmdb_id = await get_tmdb_id(session, imdb_id)   # Converte a ID do IMDB em uma do TMDB para ser processada
            if tmdb_id: # Verifica se a ID do TMDB é válida
                movie_info = await get_movie_info(session, tmdb_id) # Chama a função para pegar informações do filme
                if movie_info:  # Verifica se as informações de um determinado filme foram retornadas
                    movies_data.append(movie_info)  # Adiciona as informações do filme à lista de filmes

        # Salva os dados diretamente no S3 em lotes de 100
        save_to_s3(movies_data, bucket_name, s3_path, batch_size=100)   # Chama a função de salvar os arquivos no S3
        print("Processamento concluído!")

# Função handler que será chamada pelo Lambda
def lambda_handler(event, context):
    asyncio.run(main(event, context))   # Executar função principal
    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído e dados salvos no S3.')
    }