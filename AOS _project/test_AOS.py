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
        headphone_name = self.product.product_name()
        headphone_color = self.product.colors()[-1].get_attribute("title")
        self.product.choose_color(-1)
        for i in range(3):
            self.product.quantity_plus().click()
        headphone_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.speakers().click()
        self.category.click_on_product(1)
        speaker_price = self.product.item_price()
        speaker_name = self.product.product_name()
        speaker_color = self.product.colors()[0].get_attribute("title")
        for i in range(2):
            self.product.quantity_plus().click()
        speaker_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(1)
        laptop_price = self.product.item_price()
        laptop_name = self.product.product_name()
        laptop_color = self.product.colors()[0].get_attribute("title")
        self.product.quantity_plus().click()
        laptop_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()

        self.assertEqual(headphone_name, self.product.text_name_prod_in_cart(-1))
        self.assertIn(speaker_name[:20], self.product.text_name_prod_in_cart(1))
        self.assertIn(laptop_name[:20], self.product.text_name_prod_in_cart(0))
        self.assertEqual(headphone_quantity, self.product.quantity_of_product_in_cart(2))
        self.assertEqual(speaker_quantity, self.product.quantity_of_product_in_cart(1))
        self.assertEqual(laptop_quantity, self.product.quantity_of_product_in_cart(0))
        self.assertEqual(laptop_color, self.product.color_of_product_in_cart(0))
        self.assertEqual(speaker_color, self.product.color_of_product_in_cart(1))
        self.assertEqual(headphone_color, self.product.color_of_product_in_cart(2))
        self.assertEqual(headphone_price * self.product.quantity_of_product_in_cart(2), self.product.total_item_price(2))
        self.assertEqual(speaker_price * self.product.quantity_of_product_in_cart(1), self.product.total_item_price(1))
        self.assertEqual(laptop_price * self.product.quantity_of_product_in_cart(0), self.product.total_item_price(0))
        self.assertEqual(self.product.total_price(), self.product.total_item_price(0) + self.product.total_item_price(1) + self.product.total_item_price(2))

    # add at least 2 products to cart, remove one and check that it's not in cart anymore
    def test3(self):
        self.home_page.headphones().click()
        self.category.click_on_product(-1)
        headphone = self.product.product_name()
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.tablets().click()
        self.category.click_on_product(-1)
        tablet = self.product.product_name()
        self.product.add_to_cart().click()
        # assert happens before add to cart
        self.assertEqual(self.product.text_name_prod_in_cart(1), headphone)
        self.assertEqual(self.product.text_name_prod_in_cart(0), tablet)
        self.assertEqual(len(self.product.x_button_in_cart()), 2)
        self.product.remove_item_from_cart(0)

        self.assertEqual(len(self.product.x_button_in_cart()), 1)
        self.assertNotEqual(self.product.text_name_prod_in_cart(0), tablet)

    # add product to cart and move to shopping-cart page
    def test4(self):
        self.home_page.laptops().click()
        self.category.click_on_product(3)
        self.product.add_to_cart().click()
        self.product.hover_cart().click()

        self.assertEqual(self.shopping_cart.shopping_text(), "SHOPPING CART")

    # add at least 3 products to cart and check if the sum of their prices is equal to total price in shopping cart page
    def test5(self):
        self.home_page.tablets().click()
        self.category.click_on_product(2)
        tablet_price = self.product.item_price()
        tablet_name = self.product.product_name()
        self.product.choose_color(-1)
        for i in range(5):
            self.product.quantity_plus().click()
        tablet_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.mice().click()
        self.category.click_on_product(-3)
        mice_price = self.product.item_price()
        mice_name = self.product.product_name()
        self.product.choose_color(1)
        for i in range(4):
            self.product.quantity_plus().click()
        mice_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.laptops().click()
        self.category.click_on_product(-2)
        laptop_price = self.product.item_price()
        laptop_name = self.product.product_name()
        self.product.quantity_plus().click()
        laptop_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="select  ng-binding"]')))
        total_price = tablet_quantity * tablet_price + mice_price * mice_quantity + laptop_quantity * laptop_price
        print(f"product: {tablet_name}, quantity: {tablet_quantity}, price: {tablet_price}")
        print(f"product: {mice_name}, quantity: {mice_quantity}, price: {mice_price}")
        print(f"product: {laptop_name}, quantity: {laptop_quantity}, price: {laptop_price}")

        self.assertEqual(total_price, self.shopping_cart.total_price())

    # add 2 products, edit their quantities and check if the cart has been updated
    # bug in the site!!!!!!!
    def test6(self):
        self.home_page.tablets().click()
        self.category.click_on_product(1)
        self.product.add_to_cart().click()
        self.home_page.logo().click()
        self.home_page.mice().click()
        self.category.click_on_product(4)
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()
        self.shopping_cart.edit_product(1).click()
        for i in range(2):
            self.product.quantity_plus().click()
        sleep(5)
        mice_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        sleep(2)
        self.shopping_cart.edit_product(1).click()
        for i in range(5):
            self.product.quantity_plus().click()
        tablet_quantity = int(self.product.quantity().get_attribute("value"))
        self.product.add_to_cart().click()
        self.home_page.shopping_cart().click()

        self.assertEqual(self.shopping_cart.product_quantity(0), tablet_quantity)
        self.assertEqual(self.shopping_cart.product_quantity(1), mice_quantity)

    # after choosing a tablet go back to tablets and then go back to home page
    def test7(self):
        self.home_page.tablets().click()
        tablets = self.category.category_name()
        self.category.click_on_product(1)
        self.product.add_to_cart().click()
        self.driver.back()
        self.assertTrue(self.category.category_name() == tablets)
        self.driver.back()

    # need to be fixed
    def test10(self):
        self.home_page.user().click()
        self.account.popUp_username().send_keys("BasaLo")
        username = self.account.popUp_username().get_attribute("value")
        self.account.popUp_password().send_keys("Tester1")
        self.account.signIn_button().click()
        self.assertEqual(self.account.user_menu_options(0), "My account")
        self.wait.until(EC.element_to_be_clickable((By.ID, 'speakersImg')))
        self.home_page.click_sign_out_btn()
        self.wait.until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#menuUserLink>[data-ng-show="userCookie.response"]'), username))
        self.home_page.user().click()
        print(username)
        self.assertNotEqual(username, self.account.popUp_username().get_attribute("value"))
        self.driver.find_element(By.CLASS_NAME, "loginPopUpCloseBtn").click()








