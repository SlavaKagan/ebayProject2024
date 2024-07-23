import pytest
import sys
import os

from utils.webDriver import get_webdriver
from pages.homepage import HomePage
from pages.resultsPage import SearchResultsPage
import utils.const as const

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# This test file contains the Test Cases


@pytest.fixture(scope="module")
def driver():
    driver = get_webdriver()
    assert driver is not None, "Failed WebDriver"
    yield driver
    driver.quit()


# Verify that the eBay homepage loads correctly


def test_ebay_homepage_loads(driver):
    home_page = HomePage(driver)
    home_page.load(const.EBAY_URL)
    expected_title = "Electronics, Cars, Fashion, Collectibles, Coupons and More | eBay"
    actual_title = driver.title

    assert expected_title in actual_title, f"Expected title: {expected_title}, but got: {actual_title}"


def test_search_functionality(driver):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)

    home_page.load(const.EBAY_URL)
    home_page.search_for_item(const.TERM)

    # Searching for a specific item ("laptop") and verifying that the search results page is displayed

    expected = const.TERM
    actual = driver.current_url
    assert expected in actual, f"Expected title: {expected}, but got: {actual}"

    # Verifying that the search results contain the search term and find at least 10 results.
    assert search_results_page.verify_results_count(10), "Fewer than 10 search results found"
    assert search_results_page.is_search_term_in_results(const.TERM), "Search term 'laptop' not found in results"
