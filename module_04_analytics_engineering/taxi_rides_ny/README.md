# Module 04 — Analytics Engineering (dbt) — Homework Solutions

This repo contains the setup and results for DataTalksClub Data Engineering Zoomcamp (cohort 2026) Module 04 homework.

## Environment

- Warehouse: BigQuery (US)
- Project: `project-c5e83f31-a78d-40f0-828`
- Raw dataset: `ny_taxi`
- Prod dataset: `ny_taxi_prod`
- dbt version: 1.11.5
- Environment variable:
  export GCP_PROJECT_ID=project-c5e83f31-a78d-40f0-828

## 1) dbt project

Upstream/canonical dbt project was used:

`data-engineering-zoomcamp/04-analytics-engineering/taxi_rides_ny`

Profile name in `dbt_project.yml`:
- `profile: taxi_rides_ny`

### dbt targets

`~/.dbt/profiles.yml` includes:
- `dev` -> dataset `ny_taxi`
- `prod` -> dataset `ny_taxi_prod`

Prod dataset created:
```bash
bq mk --dataset --location=US project-c5e83f31-a78d-40f0-828:ny_taxi_prod
```

## 2) Data loading
### Yellow 2019–2020 (releases)
Downloaded from:
https://github.com/DataTalksClub/nyc-tlc-data/releases

Loaded into:
project-c5e83f31-a78d-40f0-828.ny_taxi.yellow_tripdata

### Green 2019–2020 (releases)

Loaded into:
project-c5e83f31-a78d-40f0-828.ny_taxi.green_tripdata

### FHV 2019 (releases)

Loaded into:
project-c5e83f31-a78d-40f0-828.ny_taxi.fhv_tripdata

## 3) Build (prod)
```bash
cd module_04_analytics_engineering/taxi_rides_ny
dbt build --target prod --full-refresh
```

## 4) Homework answers

### Q1. dbt Lineage and Execution

Command:
```bash
dbt run --select int_trips_unioned
```

Answer:

- stg_green_tripdata, stg_yellow_tripdata, and int_trips_unioned (upstream dependencies)

### Q2. dbt Tests

accepted_values test for payment_type, allowed [1,2,3,4,5].
If value 6 appears in source:

Answer:

- dbt test --select fct_trips fails and returns a non-zero exit code

### Q3. Counting Records in fct_monthly_zone_revenue (prod)

```sql
SELECT COUNT(*)
FROM `project-c5e83f31-a78d-40f0-828.ny_taxi_prod.fct_monthly_zone_revenue`;
```

Answer:

- 12,184

### Q4. Best performing Green zone (2020)

```sql
SELECT
  pickup_zone,
  SUM(revenue_monthly_total_amount) AS total_revenue
FROM `project-c5e83f31-a78d-40f0-828.ny_taxi_prod.fct_monthly_zone_revenue`
WHERE service_type = "Green"
  AND EXTRACT(YEAR FROM revenue_month) = 2020
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
```

Answer:
- East Harlem North

### Q5. Green taxi trip counts (October 2019)

```sql
SELECT
  SUM(total_monthly_trips) AS trips
FROM `project-c5e83f31-a78d-40f0-828.ny_taxi_prod.fct_monthly_zone_revenue`
WHERE service_type = "Green"
  AND revenue_month = DATE("2019-10-01");
```

Answer:
- 384,624

### Q6. stg_fhv_tripdata record count (2019)

```sql
SELECT COUNT(*) AS cnt
FROM `project-c5e83f31-a78d-40f0-828.ny_taxi_prod.stg_fhv_tripdata`;
```

Answer:
- 43,244,693
---