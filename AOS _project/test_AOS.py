from unittest import TestCase
from Category import *
from HomePage import *
from Account import *
from Product import *
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


class TestAccount(TestCase):
    def setUp(self):
        print("setUp")
        service = Service(r"C:\selenium\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.home_page = HomePage(self.driver)
        self.account = Account(self.driver)
        self.category = Category(self.driver)
        self.product = Product(self.driver)

    # add 2 products in different quantities that bigger then 1, and check the total number of items in cart
    def test1(self):
        self.home_page.mice().click()
        self.category.click_on_product(1)
        self.product.choose_color(1)
        for i in range(3):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(-2)
        self.product.quantity_plus().click()
        self.product.add_to_cart().click()

        self.assertEqual(self.product.item_num_in_cart(), "6")

    # add 3 products to cart and check if their details appear in the shopping-cart popUp
    def test2(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'speakersImg')))
        self.home_page.headphones().click()
        self.category.click_on_product(2)
        self.product.choose_color(-1)
        for i in range(3):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.speakers().click()
        self.category.click_on_product(1)
        for i in range(2):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(-2)
        self.product.quantity_plus().click()
        self.product.add_to_cart().click()

        self.assertEqual(self.product.text_name_prod_in_cart(-1), "HP H2310 IN-EAR HEADSET")
        self.assertIn("BOSE SOUNDLINK WIRELESS", self.product.text_name_prod_in_cart(1))
        self.assertEqual("HP STREAM - 11-D020NR LAPTOP", self.product.text_name_prod_in_cart(0))

    def tearDown(self):
        sleep(2)
        print("tearDown")
        self.driver.close()

