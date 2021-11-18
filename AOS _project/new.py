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
from OrderPayment import *
from Account import *

service1 = Service(r"C:\selenium\chromedriver.exe")

driver = webdriver.Chrome(service=service1)

driver.get("https://www.advantageonlineshopping.com/#/product/10")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
homepage = HomePage(driver)
product = Product(driver)
category = Category(driver)
shopping_cart = ShoppingCart(driver)
order_payment = OrderPayment(driver)
account = Account(driver)

sleep(2)
for i in range(7):
    product.quantity_plus().click()
product.add_to_cart().click()
sleep(2)
print(product.total_item_price(0))

homepage.logo().click()
homepage.laptops().click()
category.click_on_product(-2)
for i in range(7):
    product.quantity_plus().click()
product.add_to_cart().click()
sleep(2)
print(product.total_item_price(0))

print(product.total_price())
homepage.shopping_cart().click()
print(shopping_cart.total_price())
if shopping_cart.total_price() == product.total_price():
    print("All Good")
sleep(3)

sleep(4)
driver.close()
