from features.pages.BasePage import BasePage


class PlaceOrderPage(BasePage):

    def __init__(self, driver, wait=5):
        super().__init__(driver, wait)

    name_id = "name"
    country_id = "country"
    city_id = "city"
    credit_card_id = "card"
    month_id = "month"
    year_id = "year"
    purchase_xpath = "//div[@id='orderModal']/div[@role='document']//div[@class='modal-footer']/button[2]"
    pop_up_xpath = "//div[@class='sa-confirm-button-container']/button[@class='confirm btn btn-lg btn-primary']"

    def enter_name(self, name_text):
        self.enter_details("name_id", self.name_id, name_text)

    def enter_country(self, country_text):
        self.enter_details("country_id", self.country_id, country_text)

    def enter_city(self, city_text):
        self.enter_details("city_id", self.city_id, city_text)

    def enter_credit_card(self, credit_card_text):
        self.enter_details("credit_card_id", self.credit_card_id, credit_card_text)

    def enter_month(self, month_text):
        self.enter_details("month_id", self.month_id, month_text)

    def enter_year(self, year_text):
        self.enter_details("year_id", self.year_id, year_text)

    def click_on_purchase(self):
        self.click_on_element("purchase_xpath", self.purchase_xpath)

    def accept_pop_up(self):
        self.click_on_element("purchase_xpath", self.purchase_xpath)
