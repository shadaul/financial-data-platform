from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import sys
import os

def process_gold(ticker):
    spark = SparkSession.builder.appName("gold").getOrCreate()

    df_silver1 = f"data/silver/{ticker.lower()}_silver.parquet"
    df_silver = spark.read.parquet(df_silver1)

    df_with_year = df_silver.withColumn("Year", F.year("Date"))

    df_gold = df_with_year.groupBy("Year").agg(F.round(F.avg("Close"), 2).alias("Average_Close_Price"), F.sum("Volume").alias("Sum_Of_Volume"))

    # df_gold.show()

    os.makedirs("data/gold", exist_ok=True)
    df_gold.write.mode("overwrite").parquet(f"data/gold/{ticker.lower()}_gold.parquet")

if __name__ == "__main__":
    user_ticker = sys.argv[1]
    process_gold(user_ticker)