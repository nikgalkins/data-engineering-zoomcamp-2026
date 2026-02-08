-- Q1: Count total records
SELECT COUNT(*)
FROM `ny_taxi.yellow_tripdata_mat`;

-- Q2: Data read estimation (check estimated bytes before execution)
SELECT COUNT(DISTINCT PULocationID)
FROM `ny_taxi.external_yellow_tripdata`;

SELECT COUNT(DISTINCT PULocationID)
FROM `ny_taxi.yellow_tripdata_mat`;

-- Q4: Zero fare trips
SELECT COUNT(*)
FROM `ny_taxi.yellow_tripdata_mat`
WHERE fare_amount = 0;

-- Create partitioned & clustered table (Q5)
CREATE OR REPLACE TABLE `ny_taxi.yellow_tripdata_part`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT *
FROM `ny_taxi.yellow_tripdata_mat`;

-- Q6: Partition benefits
SELECT DISTINCT VendorID
FROM `ny_taxi.yellow_tripdata_part`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
