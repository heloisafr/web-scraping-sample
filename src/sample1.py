import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

class MyConnectionError(Exception):
    pass

def scraper(url):
    """
    Simple web scraping
    """
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('span', class_='text')

        return quotes

    except ConnectionError as e:
        raise MyConnectionError(f"Failed to resolve URL '{url}'") from e



if __name__ == '__main__':
    url = 'https://quotes.toscrape.com/'
    scraper(url)