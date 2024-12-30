# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup

# Mocked version of the script
def mock_script():
    URL = "https://en.wikipedia.org/wiki/Web_scraping"
    r = MagicMock()
    r.text = '<html><body><a href="link1">Link1</a><a href="#internal">Internal</a><a href="/wiki/Something" class="mw-jump-link">Jump</a><a href="/wiki/Else">Else</a></body></html>'
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Find all links
    links = soup.find_all('a', href=True)

    # Filter out navigation links
    filtered_links = []
    for link in links:
        href = link['href']
        if not href.startswith('#') and 'mw-jump-link' not in link.get('class', []):
            filtered_links.append(href)
    
    return filtered_links

class TestWebScraping(unittest.TestCase):

    @patch('requests.get')
    def test_filtered_links(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.text = '<html><body><a href="link1">Link1</a><a href="#internal">Internal</a><a href="/wiki/Something" class="mw-jump-link">Jump</a><a href="/wiki/Else">Else</a></body></html>'
        mock_get.return_value = mock_response
        
        # Run the script through our mocked version
        result = mock_script()
        
        # Assertions
        self.assertIn('/wiki/Else', result)  # Should be included
        self.assertNotIn('#internal', result)  # Should be filtered out
        self.assertNotIn('/wiki/Something', result)  # Should be filtered out because of class
        self.assertEqual(len(result), 2)  # Only two links should remain
    
    @patch('requests.get')
    def test_no_links(self, mock_get):
        mock_get.return_value.text = '<html><body><p>No links here</p></body></html>'
        result = mock_script()
        self.assertEqual(result, [])  # Should return an empty list

    @patch('requests.get')
    def test_all_filtered_out(self, mock_get):
        mock_get.return_value.text = '<html><body><a href="#internal">Internal</a><a href="/wiki/Something" class="mw-jump-link">Jump</a></body></html>'
        result = mock_script()
        self.assertEqual(result, [])  # All links should be filtered out

if __name__ == '__main__':
    unittest.main()