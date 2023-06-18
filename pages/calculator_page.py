from .base_page import BasePage
from locators.calculator_locators import CalculatorLocators


class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_addition_button(self):
        self.click_button(CalculatorLocators.ADDITION_BUTTON)

    def click_subtraction_button(self):
        self.click_button(CalculatorLocators.SUBTRACTION_BUTTON)

    def click_multiplication_button(self):
        self.click_button(CalculatorLocators.MULTIPLICATION_BUTTON)

    def click_division_button(self):
        self.click_button(CalculatorLocators.DIVISION_BUTTON)

    def click_reset_button(self):
        self.click_button(CalculatorLocators.RESET_BUTTON)

    def check_initial_input_fields_empty(self):
        first_value = self.find_element(CalculatorLocators.LEFT_INPUT_FIELD).text
        assert first_value == '', 'Левое поле не пустое'

        second_value = self.find_element(CalculatorLocators.RIGHT_INPUT_FIELD).text
        assert second_value == '', 'Правое поле не пустое'

    def perform_addition(self, left_operand, right_operand):
        self.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, left_operand)
        self.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, right_operand)
        self.click_addition_button()

    def verify_result(self, expected_result):
        result = self.get_result_after_equal_sign()
        assert result == expected_result, f'Ожидаемый результат {expected_result} отличается от фактического {result}'

    def verify_error_message(self, expected_error_message):
        error_message = self.get_text(CalculatorLocators.RESULT_TEXT)
        assert error_message == expected_error_message, f'Ожидаемое сообщение об ошибке {expected_error_message} не соответсвует фактическому {error_message}'

    def get_result_after_equal_sign(self):
        result = self.get_text(CalculatorLocators.RESULT_TEXT)
        equal_sign_index = result.find('=')
        if equal_sign_index != -1:
            number_after_equal_sign = result[equal_sign_index + 1:].strip()
            return number_after_equal_sign
        else:
            return None