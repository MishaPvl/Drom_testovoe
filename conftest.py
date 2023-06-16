import pytest
from appium import webdriver


@pytest.fixture(scope="session")
def driver():
    options = {
        'platformName': 'Android',
        'deviceName': 'Google_Pixel_3_XL',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.vbanthia.androidsampleapp',
        'appActivity': 'com.vbanthia.androidsampleapp.MainActivity',
        'noReset': True,
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def calculator_page(driver):
    from pages.calculator_page import CalculatorPage
    return CalculatorPage(driver)
