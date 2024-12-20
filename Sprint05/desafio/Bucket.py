# Importação dos módulos Boto3 e OS
import boto3
import os

# Definição das variáveis para acessar as credenciais
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_session_token = os.environ.get('AWS_SESSION_TOKEN')
aws_default_region = os.environ.get('AWS_DEFAULT_REGION')

# Criar um cliente S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=aws_default_region
)

# Nome do bucket a ser criado
bucket_name = input('Insira um nome para o bucket: ') # O nome deve ser único no mundo

# Criar o bucket
s3_client.create_bucket(Bucket=bucket_name)
print(f'Bucket {bucket_name} criado com sucesso!')

# Alterar o diretorio de trabalho do os, para que o script seja executável em qualquer máquina, desde que os arquivos permaneçam no mesmo diretório
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretorio_atual)
print(f"Diretório atual: {os.getcwd()}")

# Enviar o arquivo
file_name='Saldos_BCB.csv'
s3_file_name='Saldos_BCB.csv'
s3_client=boto3.client('s3', region_name='us-east-1')

# Carregar o arquivo para o bucket
try:
    s3_client.upload_file(file_name, bucket_name, s3_file_name)
    print(f"Arquivo '{file_name}' carregado com sucesso para o bucket '{bucket_name}' como '{s3_file_name}'")
# Tratamento do erro
except Exception as e:
    print(f"Erro ao criar o bucket ou carregar arquivo: {e}")
    if os.path.exists(f'{file_name}'):
        print("O arquivo existe!")
    else:
        print("Arquivo não encontrado.")

# Apagar o arquivo local: 'Saldos_BCB.csv'
if os.path.exists(file_name):
    os.remove(file_name)
    print('O arquivo foi apagado com sucesso!')
else:
    print('O arquivo nao existe.')