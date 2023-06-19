from locators.calculator_locators import CalculatorLocators
import pytest

'''
    Проверяем, что корректно отображаются все поля и кнопки
'''

class TestCalculatorPage:

    def test_input_fields_exist(self, calculator_page):
        assert calculator_page.is_element_displayed(CalculatorLocators.LEFT_INPUT_FIELD), 'Левое поле для ввода не отображается'
        assert calculator_page.is_element_displayed(CalculatorLocators.RIGHT_INPUT_FIELD), 'Правое поле для ввода не отображается'

    def test_operation_buttons_exist(self, calculator_page):
        assert calculator_page.is_element_displayed(CalculatorLocators.ADDITION_BUTTON), 'Кнопка "+" не отображается'
        assert calculator_page.is_element_displayed(CalculatorLocators.SUBTRACTION_BUTTON), 'Кнопка "-" не отображается'
        assert calculator_page.is_element_displayed(CalculatorLocators.MULTIPLICATION_BUTTON), 'Кнопка "*" не отображается'
        assert calculator_page.is_element_displayed(CalculatorLocators.DIVISION_BUTTON), 'Кнопка "/" не отображается'
        assert calculator_page.is_element_displayed(CalculatorLocators.RESET_BUTTON), 'Кнопка RESET не отображается'
    
    def test_result_field_exist(self, calculator_page):
        assert calculator_page.is_element_displayed(CalculatorLocators.RESULT_TEXT), 'Поля для вывода результата не отображается'