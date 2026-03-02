# dlt Homework (DE Zoomcamp 2026)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install dlt duckdb requests pandas
```

## Run pipeline (load data to DuckDB)
```bash
python pipeline.py
```

This will create dlt_hw.duckdb in this directory and load table "dlt_hw_ds"."trips".

## Compute homework answers
```bash
python answers.py
```

## Quick API check (optional)
```bash
python check_api.py
```