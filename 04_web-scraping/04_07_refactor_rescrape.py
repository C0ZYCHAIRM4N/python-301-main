# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

def get_filtered_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a', href=True)
    filtered_links = []
    for link in links:
        href = link['href']
        if not href.startswith('#') and 'mw-jump-link' not in link.get('class', []):
            filtered_links.append(href)
    return filtered_links
