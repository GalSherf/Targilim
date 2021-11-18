from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Account:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # return username input element
    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[name="usernameRegisterPage"]')

    # return email input element
    def email(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="emailRegisterPage"]')

    # return password input element
    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="passwordRegisterPage"]')

    # return confirm_password input element
    def confirm_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="confirm_passwordRegisterPage"]')

    # return first_name input element
    def first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="first_nameRegisterPage"]')

    # return last_name input element
    def last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="last_nameRegisterPage"]')

    # return phone_number input element
    def phone_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="phone_numberRegisterPage"]')

    # return country element
    def country(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="countryListboxRegisterPage"]')

    # get a country and select it from country select field
    def select_country(self, country):
        select_country = Select(self.country())
        select_country.select_by_visible_text(country)

    # return city input element
    def city(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="cityRegisterPage"]')

    # return address input element
    def address(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="addressRegisterPage"]')

    # return state input element
    def state(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="state_/_province_/_regionRegisterPage"]')

    # return state input element
    def postal_code(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="postal_codeRegisterPage"]')

    # return agree_conditions check-box element
    def agree_conditions(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="i_agree"]')

    # return country element
    def register_btn(self):
        return self.driver.find_element(By.ID, 'register_btnundefined')

    def edit_account_details(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[href="#/accountDetails"]')

    def edit_payment(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[href="#/accountPaymentEdit"]')

    def popUp_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="username"]')

    def popUp_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="password"]')

    def signIn_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[type="button"]')

    def click_sign_in(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="button"]')))
        self.signIn_button().click()

    def x_button_pop_up(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "loginPopUpCloseBtn")))
        return self.driver.find_element(By.CLASS_NAME, "loginPopUpCloseBtn")

    def loggedIn_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#menuUserLink>span")

    # wait until the username text to be presented in element
    def wait_username_text(self):
        self.wait.until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#menuUserLink>[data-ng-show="userCookie.response"]'),self.loggedIn_username().text))

    def user_menu(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#menuUserLink>div>label")

    def user_menu_options(self, number):
        return self.user_menu()[number].get_attribute("innerHTML")

    def delete_account(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="deleteMainBtnContainer a-button ng-scope"]')

    def confirm_delete(self):
        self.delete_account().click()
        return self.driver.find_element(By.CSS_SELECTOR, 'div[class="deletePopupBtn deleteRed"]')
