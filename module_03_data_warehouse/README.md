# Module 3 Homework — Data Warehousing & BigQuery

This repository contains my solution for **Module 3: Data Warehousing & BigQuery**
from the **Data Engineering Zoomcamp 2026** by DataTalksClub.

---

## 📊 Dataset

- **NYC Yellow Taxi Trip Records**
- Period: **January–June 2024**
- Source: NYC Taxi & Limousine Commission
- Format: **Parquet**
- Storage: **Google Cloud Storage (GCS)**

---

## 🏗️ Setup

### 1. Upload data to GCS
Taxi parquet files (January–June 2024) were downloaded from the official NYC TLC
public source and uploaded to a personal GCS bucket.

### 2. External table
An **external table** was created in BigQuery referencing parquet files in GCS.

### 3. Materialized table
A **materialized BigQuery table** was created from the external table  
(no partitioning or clustering).

---

## 🧾 SQL used in this homework

### Create external table
```sql
CREATE OR REPLACE EXTERNAL TABLE `ny_taxi.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de-zoomcamp-nytaxi-1/yellow_tripdata_2024-*.parquet']
);
```

### Create materialized table
```sql
CREATE OR REPLACE TABLE `ny_taxi.yellow_tripdata_mat` AS
SELECT *
FROM `ny_taxi.external_yellow_tripdata`;
```

### Question 1 — Count records
```sql
SELECT COUNT(*)
FROM `ny_taxi.yellow_tripdata_mat`;
```
- **Answer:** 20,332,093 records

### Question 2 — Data read estimation
- **External table:** 18.82 MB
- **Materialized table:** 47.60 MB

(Estimated bytes processed, observed before query execution)

### Question 3 — Columnar storage
BigQuery scans only requested columns.  
Querying two columns requires reading more data than querying one.

### Question 4 — Zero fare trips
```sql
SELECT COUNT(*)
FROM `ny_taxi.yellow_tripdata_mat`
WHERE fare_amount = 0;
```
- **Answer:** 8,333 records

### Question 5 — Optimization strategy
- **Partition:** `tpep_dropoff_datetime`
- **Cluster:** `VendorID`

```sql
CREATE OR REPLACE TABLE `ny_taxi.yellow_tripdata_part`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT *
FROM `ny_taxi.yellow_tripdata_mat`;
```

### Question 6 — Partition benefits
- **Non-partitioned table:** 310.24 MB scanned
- **Partitioned table:** 26.84 MB scanned
```sql
SELECT DISTINCT VendorID
FROM `ny_taxi.yellow_tripdata_part`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```

### Question 7 — External table storage
- **Answer:** Google Cloud Storage (GCS)

### Question 8 — Clustering best practices
- **Answer:** False  
  (Clustering is not always beneficial and depends on query patterns.)

### Question 9 — COUNT(*) scan
`SELECT COUNT(*)` scans almost no data because BigQuery uses table metadata.

---

## 🛠️ Technologies Used

- Google BigQuery
- Google Cloud Storage
- SQL
- Parquet

---

## 📎 Notes

This homework demonstrates:
- External vs internal tables
- Columnar storage behavior
- Query cost estimation
- Partitioning and clustering optimization

---

## 🔗 Course

Data Engineering Zoomcamp 2026  
https://github.com/DataTalksClub/data-engineering-zoomcamp
