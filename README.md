# data-engineering-zoomcamp-2026
Workshop Codespaces

## Question 1. Understanding Docker images

Command:

```bash
docker run -it --rm --entrypoint=bash python:3.13
pip --version
```

Output:

```
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```

**Answer:** 25.3

---

## Question 2. Docker networking and docker-compose

pgAdmin connects to Postgres using the Docker Compose internal network.
The hostname is the service name and the port is the container port.

**Answer:** db:5432

---

## Question 3. Counting short trips

```sql
SELECT COUNT(*) 
FROM green_tripdata_2025_11
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
```

**Answer:** 8007

---

## Question 4. Longest trip for each day

```sql
SELECT
    DATE(lpep_pickup_datetime) AS pickup_date,
    MAX(trip_distance) AS max_trip_distance
FROM green_tripdata_2025_11
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_trip_distance DESC
LIMIT 1;
```

**Answer:** 2025-11-14

---

## Question 5. Biggest pickup zone

```sql
SELECT
    z."Zone" AS pickup_zone,
    SUM(g.total_amount) AS total_amount_sum
FROM green_tripdata_2025_11 g
JOIN taxi_zone_lookup z
    ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_amount_sum DESC
LIMIT 1;
```

**Answer:** East Harlem North

---

## Question 6. Largest tip

```sql
SELECT
    dz."Zone" AS dropoff_zone,
    MAX(g.tip_amount) AS max_tip
FROM green_tripdata_2025_11 g
JOIN taxi_zone_lookup pz
  ON g."PULocationID" = pz."LocationID"
JOIN taxi_zone_lookup dz
  ON g."DOLocationID" = dz."LocationID"
WHERE g.lpep_pickup_datetime >= '2025-11-01'
  AND g.lpep_pickup_datetime <  '2025-12-01'
  AND pz."Zone" = 'East Harlem North'
GROUP BY dz."Zone"
ORDER BY max_tip DESC
LIMIT 1;
```

**Answer:** Yorkville West

---

## Question 7. Terraform Workflow

**Answer:** terraform init, terraform apply -auto-approve, terraform destroy

---