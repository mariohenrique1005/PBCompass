# Importação das bibliotecas
import pandas as pd
import json
import os
import aiohttp
import asyncio
import getpass

# Configuração da API, obtendo a chave e a base da URL para outros endereços da API
API_KEY = getpass.getpass('Digite sua chave api: ')
BASE_URL = 'https://api.themoviedb.org/3'

# Alteração do diretório de trabalho para armazenar e ler arquivos
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretorio_atual)
print(f"Diretório de trabalho atual: {os.getcwd()}")

# Carregar IDs do IMDB proveninentes do arquivo CSV
def processar_csv(csv_path):
    df = pd.read_csv(csv_path, delimiter='|', usecols=['id', 'genero', 'anoLancamento']) # Usar apenas as colunas necessárias
    df['anoLancamento'] = pd.to_numeric(df['anoLancamento'], errors='coerce') # Conversões de tipos
    df = df.dropna(subset=['anoLancamento'])
    df['anoLancamento'] = df['anoLancamento'].astype(int)
    filtro_df = df[     # Filtrar dados de acordo com os requisitos: Gênero comédia e animação e ano de lançamento dos filmes
        ((df['genero'].str.contains('Comedy', case=False)) | (df['genero'].str.contains('Animation', case=False))) &
        (df['anoLancamento'] >= 2020)
    ]
    imdb_ids = filtro_df['id'].unique().tolist()
    return imdb_ids # Retorna uma lista com as IDS do IMDB requisitadas

# Limitar o número de requisições para 4 simultâneas
semaphore = asyncio.Semaphore(4)

# Função assíncrona para buscar ID do TMDB a partir do ID do IMDb
async def get_tmdb_id(session, imdb_id):
    url = f"{BASE_URL}/find/{imdb_id}"  # URL que busca filmes de acordo com a ID do IMDB
    params = {'api_key': API_KEY, 'external_source': 'imdb_id'}
    async with semaphore:   # Envolve o código para fazer o número de tarefas simultâneas de acordo com o semaphore
        async with session.get(url, params=params) as response: # Realiza uma requisição para a URL especificada, junto com os parâmetros buscados
            if response.status == 200:  # Verifica se a resposta foi OK
                data = await response.json() # Processa a resposta do servidor
                if 'movie_results' in data and len(data['movie_results']) > 0:
                    return data['movie_results'][0]['id']
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

# Salvar os resultados em arquivos JSON, particionando-os, com 100 registros em cada arquivo
def save_to_json(data, output_dir, batch_size=100):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(0, len(data), batch_size):   # Contador de registros em cada arquivo
        batch = data[i:i + batch_size]
        with open(f"{output_dir}/movies_batch_{i // batch_size + 1}.json", 'w') as f:
            json.dump(batch, f, indent=4)

# Função principal para processamento assíncrono
async def main():
    input_csv = 'movies.csv' # Caminho do CSV
    output_dir = input('Insira um nome para o diretório dos arquivos: ')  # Pasta para salvar os arquivos JSON
    
    imdb_ids = processar_csv(input_csv) # Chama a função de processamento do CSV
    print(f'Quantidade de Ids carregadas: {len(imdb_ids)}') # Mostra quantas IDS foram carregadas
    total_ids = len(imdb_ids)
    print(f"Total de IDs a serem processados: {total_ids}") # Mostra quantas IDS serão processadas

    async with aiohttp.ClientSession() as session: # Sessão assíncrona para realizar várias execuções ao mesmo tempo
        movies_data = [] # Lista para armazenar dados dos filmes
        for index, imdb_id in enumerate(imdb_ids, start=1): # Iteração sobre a lista  de IDS do IMDB
            print(f"Processando ID {index}/{total_ids} ({total_ids - index} restantes)")    # Exibe qual ID está sendo processada e quantas restam
            
            tmdb_id = await get_tmdb_id(session, imdb_id)   # Converte a ID do IMDB em uma do TMDB para ser processada
            if tmdb_id: # Verifica se a ID do TMDB é válida
                movie_info = await get_movie_info(session, tmdb_id) # Chama a função para pegar informações do filme
                if movie_info:  # Verifica se as informações de um determinado filme foram retornadas
                    movies_data.append(movie_info)  # Adiciona as informações do filme à lista de filmes

        save_to_json(movies_data, output_dir) # Chama a função de salvar os arquivos em JSON
        print("Processamento concluído!")

# Executar a função principal
asyncio.run(main())