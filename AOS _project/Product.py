from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Product:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_color(self, color):
        color = self.driver.find_elements(By.ID, 'rabbit')
        color[-1].click()

    def choose_quantity(self, quantity):
        product_quantity = self.driver.find_element(By.CSS_SELECTOR, "input[name='quantity']")
        product_quantity.click()
        product_quantity.clear()
        product_quantity.send_keys(quantity)
