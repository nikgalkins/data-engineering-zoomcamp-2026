# Module 06 — Batch Processing with Spark

This module contains my solution for **Homework 6** from **Data Engineering Zoomcamp 2026**.

## Objective

Practice batch processing with **PySpark** using NYC Yellow Taxi trip data for **November 2025**.

The homework covers:

- installing and running Spark / PySpark
- reading parquet data
- repartitioning datasets
- calculating file sizes after repartition
- filtering records by pickup date
- computing longest trip duration
- identifying the least frequent pickup zone

## Dataset

Main dataset:

- `yellow_tripdata_2025-11.parquet`

Zone lookup:

- `taxi_zone_lookup.csv`

## Project structure

```text
module_06_batch/
├── README.md
└── homework/
    ├── hw6.py
    ├── taxi_zone_lookup.csv
    └── yellow_nov_2025_repartitioned/
```

## Environment

Used stack:

- Python
- PySpark 3.5.5
- Java 17

## How to run

From the repository root:

```bash
cd module_06_batch/homework
python hw6.py
```

## Homework answers

Results obtained from the script:

- Q1: 3.5.5
- Q2: 25MB
- Q3: 162604
- Q4: 90.6
- Q5: 4040
- Q6: Arden Heights

## Notes

While running Spark in GitHub Codespaces, I had to use Java 17 to avoid Spark startup issues related to the Java security context.

## Author

Repository owner: Nikita Galkin
EOF