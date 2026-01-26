import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5433/ny_taxi"
)

zones = pd.read_csv("taxi_zone_lookup.csv")

zones.to_sql(
    "taxi_zone_lookup",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded taxi_zone_lookup")
