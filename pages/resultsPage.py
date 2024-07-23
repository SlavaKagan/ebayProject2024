from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class SearchResultsPage(BasePage):
    RESULT_TITLES = (By.CSS_SELECTOR, ".s-item__title")

    def get_result_titles(self):
        return self.driver.find_elements(*self.RESULT_TITLES)

    def verify_results_contain_term(self, term):
        titles = self.get_result_titles()
        assert len(titles) >= 10, "Less than 10 results found."

        for title in titles:
            assert term.lower() in title.text.lower(), f"Search term '{term}' not found in result: {title.text}"
