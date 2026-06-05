from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("gold").getOrCreate()

ticker = "aapl"

df_silver1 = f"data/silver/{ticker}_silver.parquet"
df_silver = spark.read.parquet(df_silver1)

df_with_year = df_silver.withColumn("Year", F.year("Date"))

df_gold = df_with_year.groupBy("Year").agg(F.round(F.avg("Close"), 2).alias("Average_Close_Price"), F.sum("Volume").alias("Sum_Of_Volume"))

# df_gold.show()

df_gold.write.mode("overwrite").parquet(f"data/gold/{ticker}_gold.parquet")