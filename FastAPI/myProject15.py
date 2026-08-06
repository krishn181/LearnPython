from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import time

app = FastAPI()

cache_data = []
last_fetch = 0


@app.get("/")
def home():
    global cache_data, last_fetch

    start_time = time.time()

    if not cache_data or time.time() - last_fetch > 60:
        print(f"Fetching fresh data {start_time}")

        url = "https://news.ycombinator.com/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        cache_data = [
            item.text
            for item in soup.find_all("span", class_="titleline")
        ]

        last_fetch = time.time()

    else:
        print("Using cached data")

    end_time = time.time()

    return {
        "time_taken": round(end_time - start_time, 4),
        "data": cache_data[:5]
    }