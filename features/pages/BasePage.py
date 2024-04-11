from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver, wait: 5):
        self.driver = driver
        self.my_wait = WebDriverWait(driver, wait)

    def click_on_element(self, locator_type, locator_value):
        self.get_element(locator_type, locator_value).click()

    def enter_details(self, locator_type, locator_value, actual_value):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(actual_value)

    def click_on_alert_ok(self):
        self.driver.switch_to.alert.accept()

    def product_displayed(self, locator_type, locator_value):
        return self.get_element(locator_type, locator_value).text

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            # element = self.driver.find_element(By.ID, locator_value)
            element = self.my_wait.until(EC.element_to_be_clickable((By.ID, locator_value)))
        elif locator_type.endswith("_name"):
            # element = self.driver.find_element(By.NAME, locator_value)
            element = self.my_wait.until(EC.presence_of_element_located((By.NAME, locator_value)))
        elif locator_type.endswith("_class_name"):
            # element = self.driver.find_element(By.CLASS_NAME, locator_value)
            element = self.my_wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_type.endswith("_link_text"):
            # element = self.driver.find_element(By.LINK_TEXT, locator_value)
            element = self.my_wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator_value)))
        elif locator_type.endswith("_xpath"):
            # element = self.driver.find_element(By.XPATH, locator_value)
            element = self.my_wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
        elif locator_type.endswith("_css"):
            # element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
            element = self.my_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
        return element
