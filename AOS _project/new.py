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
from HomePage import HomePage
from Product import *
from Category import *

service1 = Service(r"C:\selenium\chromedriver.exe")

driver = webdriver.Chrome(service=service1)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
homepage = HomePage(driver)
product = Product(driver)
category = Category(driver)

homepage.headphones().click()
category.click_on_product(2)
product.add_to_cart().click()
homepage.logo().click()

homepage.laptops().click()
category.click_on_product(-2)
product.quantity_plus().click()
product.quantity_plus().click()
product.add_to_cart().click()

product.product_quantity_in_cart()







# username = driver.find_element(By.CSS_SELECTOR,'[name="usernameRegisterPage"]').send_keys("Shalomlo")
#
# email = driver.find_element(By.CSS_SELECTOR, '[name="emailRegisterPage"]')
# email.send_keys("g@g.com")
# password = driver.find_element(By.CSS_SELECTOR, '[name="passwordRegisterPage"]')
# password.send_keys("Kukiku1")
# conf_pass = driver.find_element(By.CSS_SELECTOR, '[name="confirm_passwordRegisterPage"]')
# conf_pass.send_keys("Kukiku1")
#
# phone = driver.find_element(By.CSS_SELECTOR, '[name="phone_numberRegisterPage"]').send_keys("0542")
#
# country = driver.find_element(By.CSS_SELECTOR, '[name="countryListboxRegisterPage"]')
# select_contry = Select(country)
# select_contry.select_by_visible_text("Israel")
#
# agree = driver.find_element(By.CSS_SELECTOR, '[name="i_agree"]')
# agree.click()
# # wait.until(EC.element_to_be_clickable((By.ID,"register_btnundefined")))
#
#
# regi = driver.find_element(By.ID, 'register_btnundefined')
# regi.click()



sleep(5)
driver.close()


"create-new-account ng-scope"