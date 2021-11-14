from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Account:
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver, 10)

    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[name="usernameRegisterPage"]')

    def type_username(self, text):
        self.username().send_keys(text)

    def email(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="emailRegisterPage"]')

    def type_email(self, text):
        self.email().send_keys(text)

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="passwordRegisterPage"]')

    def type_password(self, text):
        self.password().send_keys(text)

    def confirm_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="confirm_passwordRegisterPage"]')

    def type_confirm_password(self, text):
        self.confirm_password().send_keys(text)

    def first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="first_nameRegisterPage"]')

    def type_first_name(self, text):
        self.first_name().send_keys(text)

    def last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="last_nameRegisterPage"]')

    def type_last_name(self, text):
        self.last_name().send_keys(text)

    def phone_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="phone_numberRegisterPage"]')

    def type_phone_number(self, text):
        self.phone_number().send_keys(text)

    def country(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="countryListboxRegisterPage"]')

    def select_country(self, country):
        select_country = Select(self.country())
        select_country.select_by_visible_text(country)

    def city(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="cityRegisterPage"]')

    def type_city(self, text):
        self.city().send_keys(text)

    def address(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="addressRegisterPage"]')

    def type_address(self, text):
        self.address().send_keys(text)

    def state(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="state_/_province_/_regionRegisterPage"]')

    def type_state(self, text):
        self.state().send_keys(text)

    def postal_code(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="postal_codeRegisterPage"]')

    def type_postal_code(self, text):
        self.postal_code().send_keys(text)

    def agree_conditions(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="i_agree"]')

    def check_conditions(self):
        self.agree_conditions().click()

    def register_btn(self):
        return self.driver.find_element(By.ID, 'register_btnundefined')

    def click_register(self):
        self.register_btn().click()

    def edit_account_details(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[href="#/accountDetails"]')

    def click_edit_account_details(self):
        self.edit_account_details().click()

    def edit_payment(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[href="#/accountPaymentEdit"]')

    def click_edit_payment(self):
        self.edit_payment().click()