from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPayment:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def pay_now_btn(self):
        return self.driver.find_element(By.ID, "pay_now_btn_MasterCredit")
        # return self.driver.find_element(By.CSS_SELECTOR, '[name="pay_now_btn_MasterCredit"]')

    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="usernameInOrderPayment"]')

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="passwordInOrderPayment"]')

    def login_btn(self):
        return self.driver.find_element(By.ID, "login_btnundefined")

    def next_btn(self):
        return self.driver.find_element(By.ID, "next_btn")

    def master_credit_radio(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[ng-checked="checkedRadio == 2"]')


