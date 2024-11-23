# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.
import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Web_scraping"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

# Find all links
links = soup.find_all('a', href=True)

# Filter out navigation links
filtered_links = []
for link in links:
    href = link['href']
    if not href.startswith('#') and 'mw-jump-link' not in link.get('class', []):
        filtered_links.append(href)

# Print filtered links
for link in filtered_links:
    print(link)

