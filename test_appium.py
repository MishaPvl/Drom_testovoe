from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time


def test_start():
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'Google_Pixel_3_XL',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.vbanthia.androidsampleapp',
        'appActivity': 'com.vbanthia.androidsampleapp.MainActivity',
        'noReset': True,
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)

    try:
        digit1_btn = driver.find_element(
            MobileBy.XPATH, '//android.widget.EditText[@content-desc="inputFieldLeft"]')
        digit1_btn.click()
        digit1_btn.send_keys(7)
        digit2_btn = driver.find_element(
            MobileBy.XPATH, '//android.widget.EditText[@content-desc="inputFieldRight"]')
        digit2_btn.click()
        digit2_btn.send_keys(3)
        first = driver.find_element(
            MobileBy.XPATH, '//android.widget.Button[@content-desc="subtractButton"]')
        first.click()
        time.sleep(5)

    finally:
        driver.quit()


if __name__ == '__main__':
    test_start()
# LOCATORS
# left_field = //android.widget.EditText[@content-desc="inputFieldLeft"]
# right_field = //android.widget.EditText[@content-desc="inputFieldRight"]
# plus = //android.widget.Button[@content-desc="additionButton"]
# minus = //android.widget.Button[@content-desc="subtractButton"]
# multipl = //android.widget.Button[@content-desc="multiplicationButton"]
# division = //android.widget.Button[@content-desc="divisionButton"]
# reset = //android.widget.Button[@content-desc="resetButton"]
# result = //android.widget.TextView[@content-desc="resultTextView"]
