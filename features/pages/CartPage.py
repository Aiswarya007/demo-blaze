import time

from features.pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self, driver, wait=5):
        super().__init__(driver, wait)

    product_xpath = "//table[@class='table table-bordered table-hover table-striped']//tr/td[2]"
    place_order_xpath ="//div[@id='page-wrapper']//button[@type='button']"

    def item_availability(self):
        assert self.product_displayed("product_xpath", self.product_xpath) == "Samsung galaxy s6"

    def select_place_order(self):
        self.click_on_element("place_order_xpath", self.place_order_xpath)
