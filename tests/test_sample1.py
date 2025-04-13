import pytest
from src.sample1 import scraper, MyConnectionError


def test_scraper_ok():
    url = 'https://quotes.toscrape.com/'
    quotes = scraper(url)
    assert len(quotes) > 0
    for quote in quotes:
        print(quote.text)


def test_scraper_wring_url_error():
    with pytest.raises(MyConnectionError) as e:
        url = 'https://quotes.toscrape.co/'
        scraper(url)
    assert "Failed to resolve URL" in str(e.value)
