from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Product:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def colors(self):
        rabbit = self.driver.find_elements(By.ID, 'rabbit')
        bunny = self.driver.find_elements(By.ID, 'bunny')
        if len(bunny) == 0:
            return rabbit
        else:
            return bunny

    def choose_color(self, num):
        self.colors()[num].click()

    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']")

    def quantity_plus(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.plus')

    def add_to_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]')

    def hover_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span>label")

    def hover_cart_items_num_text(self):
        return self.hover_cart().get_attribute("innerHTML")

    def item_num_in_cart(self):
        return self.hover_cart_items_num_text()[1]

    def name_product_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "td>a>h3")

    def text_name_prod_in_cart(self, num):
        return self.name_product_in_cart()[num].get_attribute("innerHTML")

    def product_quantity_in_cart(self):
        quantity_list = self.driver.find_elements(By.CSS_SELECTOR, "a>label")
        colors = []
        print(len(quantity_list))
        color = quantity_list.pop(-1)
        colors.append(color)
        print(len(quantity_list))
