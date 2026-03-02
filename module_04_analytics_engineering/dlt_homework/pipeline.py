import dlt
import requests

BASE_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"

def fetch_pages():
    page = 1
    while True:
        params = {"page": page, "page_size": 1000}
        r = requests.get(BASE_URL, params=params, timeout=60)
        r.raise_for_status()
        rows = r.json() 

        print(f"page={page} rows={len(rows)}")

        if not rows:
            break

        yield rows
        page += 1

@dlt.resource(name="trips", write_disposition="replace")
def trips():
    yield from fetch_pages()

def main():
    pipeline = dlt.pipeline(
        pipeline_name="dlt_hw",
        destination="duckdb",
        dataset_name="dlt_hw_ds",
    )
    load_info = pipeline.run(trips())
    print(load_info)

if __name__ == "__main__":
    main()