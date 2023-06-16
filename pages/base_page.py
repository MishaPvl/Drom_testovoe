from appium.webdriver.common.mobileby import MobileBy


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def enter_number(self, number):
        pass
