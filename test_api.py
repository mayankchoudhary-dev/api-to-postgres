
import json
from pathlib import Path

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = Path("data/raw/posts.json")


def extract_api_data():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    posts = response.json()

    if not isinstance(posts, list):
        raise ValueError("Expected the API to return a list")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(posts, file, indent=2, ensure_ascii=False)

    print("Status code:", response.status_code)
    print("Records extracted:", len(posts))
    print("Saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    extract_api_data()


import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Send an HTTP GET request
response = requests.get(url, timeout=30)

# Check the HTTP status
print("Status code:", response.status_code)

# Raise an error if the request failed
response.raise_for_status()

# Convert JSON into Python objects
posts = response.json()

# Inspect the extracted data
print("Total records:", len(posts))
print("First record:", posts[0])

# Inspect the available fields
print("Fields:", list(posts[0].keys()))

