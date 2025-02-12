import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, lower
from pyspark.sql.types import IntegerType, StringType, FloatType


## @params: [JOB_NAME, S3_INPUT_PATH_SERIES, S3_TARGET_PATH_SERIES]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_SERIES', 'S3_TARGET_PATH_SERIES'])

# Criar contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos dos dados no S3 (camada Trusted)
csv_path = args['S3_INPUT_PATH_SERIES']

# Caminho do bucket no S3
s3_output_path = args['S3_TARGET_PATH_SERIES']

# Ler os dados CSV do S3 advindos da camada Trusted
df_csv = spark.read.parquet(csv_path)

# Corrigir o nome da coluna "tituloPrincipal"
df_csv = df_csv.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Selecionar as colunas necessárias do CSV
df_series = df_csv.select(
    df_csv["id"].alias("id_serie"),  # Renomeia a coluna para 'id_serie'
    df_csv["tituloPrincipal"],
    df_csv["tituloOriginal"],
    df_csv["anoLancamento"],
    df_csv["anoTermino"],
    df_csv["genero"],
    df_csv["notaMedia"],
)

# Normalizar a coluna 'genero' para minúsculas e filtrar séries cujo gênero contenha "animation" ou "comedy"
df_series = df_series.withColumn("genero", lower(col("genero")))  # Converte para minúsculas
df_series = df_series.filter(
    (col("genero").contains("animation")) | (col("genero").contains("comedy"))
)

# Conversão de tipos e seleção dos atributos
df_series = df_series.select(
    col("id_serie").cast(StringType()),
    col("tituloprincipal").cast(StringType()),
    col("genero").cast(StringType()),
    col("anolancamento").cast(IntegerType()),
    col("anotermino").cast(IntegerType()),
    col("notamedia").cast(FloatType())
)

# Criando Dataframe para a dimensão "Titulo"
df_dim_titulo = df_series.select("id_serie", "tituloprincipal", "genero").dropDuplicates()

# Criando Dataframe para fato_series
df_fato_series = df_series.select("id_serie", "anolancamento", "anotermino", "notamedia")

# Convertendo para DynamicFrame
df_dim_titulo_dyf = DynamicFrame.fromDF(df_dim_titulo, glueContext, "df_dim_titulo_dyf")
df_fato_series_dyf = DynamicFrame.fromDF(df_fato_series, glueContext, "df_fato_series_dyf")

# Salvando os dados no S3 com o caminho correto em formato Parquet
df_dim_titulo_dyf.toDF().write.mode("overwrite").parquet(s3_output_path + "/dim_titulo/")
df_fato_series_dyf.toDF().write.mode("overwrite").parquet(s3_output_path + "/fato_series/")

job.commit()