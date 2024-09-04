import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

print(fetch_url("https://github.com/topics/babel"))