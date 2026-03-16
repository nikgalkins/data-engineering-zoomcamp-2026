import json
from time import time

import pandas as pd
from kafka import KafkaProducer

TOPIC = "green-trips"
BOOTSTRAP_SERVERS = ["localhost:9092"]
DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet"

COLUMNS = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "tip_amount",
    "total_amount",
]


def to_json_bytes(value: dict) -> bytes:
    return json.dumps(value).encode("utf-8")


def main() -> None:
    df = pd.read_parquet(DATA_URL, columns=COLUMNS).copy()

    for col in ["lpep_pickup_datetime", "lpep_dropoff_datetime"]:
        df[col] = pd.to_datetime(df[col]).dt.strftime("%Y-%m-%d %H:%M:%S")

    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=to_json_bytes,
    )

    t0 = time()

    for row in df.itertuples(index=False, name=None):
        message = dict(zip(COLUMNS, row))
        producer.send(TOPIC, value=message)

    producer.flush()

    t1 = time()
    print(f"rows sent: {len(df)}")
    print(f"took {(t1 - t0):.2f} seconds")


if __name__ == "__main__":
    main()