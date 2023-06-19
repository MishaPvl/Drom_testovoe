from locators.calculator_locators import CalculatorLocators
import pytest

'''
    Файл test_multiplication.py содержит тесты для операции сложения на калькуляторе. 
'''
class TestCalculatorMultiplication:
    @pytest.mark.parametrize("left_operand, right_operand, expected_result", [
        ('2', '5', '10.00'),     # Проверка умножения двух положительных целых чисел
        ('-2', '-5', '10.00'),   # Проверка умножения двух отрицательных целых чисел
        ('2', '-5', '-10.00'),   # Проверка умножения положительного и отрицательного числа
        ('0', '5', '0.00'),      # Проверка умножения числа на нуль
        ('2', '0', '0.00'),      # Проверка умножения нуля на число
        ('2', '2', '4.00'),      # Проверка умножения числа на само себя
        ('214647', '214647', '46073334609.00'),  # Проверка умножения больших чисел
        ('99999999', '2', '199999998.00'),  # Проверка произведения с восьмизначным числом - 1
        ('100000000', '2', '200000000.00'),    # Проверка произведения с восьмизначным числом
        ('100000001', '2', '200000002.00'),    # Проверка произведения с восьмизначным числом + 1
        ('3.14', '2.5', '7.85'),                # Проверка умножения чисел с десятичной частью
        ('2.14555', '3.26565', '7.01'),      # Проверка умножения чисел с использованием десятичной дроби и большого количества знаков после запятой
        ('-1.5', '-2.7', '4.05'),               # Проверка умножения чисел с использованием отрицательных десятичных дробей
        ('00123', '0.456', '56.09'),            # Проверка умножения чисел, где одно из чисел имеет ведущие нули
        ('2e6', '3e7', '60000000000000.00'),   # Проверка умножения чисел в экспоненциальной записи
    ])
    def test_multiplication_positive(self, calculator_page, left_operand, right_operand, expected_result):
        calculator_page.perform_multiplication(left_operand, right_operand)
        calculator_page.verify_result(expected_result)

        calculator_page.perform_multiplication(right_operand, left_operand)
        calculator_page.verify_result(expected_result)

    @pytest.mark.parametrize("left_operand, right_operand", [
        ('2.5', 'abc'),     # Проверка умножения числа на неподходящее значение
        ('2.5', '2.7.8'),   # Проверка умножения чисел с неправильным форматом
        ('1,000', '2.50'),  # Проверка умножения чисел с неправильным разделителем десятичной части
        ('', ''),           # Проверка умножения пустых строк
        ('', '1'),          # Проверка умножения пустой строки и числа
        (' ', ' '),         # Проверка умножения пробелов
        (' ', '1'),         # Проверка умножения пробела и числа
        ('10.50$', '5.25'), # Проверка умножения чисел со специальными символами
    ])
    def test_multiplication_with_invalid_input(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_multiplication(left_operand, right_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")

        calculator_page.perform_multiplication(right_operand, left_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")