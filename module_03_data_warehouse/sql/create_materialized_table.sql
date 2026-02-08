-- Create materialized BigQuery table from external table

CREATE OR REPLACE TABLE `ny_taxi.yellow_tripdata_mat` AS
SELECT *
FROM `ny_taxi.external_yellow_tripdata`;
