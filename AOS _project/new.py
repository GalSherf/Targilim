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

driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
homepage = HomePage(driver)
product = Product(driver)
category = Category(driver)
shopping_cart = ShoppingCart(driver)
order_payment = OrderPayment(driver)
account = Account(driver)

# homepage.laptops().click()
# print(category.category_name())
# category.click_on_product(-2)
# product.add_to_cart().click()
# homepage.shopping_cart().click()
# shopping_cart.checkout_btn().click()
# order_payment.username().send_keys("BasaLo")
# order_payment.password().send_keys("Tester1")
# order_payment.login_btn().click()
# order_payment.next_btn().click()
# order_payment.master_credit_radio().click()
# order_payment.pay_now_btn().click()

# print(shopping_cart.shopping_cart_empty().help())

print(account.signIn_button.__doc__())

sleep(4)
driver.close()
