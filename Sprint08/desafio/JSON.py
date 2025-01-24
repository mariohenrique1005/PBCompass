import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] Parâmetros para iniciar o job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicialização dos serviços Glue e Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Definição dos caminhos de entrada e saída para os arquivos
source_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Ler os arquivos JSON da pasta de entrada com multiline=True para arrays JSON
df_jsons = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_path]},
    format="json",
    format_options={"multiline": True}  # Importante para JSON em formato de array
)

# Transformar o DynamicFrame df_jsons em DataFrame para processamento adicional
dataframe = df_jsons.toDF()

# Remover registros com valores nulos
dataframe_clean = dataframe.dropna()

# Remover registros duplicados, baseado em todas as colunas
dataframe_clean = dataframe_clean.dropDuplicates()

# Transformar o Dataframe limpo em arquivo do formato Parquet no S3
dataframe_clean.write.mode("overwrite").parquet(target_path)

job.commit()