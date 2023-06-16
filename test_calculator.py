import unittest
from appium import webdriver
from pages.calculator_page import CalculatorPage
from locators.calculator_locators import CalculatorLocators


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        capabilities = {
            'platformName': 'Android',
            'deviceName': 'Google_Pixel_3_XL',
            'automationName': 'UiAutomator2',
            'appPackage': 'com.vbanthia.androidsampleapp',
            'appActivity': 'com.vbanthia.androidsampleapp.MainActivity',
            'noReset': True,
        }
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', capabilities)
        self.page = CalculatorPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_addition(self):
        self.page.check_initial_input_fields_empty()
        self.page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '2')
        self.page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '5')
        self.page.click_addition_button()
        result = self.page.get_text(CalculatorLocators.RESULT_TEXT)
        assert result == '2.00 + 5.00 = 7.00'


if __name__ == '__main__':
    unittest.main()
