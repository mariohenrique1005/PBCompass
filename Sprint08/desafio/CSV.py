# Importação das bibliotecas necessárias
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col

## @params: [JOB_NAME] Parâmetros para iniciar o job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_MOVIES', 'S3_INPUT_PATH_SERIES', 'S3_TARGET_PATH_MOVIES', 'S3_TARGET_PATH_SERIES'])

# Inicialização dos serviços Glue e Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Definição dos paths de input e target para movies e series
source_movies = args['S3_INPUT_PATH_MOVIES']
source_series = args['S3_INPUT_PATH_SERIES']
target_path_movies = args['S3_TARGET_PATH_MOVIES']
target_path_series = args['S3_TARGET_PATH_SERIES']

# Imprimir o caminho de entrada para movies e series
print(f"Path de entrada para movies: {source_movies}")
print(f"Path de entrada para series: {source_series}")

# Função para limpar inconsistências
def clean_dataframe(df, num_cols):
    # Verifica o número de colunas do DataFrame
    if len(df.columns) != num_cols:
        raise ValueError("O número de colunas do DataFrame não corresponde ao esperado.")
    # Remove linhas nulas
    df_clean = df.dropna()
    return df_clean

# Leitura do arquivo csv movies
df_movies = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_movies]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

# Conversão para DataFrame para processamento de inconsistências
spark_movies_df = df_movies.toDF()

# Define o número esperado de colunas para o dataset de movies
num_colunas_movies = len(spark_movies_df.columns)

# Filtrando linhas inconsistentes de movies
df_movies_clean = clean_dataframe(spark_movies_df, num_colunas_movies)

# Convertendo o dataframe movies de volta para DynamicFrame
movies_clean_dyf = DynamicFrame.fromDF(df_movies_clean, glueContext, "movies_clean_dyf")

# Transformar os dados de movies no formato parquet
glueContext.write_dynamic_frame.from_options(
    frame=movies_clean_dyf,
    connection_type="s3",
    connection_options={"path": target_path_movies},
    format="parquet"
)

# Leitura do arquivo csv series
df_series = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_series]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

# Conversão para DataFrame para processamento de inconsistências
spark_series_df = df_series.toDF()

# Define o número esperado de colunas para o dataset de series
num_colunas_series = len(spark_series_df.columns)

# Filtrando linhas inconsistentes de series
df_series_clean = clean_dataframe(spark_series_df, num_colunas_series)

# Convertendo o dataframe series de volta para DynamicFrame
series_clean_dyf = DynamicFrame.fromDF(df_series_clean, glueContext, "series_clean_dyf")

# Transformar os dados de series no formato parquet
glueContext.write_dynamic_frame.from_options(
    frame=series_clean_dyf,
    connection_type="s3",
    connection_options={"path": target_path_series},
    format="parquet"
)

job.commit()