import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.webDriver import get_webdriver
from pages.homepage import HomePage
from pages.resultsPage import SearchResultsPage


@pytest.fixture(scope="module")
def driver():
    driver = get_webdriver()
    yield driver
    driver.quit()


def test_ebay_homepage_loads(driver):
    home_page = HomePage(driver)
    home_page.go_to("https://www.ebay.com/")
    assert "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay" in driver.title


def test_search_functionality(driver):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)

    home_page.go_to("https://www.ebay.com/")
    home_page.search_for_item("laptop")

    assert "laptop" in driver.title
    search_results_page.verify_results_contain_term("laptop")
