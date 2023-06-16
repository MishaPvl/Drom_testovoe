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
        time.sleep(10)

    finally:
        driver.quit()


if __name__ == '__main__':
    test_start()
