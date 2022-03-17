from pyspark.sql import SparkSession
from pyspark.sql.functions import col, min, max

# Cria objeto da Spark Session
spark = (SparkSession.builder.appName("DeltaExercise")
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0")
    # .config("spark.jars.packages", "io.delta:delta-core_2.12:1.1.0")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

# Importa o modulo das tabelas delta
from delta.tables import *

#Ler os dados do RAIS 2020
rais = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-helton-739010676765/raw-data/rais/")
)

# Escreve a tabela em staging em formato delta
print("Writing delta table...")
(
    rais
    .write
    .mode("overwrite")
    .format("delta")
    ##vai ter q arrumar pastas, partições por ano...
    # .partitionBy("year")
    .save("s3://edc-desafio-mod1-helton-tf/staging-zone/rais/")
)