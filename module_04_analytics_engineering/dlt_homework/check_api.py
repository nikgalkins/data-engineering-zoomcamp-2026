import requests

url = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"
r = requests.get(url, params={"page": 2, "page_size": 1000}, timeout=60)

print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))

data = r.json()
print("type:", type(data))

if isinstance(data, list):
    print("rows:", len(data))
else:
    print("keys:", list(data.keys())[:20])
    for k in ["data", "results", "items"]:
        if k in data and isinstance(data[k], list):
            print(f"{k} rows:", len(data[k]))