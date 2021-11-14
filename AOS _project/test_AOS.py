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
        sleep(10)

    def test1(self):
        self.home_page.click_headphones()


    def tearDown(self):
        sleep(3)
        print("tearDown")
        self.driver.close()