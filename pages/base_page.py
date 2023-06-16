from appium.webdriver.common.mobileby import MobileBy


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def enter_number(self, locator, number):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(number)

    def click_button(self, locator):
        button = self.find_element(locator)
        button.click()

    def get_text(self, locator):
        result = self.find_element(locator).text
        return result

    def element_is_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed()
