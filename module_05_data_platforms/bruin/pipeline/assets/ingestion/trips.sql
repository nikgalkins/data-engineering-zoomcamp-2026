/* @bruin

name: ingestion.trips
type: duckdb.sql

materialization:
  type: table

@bruin */

with src as (
  select *, 'yellow' as taxi_type
  from read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet')
  union all
  select *, 'yellow' as taxi_type
  from read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-02.parquet')
  union all
  select *, 'yellow' as taxi_type
  from read_parquet('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-03.parquet')
)
select * from src;