import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, upper

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

#Iniciando o job com o glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#Definição dos paths de input e target
source_file=args['S3_INPUT_PATH']
target_path=args['S3_TARGET_PATH']

#Leitura do arquivo csv
dfg = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": ","}
)

#Transformar os dados no formato parquet
glueContext.write_dynamic_frame.from_options(
    frame = dfg,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
)

#Imprimir esquema
df = dfg.toDF()
df.printSchema()

#Alterar valores de nome para maiúsculo
df = df.withColumn('nome', upper(col('nome')))

#Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo
nomes = (df.groupBy('nome','sexo','ano').count().orderBy(col('ano').desc()))
nomes.show()

#Nome feminino com mais registros e em que ano ocorreu
nome_feminino = (df.filter(col('sexo') == 'F').groupBy('ano', 'nome').count().orderBy(col('count').desc()))
resultado = nome_feminino.first()
print(f"Nome feminino com mais registros: '{resultado['nome']}'")
print(f"Ano: {resultado['ano']}, Ocorrências: {resultado['count']}")

#Nome masculino com mais registros e em que ano ocorreu
nome_masculino = (df.filter(col('sexo') == 'M').groupBy('ano', 'nome').count().orderBy(col('count').desc()))
resultado = nome_masculino.first()
print(f"Nome masculino com mais registros: '{resultado['nome']}'")
print(f"Ano: {resultado['ano']}, Ocorrências: {resultado['count']}")

#Total de registros (masculinos e femininos) para cada ano presente no dataframe. 10 primeiras linhas
total_ano = (df.groupBy('ano', 'sexo').count().orderBy('ano'))
resultado = total_ano.limit(10)
resultado.show()

#Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3
output_path = "s3://s7-exercicio-glue/lab-glue/frequencia_registro_nomes_eua"
df.write \
    .format('json') \
    .mode('overwrite') \
    .partitionBy('sexo', 'ano') \
    .save(output_path)
print(f"Dados armazenados com sucesso em {output_path}")

job.commit()