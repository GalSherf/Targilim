from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Category:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_into_product(self, num):
        list_product = self.driver.find_elements(By.CSS_SELECTOR, "[class ='cell categoryRight'] > ul > li")
        list_product[num].click()