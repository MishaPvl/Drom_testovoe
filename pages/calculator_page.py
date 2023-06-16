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
