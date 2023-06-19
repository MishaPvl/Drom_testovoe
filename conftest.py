import pytest
from appium import webdriver

''' 
    Файл conftest.py содержит фикстуры, используемые для настройки и предоставления ресурсов для тестов.
    Фикстура driver предоставляет экземпляр драйвера для взаимодействия с приложением.
    Она создается один раз для всей сессии тестирования и уничтожается после окончания сессии.
    Фикстура calculator_page предоставляет экземпляр страницы калькулятора для выполнения операций и проверок.
    Она создается один раз для каждого класса тестов и уничтожается после завершения класса. 
'''
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
