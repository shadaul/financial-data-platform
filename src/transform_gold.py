from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("gold").getOrCreate()

df_silver1 = "data/silver/aapl_silver.parquet"
df_silver = spark.read.parquet(df_silver1)

df_with_year = df_silver.withColumn("Year", F.year("Date"))

df_gold = df_with_year.groupBy("Year").agg(F.avg("Close").alias("Average_Close_Price"), F.sum("Volume").alias("Sum_Of_Volume"))

# df_gold.show()

df_gold.write.mode("overwrite").parquet("data/gold/aapl_gold.parquet")