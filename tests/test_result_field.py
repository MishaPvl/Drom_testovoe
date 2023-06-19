from locators.calculator_locators import CalculatorLocators
import pytest

'''
Файл test_result_field.py содержит тесты для проверки поля вывода результата калькулятора.
В нём используется параметризация с различными значениями операндов для проверки различных сценариев.
Из-за того, что поле для вывода содержит строку, которая состоит из двух операндов, действия над ними и результат
мне пришлось использовать следующую конструкцию:
calculator_page.verify_result_field(f'{float(left_operand):.2f} + {float(right_operand):.2f} = {result:.2f}')
Выглядит не лучшим образом, но позволяет подавать на вход и обрабатывать любые значения
'''

# Позитивные тесты для проверки правильного вывода результата
@pytest.mark.parametrize("left_operand, right_operand", [
    ('4', '2'),             # Проверка с двумя положительными числами
    ('10.05', '5.54'),      # Проверка с двумя десятичными числами
    ('-8.00', '4.00'),      # Проверка с отрицательными числами
    ('0', '4.24'),          # Проверка с нулём
    ('99999999', '99'),   # Проверка с большим числом
    ('3.14159', '1.41421'), # Проверка округления
])
class TestResultFieldPositive:
    def test_addition_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_addition(left_operand, right_operand)
        result = float(left_operand) + float(right_operand)
        calculator_page.verify_result_field(f'{float(left_operand):.2f} + {float(right_operand):.2f} = {result:.2f}')

    def test_subtraction_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_subtraction(left_operand, right_operand)
        result = float(left_operand) - float(right_operand)
        calculator_page.verify_result_field(f'{float(left_operand):.2f} - {float(right_operand):.2f} = {result:.2f}')
    
    def test_multiplication_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_multiplication(left_operand, right_operand)
        result = float(left_operand) * float(right_operand)
        calculator_page.verify_result_field(f'{float(left_operand):.2f} * {float(right_operand):.2f} = {result:.2f}')

    def test_division_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_division(left_operand, right_operand)
        result = float(left_operand) / float(right_operand)
        calculator_page.verify_result_field(f'{float(left_operand):.2f} / {float(right_operand):.2f} = {result:.2f}')


# Негативные тесты для проверки обработки некорректных значений
@pytest.mark.parametrize("left_operand, right_operand", [
    ('2.5', 'abc'),     # Проверка числа на неподходящее значение
    ('2.5', '2.7.8'),   # Проверка чисел с неправильным форматом
    ('1,000', '2.50'),  # Проверка чисел с неправильным разделителем десятичной части
    ('', ''),           # Проверка пустых строк
    ('', '1'),          # Проверка пустой строки и числа
    (' ', ' '),         # Проверка пробелов
    (' ', '1'),         # Проверка пробела и числа
    ('10.50$', '5.25'), # Проверка чисел со специальными символами
])
class TestResultFieldNegative:
    # Выполнение операции с некорректными данными и проверка, что выводится сообщение об ошибке
    def test_addition_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_addition(left_operand, right_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")

    def test_subtraction_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_subtraction(left_operand, right_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")
    
    def test_multiplication_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_multiplication(left_operand, right_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")

    def test_division_in_result_field(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_division(left_operand, right_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")