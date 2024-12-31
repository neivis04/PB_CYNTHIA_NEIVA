import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
from datetime import datetime
import boto3

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializando o contexto do Spark e do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho do arquivo de entrada no S3
input_path = 's3://desafio.sprint07/data-lake-da-cynthia/raw/TMDB/JSON/Movies/2024/12/17/filmes_comedia_animacao_2024-12-17.json'

# Caminho do bucket de saída
output_bucket = 's3://desafio.sprint08/data-lake-cynthia/trusted/parquet/movies/'

# Nome final do arquivo Parquet
output_file_name = "filmes_comedia_animacao_2024-12-30.parquet"

# Lendo o arquivo JSON em um DataFrame
df = spark.read.option("multiline", "true").json(input_path)

# Exibindo o esquema do DataFrame
df.printSchema()

# Tratamento de dados
# Excluir linhas nulas
df_cleaned = df.na.drop()

# Excluir linhas onde a coluna 'overview' está vazia
df_cleaned = df_cleaned.filter(col('overview') != '')

# Converter a coluna 'release_date' para datetime
df_cleaned = df_cleaned.withColumn('release_date', col('release_date').cast('date'))

# Adicionar as colunas de data para facilitar o particionamento
now = datetime.now()
year = now.year
month = now.month
day = now.day

# Definindo o caminho para salvar os dados tratados
output_path_parquet = f"{output_bucket}{year}/{month}/{day}/"

# Consolidando os dados em um único arquivo
df_single_file = df_cleaned.coalesce(1)

# Salvando o DataFrame tratado como Parquet com o nome especificado
df_single_file.write.mode('overwrite').parquet(output_path_parquet)

# Renomeando o arquivo para o nome especificado
s3 = boto3.resource('s3')
bucket_name = output_bucket.split('/')[2]
bucket = s3.Bucket(bucket_name)

# Listando o arquivo gerado na pasta temporária
for obj in bucket.objects.filter(Prefix=f"{year}/{month}/{day}/"):
    if obj.key.endswith(".parquet"):
        source_key = obj.key
        destination_key = f"{year}/{month}/{day}/{output_file_name}"
        s3.Object(bucket_name, destination_key).copy_from(CopySource=f"{bucket_name}/{source_key}")
        s3.Object(bucket_name, source_key).delete()  # Removendo o arquivo temporário

print(f"Arquivo final salvo como: {output_file_name}")

# Finalizando o trabalho
job.commit()
