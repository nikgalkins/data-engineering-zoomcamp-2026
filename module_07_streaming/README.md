# Module 7 — Stream Processing

Homework 7 for Data Engineering Zoomcamp 2026.

## Structure

```text
module_07_streaming/
├── README.md
└── workshop/
    ├── docker-compose.yml
    ├── Dockerfile.flink
    ├── pyproject.flink.toml
    ├── flink-config.yaml
    ├── producer_green.py
    ├── check_answers_local.py
    └── src/
        └── job/
            ├── q4_job.py
            ├── q5_job.py
            └── q6_job.py
```
## Setup

From module_07_streaming/workshop:
```bash
docker compose build
docker compose up -d
docker exec -it workshop-redpanda-1 rpk topic create green-trips
python producer_green.py
python check_answers_local.py
```

## Homework answers

- Q1: v25.3.9
- Q2: 10 seconds
- Q3: 8506
- Q4: 74
- Q5: 81
- Q6: 2025-10-16 18:00:00

## Notes

- producer_green.py reads the October 2025 Green Taxi parquet file and sends records to the green-trips topic.
- check_answers_local.py was used as a local validation script.
- The homework environment is based on the workshop infrastructure with Redpanda, Flink, and PostgreSQL.