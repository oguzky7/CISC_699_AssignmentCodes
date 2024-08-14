import requests
from bs4 import BeautifulSoup

class BrowserInterface:
    """
    Handles interactions between the bot and the browser for scraping web data.
    """

    def __init__(self, url):
        # Store the URL to scrape data from
        self.url = url
        self.page_content = None

    def fetch_page(self):
        # Fetch the content of the webpage
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check for request errors
            self.page_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch the page: {e}")
            self.page_content = None

    def parse_page(self):
        # Parse the webpage content using BeautifulSoup
        if self.page_content:
            soup = BeautifulSoup(self.page_content, 'html.parser')
            return soup
        else:
            print("No content to parse")
            return None
