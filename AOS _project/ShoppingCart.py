from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class ShoppingCart:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def shopping_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="select  ng-binding"]').get_attribute("innerHTML")[1:]
