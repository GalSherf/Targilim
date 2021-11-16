from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class ShoppingCart:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def shopping_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="select  ng-binding"]').get_attribute("innerHTML")[1:]

    def product_quantity(self):
        quantity_list = self.driver.find_elements(By.CSS_SELECTOR, 'class="ng-binding"')
        for i in quantity_list:
            if i.get_attribute("title"):
                quantity_list.remove(i)
        print(len(quantity_list))

    def product_color(self, number):
        colors = self.driver.find_elements(By.CLASS_NAME, "productColor")
        return colors[number].get_attribute("title")

    def total_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR, '#shoppingCart>table>tfoot>tr>td>span[class="roboto-medium ng-binding"]').text
        if len(price) < 8:
            return float(price[1:])
        elif len(price) == 9:
            return float(price[1] + price[3:])
        else:
           return float(price[1:2] + price[4:])
