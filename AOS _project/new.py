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
from ShoppingCart import *

service1 = Service(r"C:\selenium\chromedriver.exe")

driver = webdriver.Chrome(service=service1)

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
homepage = HomePage(driver)
product = Product(driver)
category = Category(driver)
shopping_cart = ShoppingCart(driver)
#
# homepage.headphones().click()
# category.click_on_product(2)
# product.add_to_cart().click()
# homepage.logo().click()

homepage.laptops().click()
print(category.category_name())
category.click_on_product(-2)
product.add_to_cart().click()
# homepage.logo().click()
# homepage.laptops().click()
# category.click_on_product(-1)
# product.add_to_cart().click()
# homepage.logo().click()
# homepage.headphones().click()
# category.click_on_product(2)
# product.add_to_cart().click()
# homepage.shopping_cart().click()
# shopping_cart.edit_product(0).click()



sleep(4)
driver.close()
