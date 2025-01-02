# Importação dos módulos Boto3, OS e Datetime
import boto3
import os
from datetime import datetime

# Definição das variáveis para acessar as credenciais
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token = os.getenv('AWS_SESSION_TOKEN')
aws_default_region = os.getenv('AWS_DEFAULT_REGION')

# Criar um cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
)

# Alterar o diretorio de trabalho do os
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretorio_atual)
print(f"Diretório atual: {os.getcwd()}")

# Definindo a datal atual
data_atual=datetime.now()

# Separando a data por dia, mês e ano
ano=data_atual.year
mes=data_atual.month
dia=data_atual.day

# Nome do Bucket de destino
bucket_name='desafio-final-mario-henrique'

# Definindo destino do arquivo 'movies' para upload
file_name1='movies.csv'
s3_file_name=f'Raw/Local/CSV/Movies/{ano}/{mes}/{dia}/{file_name1}'
s3_client=boto3.client('s3', region_name='us-east-1')

# Carregar o arquivo 'movies' para o bucket
try:
    s3_client.upload_file(file_name1, bucket_name, s3_file_name)
    print(f"Arquivo '{file_name1}' carregado com sucesso para o bucket '{bucket_name}' como '{s3_file_name}'")
    # Tratamento do erro
except Exception as e:
    print(f"Erro ao criar o bucket ou carregar arquivo: {e}")
    if os.path.exists(f'{file_name1}'):
        print(f"O arquivo '{file_name1}' existe!")
    else:
        print("Arquivo não encontrado.")

# Definindo destino do arquivo 'series' para upload
file_name2='series.csv'
s3_file_name=f'Raw/Local/CSV/Series/{ano}/{mes}/{dia}/{file_name2}'

# Carregar o arquivo 'series' para o bucket
try:
    s3_client.upload_file(file_name2, bucket_name, s3_file_name)
    print(f"Arquivo '{file_name2}' carregado com sucesso para o bucket '{bucket_name}' como '{s3_file_name}'")
# Tratamento do erro
except Exception as e:
    print(f"Erro ao criar o bucket ou carregar arquivo: {e}")
    if os.path.exists(f'{file_name2}'):
        print(f"O arquivo '{file_name2}' existe!")
    else:
        print("Arquivo não encontrado.")