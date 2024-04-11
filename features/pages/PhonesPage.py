import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class PhonesPage(BasePage):

    def __init__(self, driver, wait=5):
        super().__init__(driver, wait)

    select_item_link_text = "Samsung galaxy s6"

    def select_an_item(self):
        self.click_on_element("select_item_link_text", self.select_item_link_text)
        # time.sleep(3)
