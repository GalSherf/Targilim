from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # return the speakers category element after it presented
    def speakers(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'speakersImg')))
        return self.driver.find_element(By.ID, 'speakersImg')

    # return the tablets category element after it presented
    def tablets(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'tabletsImg')))
        return self.driver.find_element(By.ID, 'tabletsImg')

    # return the laptops category element after it presented
    def laptops(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'laptopsImg')))
        return self.driver.find_element(By.ID, 'laptopsImg')

    # return the mice category element after it presented
    def mice(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'miceImg')))
        return self.driver.find_element(By.ID, 'miceImg')

    # return the headphones category element after it presented
    def headphones(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'headphonesImg')))
        return self.driver.find_element(By.ID, 'headphonesImg')

    # return the site logo element after it presented
    def logo(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'logo')))
        return self.driver.find_element(By.CLASS_NAME, 'logo')

    # return the user icon element after it presented
    def user(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUserLink')))
        return self.driver.find_element(By.ID, 'menuUserLink')

    # return the user icon element after it presented
    def create_user(self):
        self.wait.until(EC.text_to_be_present_in_element((By.LINK_TEXT, "CREATE NEW ACCOUNT"), "CREATE NEW ACCOUNT"))
        return self.driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT")

    def shopping_cart(self):
        return self.driver.find_element(By.ID, 'shoppingCartLink')

    def my_account_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#loginMiniTitle>[translate="My_account"]')

    def click_my_account_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUserLink')))
        self.user().click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginMiniTitle>[translate="My_account"]')))
        self.my_account_btn().click()

    def my_orders_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#menuUserLink>div>[translate="My_Orders"]')

    def click_my_order_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUserLink')))
        self.user().click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#menuUserLink>div>[translate="My_Orders"]')))
        self.my_orders_btn().click()

    def sign_out_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][class='option roboto-medium ng-scope']")

    def click_sign_out_btn(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'menuUserLink')))
        self.user().click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[translate='Sign_out'][class='option roboto-medium ng-scope']")))
        self.sign_out_btn().click()

