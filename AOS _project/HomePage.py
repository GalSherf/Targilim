from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import random
service1 = Service(r"C:\selenium\chromedriver.exe")

driver = webdriver.Chrome(service=service1)


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 10)

    def speakers(self):
        return self.driver.find_element(By.ID, 'speakersImg')

    def click_headphones(self):
        self.headphones().click()

    def tablets(self):
        return self.driver.find_element(By.ID, 'tabletsImg')

    def laptops(self):
        return self.driver.find_element(By.ID, 'laptopsImg')

    def mice(self):
        return self.driver.find_element(By.ID, 'miceImg')

    def headphones(self):
        return self.driver.find_element(By.ID, 'headphonesImg')

    def logo(self):
        return self.driver.find_element(By.CLASS_NAME, 'logo')

    def click_logo(self):
        self.logo().click()

    def user(self):
        return self.driver.find_element(By.ID, 'menuUserLink')

    def click_user(self):
        self.user().click()

    def create_user(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="create-new-account ng-scope"]')

    def click_create_user(self):
        self.create_user().click()

    def shopping_cart(self):
        return self.driver.find_element(By.ID, 'shoppingCartLink')

    def my_account_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="option ng-scope"][translate="My_account"]')

    def click_my_account_btn(self):
        self.click_user()
        self.my_account_btn().click()

    def my_orders_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.mobileTitle>div>[class="option ng-scope"][translate="My_Orders"]')

    def click_my_order_btn(self):
        self.click_user()
        self.my_orders_btn().click()

    def sign_out_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="option ng-scope"][translate="Sign_out"]')

    def click_sign_out_btn(self):
        self.click_user()
        self.sign_out_btn().click()