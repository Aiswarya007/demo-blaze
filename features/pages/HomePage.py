import time

from features.pages.BasePage import BasePage
from features.pages.PhonesPage import PhonesPage


class HomePage(BasePage):

    def __init__(self, driver, wait=5):
        super().__init__(driver, wait)

    phone_category_link_text = "Phones"
    cart_link_text = "Cart"

    def select_phone_category(self):
        self.click_on_element("phone_category_link_text", self.phone_category_link_text)
        # time.sleep(3)

    def navigate_to_cart(self):
        self.click_on_element("cart_link_text", self.cart_link_text)
        # time.sleep(3)