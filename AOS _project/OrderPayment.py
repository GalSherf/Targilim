from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPayment:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def pay_now_btn(self):
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")
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

    def edit_btn(self):
        return self.driver.find_element(By.CLASS_NAME, "edit")

    def card_number(self):
        return self.driver.find_element(By.ID, "creditCard")

    def cvv_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="cvv_number"]')

    def card_holder(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="cardholder_name"]')

    def expiration_month(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="mmListbox"]')

    def expiration_year(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="yyyyListbox"]')

    def thanks_for_buying(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[translate="Thank_you_for_buying_with_Advantage"]')

    def number_above_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#shoppingCartLink>span')

    def order_number(self):
        return self.driver.find_element(By.ID, 'orderNumberLabel')

    def order_number_text(self):
        return self.driver.find_element(By.ID, 'orderNumberLabel').text

    def wait_order_number(self):
        self.wait.until(EC.visibility_of(self.order_number()))



