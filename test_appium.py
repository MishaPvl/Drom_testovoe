# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
# import time
# from locators.calculator_locators import CalculatorLocators


# def test_start():
# capabilities = {
#     'platformName': 'Android',
#     'deviceName': 'Google_Pixel_3_XL',
#     'automationName': 'UiAutomator2',
#     'appPackage': 'com.vbanthia.androidsampleapp',
#     'appActivity': 'com.vbanthia.androidsampleapp.MainActivity',
#     'noReset': True,
# }
#     url = 'http://localhost:4723/wd/hub'
#     driver = webdriver.Remote(url, capabilities)

#     try:
#         digit1_btn = driver.find_element(*CalculatorLocators.LEFT_INPUT_FIELD)
#         digit1_btn.click()
#         digit1_btn.send_keys(7)
#         digit2_btn = driver.find_element(*CalculatorLocators.RIGHT_INPUT_FIELD)
#         digit2_btn.click()
#         digit2_btn.send_keys(3)
#         first = driver.find_element(*CalculatorLocators.DIVISION_BUTTON)
#         first.click()
#         time.sleep(5)

#     finally:
#         driver.quit()


# if __name__ == '__main__':
#     test_start()
# LOCATORS
# left_field = //android.widget.EditText[@content-desc="inputFieldLeft"]
# right_field = //android.widget.EditText[@content-desc="inputFieldRight"]
# plus = //android.widget.Button[@content-desc="additionButton"]
# minus = //android.widget.Button[@content-desc="subtractButton"]
# multipl = //android.widget.Button[@content-desc="multiplicationButton"]
# division = //android.widget.Button[@content-desc="divisionButton"]
# reset = //android.widget.Button[@content-desc="resetButton"]
# result = //android.widget.TextView[@content-desc="resultTextView"]
# В данном случае, функции perform_addition и verify_error_message являются специфичными для тестового класса TestCalculatorAddition и не обязательно должны быть вынесены в base_page или calculator_page.
# Однако, если вы заметите, что эти функции или их части повторяются в других тестовых классах, то может быть полезно вынести их в base_page или calculator_page для повторного использования.
# В общем случае, base_page должен содержать общие функции, которые могут быть использованы в различных тестовых классах (например, функции для ввода текста в поле ввода, клика по кнопке и т.д.). calculator_page должен содержать функции, специфичные для страницы калькулятора (например, функции для ввода чисел в поля ввода калькулятора, клика по кнопкам калькулятора и т.д.).
# Ваш подход к организации кода должен зависеть от конкретных требований и структуры вашего проекта. Главное - следовать принципам чистого кода и обеспечивать читаемость и поддерживаемость кода.


class TestCalculatorAddition():
    @pytest.mark.parametrize("left_operand, right_operand", [
        ('2.5', 'text'),  # Проверка сложения числа и неподходящего значения
        ('abc', '5'),  # Проверка сложения неподходящего значения и числа
        ('2.5', '2.7.8'),  # Проверка сложения чисел с неправильным форматом
        ('1,000', '2.50'),  # Проверка сложения чисел с неправильным разделителем десятичной части
        ('10.50$', '5.25'),  # Проверка сложения чисел со специальными символами
    ])
    def test_addition_negative(self, calculator_page, left_operand, right_operand):
        self.perform_addition(calculator_page, left_operand, right_operand)
        self.verify_error_message(calculator_page, "Please, fill the input fields correctly")

    def perform_addition(self, calculator_page, left_operand, right_operand):
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, str(left_operand))
        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, str(right_operand))
        calculator_page.click_addition_button()

    def verify_error_message(self, calculator_page, expected_error_message):
        error_message = calculator_page.get_text(CalculatorLocators.RESULT_TEXT)
        assert error_message == expected_error_message, f'Expected error message "{expected_error_message}", but got "{error_message}"'


class TestCalculatorAddition():
    @pytest.mark.parametrize("left_operand, right_operand, expected_result", [
        ('2', '5', '2.00 + 5.00 = 7.00'),
        ('-2', '-5', '-2.00 + -5.00 = -7.00'),
        ('2', '-5', '2.00 + -5.00 = -3.00'),
        ('0', '5', '0.00 + 5.00 = 5.00'),
        ('2', '2', '2.00 + 2.00 = 4.00'),
        ('9999999999', '9999999999', '9999999999.00 + 9999999999.00 = 19999999998.00'),
        ('2147483647', '1', '2147483647.00 + 1.00 = 2147483648.00'),
        ('3.14', '2.86', '3.14 + 2.86 = 6.00'),
        ('2.1', '3.2', '2.10 + 3.20 = 5.30'),
        ('-1.5', '-2.7', '-1.50 + -2.70 = -4.20'),
        ('5', '0', '5.00 + 0.00 = 5.00'),
        ('00123', '0.456', '123.00 + 0.46 = 123.46'),
        ('2e6', '3e7', '2000000.00 + 30000000.00 = 32000000.00'),
    ])
    def test_addition_positive(self, calculator_page, left_operand, right_operand, expected_result):
        self.perform_addition(calculator_page, left_operand, right_operand, expected_result)

    def perform_addition(self, calculator_page, left_operand, right_operand, expected_result):
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, str(left_operand))
        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, str(right_operand))
        calculator_page.click_addition_button()
        self.verify_result(calculator_page, expected_result)

    def verify_result(self, calculator_page, expected_result):
        result = calculator_page.get_text(CalculatorLocators.RESULT_TEXT)
        assert result == expected_result, f'Expected {expected_result}, but got {result}'
