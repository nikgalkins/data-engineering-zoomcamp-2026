# Module 2 — Workflow Orchestration (Kestra)

## How to run
```bash
docker compose -f docker-compose-kestra.yaml up -d
```

Open Kestra UI at http://localhost:8081

# Flow
- taxi_flow.yaml
- Supports taxi type, year, month
- Backfill used to process 2021 data