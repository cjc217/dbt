from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

views = spark.sql('SHOW VIEWS IN dbt_test;')

views.show()
