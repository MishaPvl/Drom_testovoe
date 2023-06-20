from .base_page import BasePage
from locators.calculator_locators import CalculatorLocators


class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_addition_button(self):
        # Нажимает на кнопку сложения
        self.click_button(CalculatorLocators.ADDITION_BUTTON)

    def click_subtraction_button(self):
        # Нажимает на кнопку вычитания
        self.click_button(CalculatorLocators.SUBTRACTION_BUTTON)

    def click_multiplication_button(self):
        # Нажимает на кнопку умножения
        self.click_button(CalculatorLocators.MULTIPLICATION_BUTTON)

    def click_division_button(self):
        # Нажимает на кнопку деления
        self.click_button(CalculatorLocators.DIVISION_BUTTON)

    def click_reset_button(self):
        # Нажимает на кнопку сброса
        self.click_button(CalculatorLocators.RESET_BUTTON)

    def check_input_fields_empty(self):
        # Проверяет, что поля ввода пустые
        first_value = self.find_element(CalculatorLocators.LEFT_INPUT_FIELD).text
        assert first_value == '', 'Левое поле не пустое'

        second_value = self.find_element(CalculatorLocators.RIGHT_INPUT_FIELD).text
        assert second_value == '', 'Правое поле не пустое'
    
    def check_result_field_empty(self):
        # Проверяет, что поле результата пустое
        result_field = self.find_element(CalculatorLocators.RESULT_TEXT).text
        assert result_field == '', 'Поле результата не пустое'

    def perform_addition(self, left_operand, right_operand):
        # Выполняет операцию сложения на калькуляторе
        self.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, left_operand)
        self.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, right_operand)
        self.click_addition_button()

    def perform_subtraction(self, left_operand, right_operand):
        # Выполняет операцию вычитания на калькуляторе
        self.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, left_operand)
        self.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, right_operand)
        self.click_subtraction_button()

    def perform_multiplication(self, left_operand, right_operand):
        # Выполняет операцию умножения на калькуляторе
        self.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, left_operand)
        self.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, right_operand)
        self.click_multiplication_button()

    def perform_division(self, left_operand, right_operand):
        # Выполняет операцию деления на калькуляторе
        self.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, left_operand)
        self.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, right_operand)
        self.click_division_button()

    def verify_result(self, expected_result):
        # Проверяет, что ответ совпадает с ожидаемым (число после знака =)
        result_value = self.get_result_after_equal_sign()
        result = self.format_decimal_value(result_value)
        assert result == expected_result, f'Ожидаемый результат {expected_result} отличается от фактического {result}'

    def verify_result_field(self, expected_result):
        # Проверяет полный текст в поле вывода
        result_value = self.get_text(CalculatorLocators.RESULT_TEXT)
        result = self.format_decimal_value(result_value)
        assert result == expected_result, f'Ожидаемый результат {expected_result} отличается от фактического {result}'

    def verify_error_message(self, expected_error_message):
        # Проверяет, что сообщение об ошибке успешно отображается
        error_message = self.get_text(CalculatorLocators.RESULT_TEXT)
        assert error_message == expected_error_message, f'Ожидаемое сообщение об ошибке {expected_error_message} не соответсвует фактическому {error_message}'

    def get_result_after_equal_sign(self):
        # Функция для того, чтобы получить число после знака =
        result = self.get_text(CalculatorLocators.RESULT_TEXT)
        equal_sign_index = result.find('=')
        if equal_sign_index != -1:
            number_after_equal_sign = result[equal_sign_index + 1:].strip()
            return number_after_equal_sign
        else:
            return None
        
    def format_decimal_value(self, value):
    # Замените запятую на точку в числе, если она присутствует
    # Без этой функции часть тестов может не проходить на телефонах из-за разницы в отображении формата чисел
    # Например я прогонял все тесты на телефоне с английской локализацией и все тесты проходили, 
    # на телефоне с русской локализацией все эти тесты упали.
        if ',' in value:
            value = value.replace(',', '.')

        return value