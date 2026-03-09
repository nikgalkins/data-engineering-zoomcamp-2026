import os

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
os.environ["SPARK_USER"] = os.environ.get("USER", "spark")
from pathlib import Path
from pyspark.sql import SparkSession, functions as F

spark = (
    SparkSession.builder
    .appName("de-zoomcamp-hw6")
    .master("local[*]")
    .getOrCreate()
)

# Q1
print(f"Q1 Spark version: {spark.version}")

# Load main dataset
df = spark.read.parquet("yellow_tripdata_2025-11.parquet")

# Q2
out_path = "yellow_nov_2025_repartitioned"
df.repartition(4).write.mode("overwrite").parquet(out_path)

parquet_files = sorted(Path(out_path).glob("*.parquet"))
sizes_mb = [f.stat().st_size / (1024 * 1024) for f in parquet_files]
avg_mb = sum(sizes_mb) / len(sizes_mb)

print("Q2 parquet file sizes (MB):", [round(x, 2) for x in sizes_mb])
print("Q2 average parquet size (MB):", round(avg_mb, 2))

# Q3
q3 = (
    df.filter(F.to_date(F.col("tpep_pickup_datetime")) == F.lit("2025-11-15"))
      .count()
)
print(f"Q3 count records: {q3}")

# Q4
q4 = (
    df.withColumn(
        "trip_hours",
        (
            F.unix_timestamp("tpep_dropoff_datetime")
            - F.unix_timestamp("tpep_pickup_datetime")
        ) / 3600.0
    )
    .agg(F.max("trip_hours").alias("max_trip_hours"))
    .first()["max_trip_hours"]
)
print(f"Q4 longest trip hours: {q4}")

# Q5
print("Q5 Spark UI port: 4040")

# Q6
zones = (
    spark.read.option("header", True)
    .csv("taxi_zone_lookup.csv")
    .withColumn("LocationID", F.col("LocationID").cast("int"))
)

q6_df = (
    df.groupBy("PULocationID")
      .agg(F.count("*").alias("trip_count"))
      .join(zones, df.PULocationID == zones.LocationID, "left")
      .select("PULocationID", "Zone", "trip_count")
      .orderBy(F.col("trip_count").asc(), F.col("Zone").asc())
)

q6_df.show(20, truncate=False)
print(f"Q6 least frequent pickup zone: {q6_df.first()['Zone']}")

spark.stop()