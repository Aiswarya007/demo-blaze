import time

from features.pages.BasePage import BasePage


class ItemPage(BasePage):

    def __init__(self, driver, wait=5):
        super().__init__(driver, wait)

    add_to_cart_link_text = "Add to cart"


    def add_to_cart(self):
        self.click_on_element("add_to_cart_link_text", self.add_to_cart_link_text)
        # time.sleep(3)

    def accept_alert(self):
        self.click_on_alert_ok()
        # time.sleep(3)



