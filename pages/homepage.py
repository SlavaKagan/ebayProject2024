from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.basePage import BasePage

# Represents the homepage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")

    def search_for_item(self, item):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(item)
        search_box.send_keys(Keys.RETURN)

    def is_search_button_present(self):
        return self.driver.find_element(*self.SEARCH_BUTTON).is_displayed()
