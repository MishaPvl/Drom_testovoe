from locators.calculator_locators import CalculatorLocators
import pytest

'''
    Файл test_addition.py содержит тесты для операции сложения на калькуляторе.
    Метод test_addition_positive использует параметризацию для выполнения нескольких тестов с различными значениями операндов. Каждый набор операндов представлен в виде кортежа, содержащего левый операнд, правый операнд и ожидаемый результат сложения. Метод выполняет операцию сложения на калькуляторе с каждым набором операндов и проверяет, что результат совпадает с ожидаемым. Затем метод меняет местами операнды и выполняет операцию сложения еще раз, чтобы проверить коммутативность сложения.
    Метод test_addition_with_invalid_input также использует параметризацию для выполнения тестов с некорректными входными значениями операндов.
    Метод выполняет операцию сложения на калькуляторе с каждым набором операндов и проверяет, что отображается сообщение об ошибке "Please, fill the input fields correctly".  
'''

class TestCalculatorAddition():
    @pytest.mark.parametrize("left_operand, right_operand, expected_result", [
        ('2', '5', '7.00'),     # Проверка сложения двух положительных целых чисел
        ('-2', '-5', '-7.00'),  # Проверка сложения двух отрицательных целых чисел
        ('2', '-5', '-3.00'),   # Проверка сложения положительного и отрицательного числа
        ('0', '5', '5.00'),     # Проверка сложения числа с нулём
        ('2', '2', '4.00'),     # Проверка сложения числа с самим собой
        ('9999999999', '9999999999', '19999999998.00'),  # Проверка сложения очень больших чисел
        ('100000000', '1', '100000001.00'), # Проверка суммы с восьмизначным числом
        ('99999999', '1', '100000000.00'),  # Проверка суммы с восьмизначным числом - 1
        ('100000001', '1', '100000002.00'), # Проверка суммы с восьмизначным числом + 1
        ('3.14', '2.86', '6.00'),           # Проверка сложения чисел с десятичной частью
        ('2.14555', '3.26565', '5.41'),  # Проверка сложения чисел с использованием десятичной дроби и большого количества знаков после запятой
        ('-1.5', '-2.7', '-4.20'),     # Проверка сложения чисел с использованием отрицательных десятичных дробей
        ('5', '0', '5.00'),            # Проверка сложения чисел, где одно из них равно нулю
        ('00123', '0.456', '123.46'),  # Проверка сложения чисел, где одно из чисел имеет ведущие нули
        ('2e6', '3e7', '32000000.00'), # Проверка сложения чисел с использованием чисел в экспоненциальной записи
])
    def test_addition_positive(self, calculator_page, left_operand, right_operand, expected_result):
        calculator_page.perform_addition(left_operand, right_operand)
        calculator_page.verify_result(expected_result)

        calculator_page.perform_addition(right_operand, left_operand)
        calculator_page.verify_result(expected_result)

    @pytest.mark.parametrize("left_operand, right_operand", [
        ('2.5', 'abc'),     # Проверка сложения числа и неподходящего значения
        ('2.5', '2.7.8'),   # Проверка сложения чисел с неправильным форматом
        ('1,000', '2.50'),  # Проверка сложения чисел с неправильным разделителем десятичной части
        ('', ''),           # Проверка сложения пустых строк
        ('', '1'),          # Проверка сложения пустой строки и числа
        (' ', ' '),         # Проверка сложения пробелов
        (' ', '1'),         # Проверка сложения пробела и числа
        ('10.50$', '5.25'), # Проверка сложения чисел со специальными символами
    ])
    def test_addition_with_invalid_input(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_addition(left_operand, right_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")

        calculator_page.perform_addition(right_operand, left_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")