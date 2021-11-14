from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_color(self, number):
        colors = self.driver.find_elements(By.ID, 'rabbit')
        colors[number].click()

    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']")

    def type_quantity(self, number):
        self.quantity().send_keys(number)

    def quantity_plus(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.plus')

    def click_plus(self):
        self.quantity_plus().click()

    def add_to_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]')

    def click_add_to_cart(self):
        self.add_to_cart().click()
