from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

#WebCrawling
@app.get("/")
def home():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.txt, "html.parser")
    title = []
    for item in soup.find_all("span",class_="titleline"):
        title.append(item.text)
    return{
        "item":title[:2]
    }

#pagination
@app.get("/pagination")
def pagination(page:int = 1, limit:int = 4):
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.txt, "html.parser")
    title = []
    for item in soup.find_all("span",class_="titleline"):
        title.append(item.text)

    #pagination logic
    start = (page-1)*limit
    end = start+limit
    return{
        "page":page,
        "limit":limit,
        "total":len(title),
        "data":title[start:end]
    }
