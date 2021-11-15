from unittest import TestCase
from Category import *
from HomePage import *
from Account import *
from Product import *
from ShoppingCart import *
from time import sleep
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
        self.shopping_cart = ShoppingCart(self.driver)

    def tearDown(self):
        print("tearDown")
        sleep(2)
        self.home_page.logo().click()
        self.driver.close()

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

        self.assertEqual(self.product.item_num_in_cart(), 6)

    # add 3 products to cart and check if their details appear in the shopping-cart popUp
    def test2(self):
        self.home_page.headphones().click()
        self.category.click_on_product(2)
        headphone_price = self.product.item_price()
        self.product.choose_color(-1)
        for i in range(3):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.speakers().click()
        self.category.click_on_product(1)
        speaker_price = self.product.item_price()
        for i in range(2):
            self.product.quantity_plus().click()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(-2)
        laptop_price = self.product.item_price()
        self.product.quantity_plus().click()
        self.product.add_to_cart().click()

        self.assertEqual("HP H2310 IN-EAR HEADSET", self.product.text_name_prod_in_cart(-1))
        self.assertIn("BOSE SOUNDLINK WIRELESS", self.product.text_name_prod_in_cart(1))
        self.assertEqual("HP STREAM - 11-D020NR LAPTOP", self.product.text_name_prod_in_cart(0))
        self.assertEqual(4, self.product.quantity_of_product_in_cart(0))
        self.assertEqual(3, self.product.quantity_of_product_in_cart(1))
        self.assertEqual(2, self.product.quantity_of_product_in_cart(2))
        self.assertEqual("YELLOW", self.product.color_of_product_in_cart(0))
        self.assertEqual("TURQUOISE", self.product.color_of_product_in_cart(1))
        self.assertEqual("PURPLE", self.product.color_of_product_in_cart(2))
        self.assertEqual(self.product.total_price(), self.product.total_item_price(0) + self.product.total_item_price(1) + self.product.total_item_price(2))
        self.assertEqual(headphone_price * self.product.quantity_of_product_in_cart(0), self.product.total_item_price(0))
        self.assertEqual(speaker_price * self.product.quantity_of_product_in_cart(1), self.product.total_item_price(1))
        self.assertEqual(laptop_price * self.product.quantity_of_product_in_cart(2), self.product.total_item_price(2))
        print(self.product.items_in_cart()[0].get_attribute("value"))
        print(self.product.items_in_cart()[1].get_attribute("value"))
        print(self.product.items_in_cart()[2].get_attribute("value"))

    # add at least 2 products to cart, remove one and check that it's not in cart anymore
    def test3(self):
        self.home_page.headphones().click()
        self.category.click_on_product(-1)
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.tablets().click()
        self.category.click_on_product(-1)
        self.product.add_to_cart().click()
        self.assertEqual(self.product.text_name_prod_in_cart(1), "LOGITECH USB HEADSET H390")
        self.assertEqual(len(self.product.x_button_in_cart()), 2)
        self.product.remove_item_from_cart(1)

        self.assertEqual(len(self.product.x_button_in_cart()), 1)
        self.assertEqual(self.product.text_name_prod_in_cart(0), "HP PRO TABLET 608 G1")

    # add product to cart and move to shopping-cart page
    def test4(self):
        self.home_page.laptops().click()
        self.category.click_on_product(3)
        self.product.add_to_cart().click()
        self.product.hover_cart().click()

        self.assertEqual(self.shopping_cart.shopping_text(), "SHOPPING CART")

    def test5(self):
        self.home_page.laptops().click()
        self.category.click_on_product(3)
        self.product.add_to_cart().click()
        self.product.hover_cart().click()

