import pandas as pd

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


def main() -> None:
    df = pd.read_parquet(DATA_URL, columns=COLUMNS).copy()

    df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
    df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])

    # Q3
    q3 = int((df["trip_distance"] > 5).sum())
    print(f"Q3 trips with trip_distance > 5: {q3}")

    # Q4
    q4 = (
        df.dropna(subset=["lpep_pickup_datetime", "PULocationID"])
        .assign(window_start=lambda x: x["lpep_pickup_datetime"].dt.floor("5min"))
        .groupby(["window_start", "PULocationID"], as_index=False)
        .size()
        .rename(columns={"size": "num_trips"})
        .sort_values(["num_trips", "PULocationID"], ascending=[False, True])
    )

    print("\nQ4 top 10:")
    print(q4.head(10).to_string(index=False))
    print(f"Q4 answer PULocationID: {int(q4.iloc[0]['PULocationID'])}")

    # Q5
    sessions = (
        df.dropna(subset=["PULocationID", "lpep_pickup_datetime"])
        .loc[:, ["PULocationID", "lpep_pickup_datetime"]]
        .sort_values(["PULocationID", "lpep_pickup_datetime"])
        .copy()
    )

    session_break = (
        sessions.groupby("PULocationID")["lpep_pickup_datetime"]
        .diff()
        .gt(pd.Timedelta(minutes=5))
        .fillna(True)
    )

    sessions["new_session"] = session_break.astype(int)
    sessions["session_id"] = sessions.groupby("PULocationID")["new_session"].cumsum()

    q5 = (
        sessions.groupby(["PULocationID", "session_id"], as_index=False)
        .size()
        .rename(columns={"size": "num_trips"})
        .sort_values(["num_trips", "PULocationID"], ascending=[False, True])
    )

    print("\nQ5 top 10:")
    print(q5.head(10).to_string(index=False))
    print(f"Q5 answer longest session trips: {int(q5.iloc[0]['num_trips'])}")

    # Q6
    q6 = (
        df.dropna(subset=["lpep_pickup_datetime", "tip_amount"])
        .assign(window_start=lambda x: x["lpep_pickup_datetime"].dt.floor("1h"))
        .groupby("window_start", as_index=False)["tip_amount"]
        .sum()
        .rename(columns={"tip_amount": "total_tip_amount"})
        .sort_values(["total_tip_amount", "window_start"], ascending=[False, True])
    )

    print("\nQ6 top 10:")
    print(q6.head(10).to_string(index=False))
    print(f"Q6 answer hour: {q6.iloc[0]['window_start']}")


if __name__ == "__main__":
    main()