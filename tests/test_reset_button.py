from locators.calculator_locators import CalculatorLocators
import pytest

'''
    Тесты проверяют, что кнопка RESET стирает значения в полях для ввода и поле для вывода результата после выполнения различных операций (сложение, вычитание, умножение, деление).
    Тесты в данном классе помечены декоратором @pytest.mark.parametrize, который позволяет задать набор параметров для выполнения тестов с различными значениями операндов.
'''
@pytest.mark.parametrize("left_operand, right_operand", [
    ('4', '2'),             # Проверка с двумя положительными числами
    ('10.05', '5.54'),      # Проверка с двумя десятичными числами
    ('-8.00', '4.00'),      # Проверка с отрицательными числами
    ('10.50$', '5.25')      # Проверка, что RESET сотрёт некорректный ввод и сообщение об ошибке
])
class TestResetButton():
    def test_reset_button_resets_input_fields(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения, которые были введены в поля
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, left_operand)
        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_input_fields_empty()

    def test_reset_button_resets_input_fields_after_addition(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в полях для ввода после операции сложения
        calculator_page.perform_addition(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_input_fields_empty()

    def test_reset_button_resets_input_fields_after_subtraction(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в полях для ввода после операции вычитания
        calculator_page.perform_subtraction(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_input_fields_empty()

    def test_reset_button_resets_input_fields_after_multiplication(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в полях для ввода после операции умножения
        calculator_page.perform_multiplication(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_input_fields_empty()

    def test_reset_button_resets_input_fields_after_division(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в полях для ввода после операции деления
        calculator_page.perform_division(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_input_fields_empty()

    def test_reset_button_resets_result_field_after_addition(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в поле для вывода результата после операции сложения
        calculator_page.perform_addition(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_result_field_empty()

    def test_reset_button_resets_result_field_after_subtraction(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в поле для вывода результата вычитания
        calculator_page.perform_subtraction(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_result_field_empty()

    def test_reset_button_resets_result_field_after_multiplication(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в поле для вывода результата операции умножения
        calculator_page.perform_multiplication(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_result_field_empty()

    def test_reset_button_resets_result_field_after_division(self, calculator_page, left_operand, right_operand):
        # Проверяем, что кнопка RESET стирает значения в поле для вывода результата операции деления
        calculator_page.perform_division(left_operand, right_operand)
        calculator_page.click_reset_button()
        calculator_page.check_result_field_empty()