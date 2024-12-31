import sys
sys.path.append('/home/kyle/python-301-main/06_testing/06_05_recipe-scraper')

import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import re

from rescrape import get_page_content, get_html_content, make_soup, get_recipe_links, get_author, get_recipe

def test_get_page_content(monkeypatch):
    mock_response = MagicMock(text="Mocked HTML content")
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: mock_response)
    result = get_page_content("some_url")
    assert result.text == "Mocked HTML content"

def test_get_html_content(monkeypatch):
    mock_response = MagicMock()
    mock_response.text = "HTML content"
    monkeypatch.setattr("your_script.get_page_content", lambda *args, **kwargs: mock_response)
    result = get_html_content("some_url")
    assert result == "HTML content"

def test_make_soup():
    html = "<html><body><p>Test</p></body></html>"
    soup = make_soup(html)
    assert isinstance(soup, BeautifulSoup)

def test_get_recipe_links():
    html = '<html><body><a href="link1">Link1</a><a href="link2">Link2</a></body></html>'
    soup = BeautifulSoup(html, "html.parser")
    links = get_recipe_links(soup)
    assert links == ["link1", "link2"]

def test_get_author():
    html = '<html><body><p class="author">by John Doe</p></body></html>'
    soup = BeautifulSoup(html, "html.parser")
    author = get_author(soup)
    assert author == "John Doe"

def test_get_recipe():
    html = '<html><body><div class="md">Recipe content here</div></body></html>'
    soup = BeautifulSoup(html, "html.parser")
    recipe = get_recipe(soup)
    assert recipe == "Recipe content here"

@pytest.mark.parametrize("html, expected_output", [
    ('<html><body><a href="recipe1.html">Recipe1</a></body></html>', '<html><body><a href="recipe1.html">Recipe1</a></body></html>'),
    ('<html><body></body></html>', '<html><body></body></html>'),
])
def test_main_loop(monkeypatch, capsys, html, expected_output):
    # Mocking the HTML content for the index page
    monkeypatch.setattr("your_script.get_html_content", lambda *args, **kwargs: html)
    
    def mock_soup(html):
        soup = BeautifulSoup(html, "html.parser")
        return soup
    
    monkeypatch.setattr("your_script.make_soup", mock_soup)

    # Mocking HTML for the recipe page
    recipe_html = '<html><body><p class="author">by Author Name</p><div class="md">Recipe Text</div></body></html>'
    monkeypatch.setattr("your_script.get_html_content", lambda *args, **kwargs: recipe_html if '/recipe1.html' in args[0] else html)

    # Run the main block
    if __name__ == "test_main":
        index_html = get_html_content("BASE_URL")
        index_soup = make_soup(index_html)
        recipe_links = get_recipe_links(index_soup)

        for r_link in recipe_links:
            URL = f"BASE_URL/{r_link}"
            soup = make_soup(get_html_content(URL))
            author = get_author(soup)
            recipe = get_recipe(soup) 
            print(f"({author})\t[{recipe}]\n\n\n")

    # Capture stdout
    captured = capsys.readouterr()
    assert re.search(r"\(Author Name\)\t\[Recipe Text\]", captured.out)