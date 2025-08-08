from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

spark.sql('USE CATALOG development_aax')
spark.sql('USE SCHEMA dbt_test')

spark.sql('SHOW views in development_aax.dbt_test')
