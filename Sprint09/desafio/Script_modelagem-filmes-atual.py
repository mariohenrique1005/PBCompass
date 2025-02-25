import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql.functions import col, lower, monotonically_increasing_id
from pyspark.sql.types import StringType, IntegerType, FloatType
from pyspark.sql.functions import hash, abs

## @params: [JOB_NAME, S3_INPUT_PATH_MOVIES_CSV, S3_INPUT_PATH_MOVIES_JSON, S3_TARGET_PATH_MOVIES]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_MOVIES_CSV', 'S3_INPUT_PATH_MOVIES_JSON', 'S3_TARGET_PATH_MOVIES'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos dos dados no S3 (camada Trusted)
csv_path = args['S3_INPUT_PATH_MOVIES_CSV']
json_path = args['S3_INPUT_PATH_MOVIES_JSON']

# Caminho de saída para o S3
s3_output_path = args['S3_TARGET_PATH_MOVIES']

# Ler os dados diretamente do S3 (camada Trusted)
df_csv = spark.read.parquet(csv_path)
df_json = spark.read.parquet(json_path)

# Corrigir o nome da coluna (se necessário)
df_csv = df_csv.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Selecionar apenas as colunas necessárias do CSV
df_csv_selected = df_csv.select(
    df_csv["id"].alias("id_filme"),  # Renomeia 'id' para 'id_filme'
    df_csv["tituloPrincipal"],
    df_csv["tituloOriginal"],
    df_csv["anoLancamento"],
    df_csv["tempoMinutos"],
    df_csv["genero"],
    df_csv["notaMedia"],
    df_csv["numeroVotos"],
    df_csv["nomeArtista"],
    df_csv["profissao"]
)

# Selecionar apenas as colunas necessárias do JSON
df_json_selected = df_json.select(
    df_json["Id_IMDB"].alias("id_filme"),  # Renomeia 'Id_IMDB' para 'id_filme'
    df_json["Orcamento"],
    df_json["Bilheteria"]
)

# Normalizar a coluna 'genero' para minúsculas e filtrar filmes cujo gênero contenha "animação" ou "comédia"
df_csv_selected = df_csv_selected.withColumn("genero", lower(col("genero")))  # Converte para minúsculas
df_csv_selected = df_csv_selected.filter(
    (col("genero").contains("animation")) | (col("genero").contains("comedy"))
)

# Juntar os dataframes usando 'id_filme' como chave de join
df_filmes = df_csv_selected.join(df_json_selected, "id_filme", "left")

# Definição de schema correto conforme seu modelo
df_filmes = df_filmes.select(
    col("id_filme").cast(StringType()),
    col("tituloprincipal").cast(StringType()),
    col("titulooriginal").cast(StringType()),
    col("anolancamento").cast(IntegerType()),
    col("tempominutos").cast(IntegerType()),
    col("genero").cast(StringType()),
    col("notamedia").cast(FloatType()),
    col("numerovotos").cast(IntegerType()),
    col("nomeartista").cast(StringType()),
    col("profissao").cast(StringType()),
    col("orcamento").cast(IntegerType()),
    col("bilheteria").cast(IntegerType())
)

# Criando ID único para artistas
df_artistas = (
    df_filmes.select("nomeartista", "profissao", "id_filme")
    .distinct()
    .withColumn("id_artista", abs(hash("nomeartista", "profissao")))
)

# Criando DataFrames para dimensões
df_dim_filme = df_filmes.select("id_filme", "tituloprincipal", "genero").dropDuplicates()
df_dim_artista = df_artistas.select("id_artista", "id_filme", "nomeartista", "profissao").dropDuplicates()

# Criando DataFrame para fato (Fato_Filme)
df_fato_filme = df_filmes.select(
    "id_filme",
    "anolancamento",
    "notamedia",
    "numerovotos",
    "tempominutos",
    "orcamento",
    "bilheteria"
).dropDuplicates(["id_filme"])  # Garante que cada filme apareça apenas uma vez

# Convertendo de DataFrame do Spark para DynamicFrame do Glue
df_dim_filme_dyf = DynamicFrame.fromDF(df_dim_filme, glueContext, "df_dim_filme_dyf")
df_dim_artista_dyf = DynamicFrame.fromDF(df_dim_artista, glueContext, "df_dim_artista_dyf")
df_fato_filme_dyf = DynamicFrame.fromDF(df_fato_filme, glueContext, "df_fato_filme_dyf")

# Salvando os dados no S3 em formato Parquet
df_dim_filme.write.mode("overwrite").parquet(s3_output_path + "dim_filme/")
df_dim_artista.write.mode("overwrite").parquet(s3_output_path + "dim_artista/")
df_fato_filme.write.mode("overwrite").parquet(s3_output_path + "fato_filme/")

job.commit()