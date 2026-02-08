-- Create external table over Yellow Taxi 2024 parquet files in GCS

CREATE OR REPLACE EXTERNAL TABLE `ny_taxi.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de-zoomcamp-nytaxi-1/yellow_tripdata_2024-*.parquet']
);
