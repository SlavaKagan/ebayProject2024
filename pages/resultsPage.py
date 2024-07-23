from selenium.webdriver.common.by import By
from pages.basePage import BasePage

# Represents the search results page on eBay


class SearchResultsPage(BasePage):
    RESULTS = (By.CSS_SELECTOR, '.s-item')
    SEARCH_TERM_IN_RESULTS = (By.XPATH, '//span[contains(text(), "{}")]')

    def get_results(self):
        return self.driver.find_elements(*self.RESULTS)

    def is_search_term_in_results(self, search_term):
        results = self.get_results()
        for result in results:
            if search_term.lower() in result.text.lower():
                return True
        return False

    def verify_results_count(self, min_count):
        results = self.get_results()
        return len(results) >= min_count
