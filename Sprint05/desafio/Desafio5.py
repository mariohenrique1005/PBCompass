### Importando a biblioteca Pandas, Datetime, Runpy, OS e Boto3
import pandas as pd
from datetime import datetime
import runpy
import os
import boto3

## Configurando o OS para o diretório dos arquivos
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretorio_atual)
# Importando o script 'Bucket.py'
file_path = os.path.join(os.path.dirname(__file__), "Bucket.py")
namespace = runpy.run_path(file_path)

# Configurando as credenciais
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

# Definindo as variáveis
bucket_name= namespace.get('bucket_name')
s3_file_name = namespace.get('s3_file_name')  # Caminho do arquivo no S3
local_file_name = s3_file_name  # Caminho para onde o arquivo será baixado

# Baixar o arquivo do S3 para o diretório local
try:
    s3_client.download_file(bucket_name, s3_file_name, local_file_name)
    print(f"Arquivo '{s3_file_name}' baixado com sucesso para '{local_file_name}'")
except Exception as e:
    print(f"Erro ao baixar o arquivo: {e}")

# Lendo o CSV e salvando em um Dataframe
arquivo=s3_file_name
df=pd.read_csv(arquivo)

## Copiando o dataframe para dataframe 2
df2=df.copy()

# Renomeando colunas
df2.rename(columns={'Conta_Nome':'Descrição da conta','Valor_Ajustado':'Valor ajustado'},inplace=True)

# Renomear a descrição da conta, tornando esta mais apresentável
def capitalizar(frase):
  return frase.lower().capitalize()
df2['Descrição da conta']=df2['Descrição da conta'].apply(capitalizar)

# Substituindo as ',' por '.' e convertendo valores
df2["Valor ajustado"] = df2["Valor ajustado"].str.replace(",", ".", regex=False)
df2['Data']=pd.to_datetime(df2['Data'])
df2['Conta']=df2['Conta'].astype(pd.StringDtype())
df2['Descrição da conta']=df2['Descrição da conta'].astype(pd.StringDtype())
df2['Valor ajustado'] = df2['Valor ajustado'].astype(float)
df2['Origem']=df2['Origem'].astype(pd.StringDtype())
df2.dtypes #Visualizar os tipos de dados

# Removendo espaços adicionais
df2['Descrição da conta'] = df2['Descrição da conta'].str.replace(r'\s+', ' ', regex=True)

# Verificando se há valores nulos
nan=df2.isna().any().any()
print('Valores nulos: ', nan)

# Verificando se há valores duplicados
duplicados=df2.duplicated().any()
print('Valores duplicados: ', duplicados)

# Verificando o menor valor, para definir a melhor forma de apresentar os dados
menor_valor = df2[df2["Valor ajustado"] > 0]["Valor ajustado"].min()
print('O menor valor de "Valor ajustado" é: ', menor_valor)

# Verificando o maior valor, para definir a melhor forma de apresentar os dados
maior_valor=df2["Valor ajustado"].max()
print('O maior valor de "Valor ajustado" é: ', maior_valor)

# Verificando quais valores são maior que 0 e menor que 1 milhão, para definir a melhor forma de apresentar os dados
qtde_menor_que_um_milhao = df2[(df2["Valor ajustado"] < 1000000) & (df2["Valor ajustado"] > 0)]
print('Valores maiores que 0 e menores que 1 milhão: ', qtde_menor_que_um_milhao)

# Classificando o dataframe por data
df2=df2.sort_values(by='Data')

## Copiando o dataframe 2 para o dataframe 3
df3=df2.copy()

# Melhorando a visualização dos números
pd.options.display.float_format="{:,.2f}".format

# Dividindo os valores por 1 milhão
df3["Valor ajustado"]=df3["Valor ajustado"]/1000000
df3.rename(columns={'Valor ajustado':'Valor ajustado(R$ Milhões)'},inplace=True)

# Exportando Database filtrado
nome_arquivo=input("Digite o nome do arquivo, sem extensão, que será salvo localmente e no bucket: ")
nome_arquivo=f'{nome_arquivo}.csv'
df3.to_csv(nome_arquivo, index=False, encoding='ISO-8859-1')

## Função para exportar o Database para o S3
def upload_db(nome_arq):
    file_name=nome_arq
    s3_file_name=nome_arq
    try:
        # Carregar o arquivo para o bucket
        s3_client.upload_file(file_name, bucket_name, s3_file_name)
        print(f"Arquivo '{file_name}' carregado com sucesso para o bucket '{bucket_name}' como '{s3_file_name}'")
        # Tratamento de erros
    except Exception as e:
        print(f"Erro ao criar o bucket ou carregar arquivo: {e}")
        # Verificando se o arquivo foi encontrado
        if os.path.exists(f'{nome_arq}.csv'):
            print("O arquivo existe!")
        else:
            print("Arquivo não encontrado.")
# Chama a função para fazer o upload do arquivo para o S3
upload_db(nome_arquivo)

## Função de conversão dos valores: Divide os números a partir do Dataframe 2 por um valor correspondente.
def conversao(valor):
  if valor <= 1e-12: 
    valor_f=valor/1e12
    return f"{valor_f:.3f} trilhões"
  elif valor <= 1e-09:
    valor_f=valor/1e09
    return f"{valor_f:.3f} bilhões"
  elif valor <= 1e-06:
    valor_f=valor/1e06
    return f"{valor_f:.3f} milhões"
  elif valor >= 1e12:                 # Exemplo: Se o número tiver 12 casas ou mais, ele será dividido por 1 trilhão e depois apresentado
    valor_f=valor/1e12
    return f"{valor_f:.3f} trilhões"
  elif valor >= 1e09:
    valor_f=valor/1e09
    return f"{valor_f:.3f} bilhões"
  elif valor >= 1e06:
    valor_f=valor/1e06
    return f"{valor_f:.3f} milhões"
  else:
    return valor

# Verificação do maior valor da coluna 'Valor ajustado'
maior_valor=df2["Valor ajustado"].max() #Necessário utilizar df2, que não contém valores divididos por 1 milhão
maior=conversao(maior_valor)
print('O maior valor + de "Valor ajustado" é: ', maior)

# Menor valor positivo da coluna 'Valor ajustado'
menor_valor_positivo = df2[df2["Valor ajustado"]>0]["Valor ajustado"].min()
menor=conversao(menor_valor_positivo)
print('O menor valor + de "Valor ajustado" é: ', menor)

# Verificando valores únicos para os números das contas e seus respectivos nomes
contagem_Conta = df3['Conta'].nunique()
contagem_NConta = df3['Descrição da conta'].nunique()
print(f'Valores únicos de conta: {contagem_Conta}, Valores únicos de descrição: {contagem_NConta}')

# Verificando quais contas possuem mais de um valor atribuído
contagem = df3.groupby('Descrição da conta')['Conta'].nunique()
contas_com_mais_de_um_numero = contagem[contagem > 1]
print('Contas com mais de um número: ', contas_com_mais_de_um_numero)

## Copiando o dataframe 3 para dataframe 4
df4=df3.copy()

# Função de conversão: Convertendo os dados da coluna 'Origem' para Category
df4['Origem'] = df4['Origem'].astype('category')

## Foi escolhida a conta '87-3' para uma análise mais profunda
# Filtragem de dados utilizando dois operadores lógicos (== e &)
df4_filtro1 = df4[(df4["Conta"] == '87-3') & (df4["Origem"]=='d')]
pd.options.display.float_format="{:,.5f}".format

# Primeira função de agregação, somando os resultados da conta '87-3' por ano
df4_filtro2=df4[(df4['Conta']=='87-3') &
               (df4['Origem'].str.contains('d')) &
               (df4['Data'].dt.year.isin([2021,2022,2023,2024]))]
resultado=df4_filtro2.groupby(df4_filtro2['Data'].dt.year)['Valor ajustado(R$ Milhões)'].sum()

# Convertendo series para Dataframe
if isinstance(resultado, pd.Series):
    resultado = resultado.to_frame().reset_index()

# Segunda função de agregação a partir do DF resultado, agrupando por biênio
df_resultado_final = pd.DataFrame(columns=['Período', 'Somatória(R$ Milhões)'])
somatoria_21_22=resultado.loc[resultado['Data'].isin([2021, 2022]), 'Valor ajustado(R$ Milhões)'].sum()
somatoria_23_24=resultado.loc[resultado['Data'].isin([2023,2024]), 'Valor ajustado(R$ Milhões)'].sum()
df_resultado_final.loc[len(df_resultado_final)] = ['2021-2022', somatoria_21_22]
df_resultado_final.loc[len(df_resultado_final)] = ['2023-2024', somatoria_23_24]

# Adicionando uma observação
df_resultado_final['Período'] = df_resultado_final['Período'].str.replace('2024', '2024*')
df_resultado_final.loc[len(df_resultado_final)] = ['*Observação:', 'Valores até 09-2024']

# Função para obter data atual
def data_atual(data):
  data_atual = datetime.now().date()
  df_resultado_final.loc[len(df_resultado_final)] = [f'Até {data_atual}', 'não há novos dados']
  return df_resultado_final

# Teste de condição para adicionar ou substituir por uma data atual
if len(df_resultado_final) <= 3:
  df_resultado_final=data_atual(df_resultado_final)
else:
   df_resultado_final=df_resultado_final.drop(df_resultado_final.index[-1])
   df_resultado_final=data_atual(df_resultado_final)
df_resultado_final

# Convertendo o dataframe 'resultado_final' para um csv
nome_arquivo=input("Digite o nome do segundo arquivo, sem extensão, que será salvo localmente e no bucket: ")
nome_arquivo=f'{nome_arquivo}.csv'
df_resultado_final.to_csv(nome_arquivo, index=False, encoding='ISO-8859-1')
# Chamada da função para salvar o arquivo no S3
upload_db(nome_arquivo)

# Upload dos scripts para o bucket no S3
nome_script1='Bucket.py'
nome_script2='Desafio5.py'
upload_db(nome_script1)
upload_db(nome_script2)