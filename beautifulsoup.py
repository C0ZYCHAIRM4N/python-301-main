import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.co/"
page = requests.get(URL)
