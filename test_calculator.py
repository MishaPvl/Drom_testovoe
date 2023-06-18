from locators.calculator_locators import CalculatorLocators
import pytest


# class TestCalculatorPage:
#     '''
#     Проверяем, что все поля отображаются при запуске приложения 
#     '''
#     def test_input_fields_exist(self, calculator_page):
#         assert calculator_page.is_element_displayed(CalculatorLocators.LEFT_INPUT_FIELD), 'Левое поле для ввода не отображается'
#         assert calculator_page.is_element_displayed(CalculatorLocators.RIGHT_INPUT_FIELD), 'Правое поле для ввода не отображается'

#     def test_operation_buttons_exist(self, calculator_page):
#         assert calculator_page.is_element_displayed(CalculatorLocators.ADDITION_BUTTON), 'Кнопка "+" не отображается'
#         assert calculator_page.is_element_displayed(CalculatorLocators.SUBTRACTION_BUTTON), 'Кнопка "-" не отображается'
#         assert calculator_page.is_element_displayed(CalculatorLocators.MULTIPLICATION_BUTTON), 'Кнопка "*" не отображается'
#         assert calculator_page.is_element_displayed(CalculatorLocators.DIVISION_BUTTON), 'Кнопка "/" не отображается'
#         assert calculator_page.is_element_displayed(CalculatorLocators.RESET_BUTTON), 'Кнопка RESET не отображается'
    
#     def test_result_field_exist(self, calculator_page):
#         assert calculator_page.is_element_displayed(CalculatorLocators.RESULT_TEXT), 'Поля для вывода результата не отображается'


# class TestCalculatorInputFields:
#     '''
#     Проверяем как поля для ввода обрабатывают введённые значения
#     '''
#     def test_empty_input_fields_on_startup(self, calculator_page):
#         # Проверяем, что при запуске приложения оба поля пустые.
#         calculator_page.check_initial_input_fields_empty()

#     def test_integer_input_fields(self, calculator_page):
#         # Введите целое число в первое и второе поле для ввода и убедитесь, что они правильно принимает вводимые данные.
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '10')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '10', 'Поле ввода левого операнда содержит неверное значение.'

#         calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '5')
#         result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
#         assert result == '5', 'Поле ввода правого операнда содержит неверное значение.'

#     @pytest.mark.xfail
#     def test_invalid_input(self, calculator_page):
#         # Введите недопустимые символы в оба поля для ввода и убедитесь, что они не приняты.
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, 'abc')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '', 'Поле ввода левого операнда приняло недопустимые символы'

#         calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '@#$')
#         result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
#         assert result == '', 'Поле ввода правого операнда приняло недопустимые символы'

#     def test_very_large_number_input(self, calculator_page):
#         # Введите очень большое число в оба поля и убедитесь, что оно принято и отображается правильно..
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '999999999999999')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '999999999999999', 'Поле ввода левого операнда содержит неверное значение.'

#         calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '999999999999999')
#         result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
#         assert result == '999999999999999', 'Поле ввода правого операнда содержит неверное значение.'

#     def test_decimal_number_input(self, calculator_page):
#         # Введите десятичное число в оба поля ввода и убедитесь, что оно принято и отображается правильно.
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '3.14')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '3.14', 'Поле ввода левого операнда некорректно отображает десятичное число'

#         calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '2.5')
#         result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
#         assert result == '2.5', 'Поле ввода правого операнда некорректно отображает десятичное число'

#     def test_negative_number_input(self, calculator_page):
#         # Проверка ввода отрицательных чисел
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '-7')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '-7', 'Поле ввода левого операнда некорректно отображает отрицательное число'

#         calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '-2')
#         result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
#         assert result == '-2', 'Поле ввода правого операнда некорректно отображает отрицательное число'

#     def test_zero_input(self, calculator_page):
#         # Введите 0 и убедитесь, что число принято и отображается правильно.
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '0')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '0', 'Поле ввода левого операнда содержит неверное значение'

#         calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '0')
#         result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
#         assert result == '0', 'Поле ввода правого операнда содержит неверное значение'
    
#     def test_valid_number_single_field(self, calculator_page):
#         # Убедитесь, что калькулятор не выполняет никаких вычислений, если число есть только в одном поле
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '10')
#         result = calculator_page.get_text(CalculatorLocators.RESULT_TEXT)
#         assert result == '', 'Калькулятор выполняет вычисление при наличии числа только в одном поле'
    
#     @pytest.mark.xfail
#     # Проверка ввода числа с ведущими нулями
#     def test_leading_zeros_input(self, calculator_page):
#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '00123')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '123', 'Поле ввода левого операнда содержит неверное значение'

#         calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '00256')
#         result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
#         assert result == '256', 'Поле ввода правого операнда содержит неверное значение'


# class TestCalculatorAddition():
#     @pytest.mark.parametrize("left_operand, right_operand, expected_result", [
#         ('2', '5', '7.00'),     # Проверка сложения двух положительных целых чисел
#         ('-2', '-5', '-7.00'),  # Проверка сложения двух отрицательных целых чисел
#         ('2', '-5', '-3.00'),   # Проверка сложения положительного и отрицательного числа
#         ('0', '5', '5.00'),     # Проверка сложения числа с нулём
#         ('2', '2', '4.00'),     # Проверка сложения числа с самим собой
#         ('9999999999', '9999999999', '19999999998.00'),  # Проверка сложения очень больших чисел
#         ('2147483647', '1', '2147483648.00'),  # Проверка сложения чисел с использованием границы целочисленного типа - 1
#         ('2147483648', '1', '2147483649.00'),  # Проверка сложения чисел с использованием границы целочисленного типа
#         ('2147483649', '1', '2147483650.00'),  # Проверка сложения чисел с использованием границы целочисленного типа
#         ('100000000', '1', '100000001.00'), # Проверка суммы с восьмизначным числом
#         ('99999999', '1', '100000000.00'),  # Проверка суммы с восьмизначным числом - 1
#         ('100000001', '1', '100000002.00'), # Проверка суммы с восьмизначным числом + 1
#         ('3.14', '2.86', '6.00'),           # Проверка сложения чисел с десятичной частью
#         ('2.14555', '3.26565', '5.42'),  # Проверка сложения чисел с использованием десятичной дроби и большого количества знаков после запятой
#         ('-1.5', '-2.7', '-4.20'),     # Проверка сложения чисел с использованием отрицательных десятичных дробей
#         ('5', '0', '5.00'),            # Проверка сложения чисел, где одно из них равно нулю
#         ('00123', '0.456', '123.46'),  # Проверка сложения чисел, где одно из чисел имеет ведущие нули
#         ('2e6', '3e7', '32000000.00'), # Проверка сложения чисел с использованием чисел, представленных в научной нотации
# ])
#     def test_addition_with_positive_numbers(self, calculator_page, left_operand, right_operand, expected_result):
#         calculator_page.perform_addition(left_operand, right_operand)
#         calculator_page.verify_result(expected_result)

#         calculator_page.perform_addition(right_operand, left_operand)
#         calculator_page.verify_result(expected_result)

    # @pytest.mark.parametrize("left_operand, right_operand", [
    #     ('2.5', 'abc'),     # Проверка сложения числа и неподходящего значения
    #     ('2.5', '2.7.8'),   # Проверка сложения чисел с неправильным форматом
    #     ('1,000', '2.50'),  # Проверка сложения чисел с неправильным разделителем десятичной части
    #     ('', ''),           # Проверка сложения пустых строк
    #     (' ', ' '),         # Проверка сложения пробелов
    #     ('10.50$', '5.25'), # Проверка сложения чисел со специальными символами
    # ])
    # def test_addition_with_invalid_input(self, calculator_page, left_operand, right_operand):
    #     calculator_page.perform_addition(left_operand, right_operand)
    #     calculator_page.verify_error_message("Please, fill the input fields correctly")

    #     calculator_page.perform_addition(right_operand, left_operand)
    #     calculator_page.verify_error_message("Please, fill the input fields correctly")


class TestCalculatorSubtraction():
    @pytest.mark.parametrize("left_operand, right_operand, expected_result", [
        ('5', '2', '3.00'),     # Проверка вычитания положительных целых чисел
        ('-5', '-2', '-3.00'),  # Проверка вычитания отрицательных целых чисел
        ('2', '-5', '7.00'),    # Проверка вычитания положительного числа из отрицательного числа
        ('0', '5', '-5.00'),    # Проверка вычитания числа из нуля
        ('5', '5', '0.00'),     # Проверка вычитания числа из самого себя
        ('9999999999', '9999999999', '0.00'),  # Проверка вычитания очень больших чисел
        ('2147483648', '1', '2147483647.00'),  # Проверка вычитания чисел с использованием границы целочисленного типа
        ('100000000', '1', '99999999.00'),     # Проверка разности с восьмизначным числом
        ('100000001', '1', '100000000.00'),    # Проверка разности с восьмизначным числом + 1
        ('3.14', '2.86', '0.28'),              # Проверка вычитания чисел с десятичной частью
        ('5.42', '3.26565', '2.15'),  # Проверка вычитания чисел с использованием десятичной дроби и большого количества знаков после запятой
        ('-1.5', '-2.7', '1.20'),     # Проверка вычитания чисел с использованием отрицательных десятичных дробей
        ('5', '0', '5.00'),           # Проверка вычитания чисел, где одно из них равно нулю
        ('123.46', '0.456', '123.00'),  # Проверка вычитания чисел, где одно из чисел имеет ведущие нули
        ('3e7', '2e6', '28000000.00'),  # Проверка вычитания чисел с использованием чисел, представленных в научной нотации
    ])
    def test_subtraction_with_positive_numbers(self, calculator_page, left_operand, right_operand, expected_result):
        calculator_page.perform_subtraction(left_operand, right_operand)
        calculator_page.verify_result(expected_result)

    @pytest.mark.parametrize("left_operand, right_operand", [
        ('2.5', 'abc'),     # Проверка вычитания числа и неподходящего значения
        ('2.5', '2.7.8'),   # Проверка вычитания чисел с неправильным форматом
        ('1,000', '2.50'),  # Проверка вычитания чисел с неправильным разделителем десятичной части
        ('', ''),           # Проверка вычитания пустых строк
        (' ', ' '),         # Проверка вычитания пробелов
        ('10.50$', '5.25'), # Проверка вычитания чисел со специальными символами
    ])
    def test_subtraction_with_invalid_input(self, calculator_page, left_operand, right_operand):
        calculator_page.perform_subtraction(left_operand, right_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")

        calculator_page.perform_subtraction(right_operand, left_operand)
        calculator_page.verify_error_message("Please, fill the input fields correctly")








#     @pytest.mark.parametrize("field, input_value, expected_result", [
#     (CalculatorLocators.LEFT_INPUT_FIELD, '10', '10'),  # Проверка ввода целого числа в первое поле ввода
#     (CalculatorLocators.RIGHT_INPUT_FIELD, '5', '5'),  # Проверка ввода целого числа во второе поле ввода
#     (CalculatorLocators.LEFT_INPUT_FIELD, 'abc', ''),  # Проверка недопустимого ввода
#     (CalculatorLocators.RIGHT_INPUT_FIELD, '@#$', ''),  # Проверка недопустимого ввода
#     (CalculatorLocators.LEFT_INPUT_FIELD, '999999999999999', '999999999999999'),  # Проверка очень большого числа
#     (CalculatorLocators.RIGHT_INPUT_FIELD, '999999999999999', '999999999999999'),  # Проверка очень большого числа
#     (CalculatorLocators.LEFT_INPUT_FIELD, '3.14', '3.14'),  # Проверка ввода десятичного числа
#     (CalculatorLocators.RIGHT_INPUT_FIELD, '2.5', '2.5'),  # Проверка ввода десятичного числа
#     (CalculatorLocators.LEFT_INPUT_FIELD, '-7', '-7'),  # Проверка ввода отрицательного числа
#     (CalculatorLocators.RIGHT_INPUT_FIELD, '-2', '-2'),  # Проверка ввода отрицательного числа
#     (CalculatorLocators.LEFT_INPUT_FIELD, '0', '0'),  # Проверка ввода числа 0
#     (CalculatorLocators.RIGHT_INPUT_FIELD, '0', '0'),  # Проверка ввода числа 0
#     (CalculatorLocators.LEFT_INPUT_FIELD, '10', ''),  # Проверка ввода числа только в одном поле
#     (CalculatorLocators.LEFT_INPUT_FIELD, '00123', '123'),  # Проверка ввода числа с ведущими нулями
#     (CalculatorLocators.LEFT_INPUT_FIELD, '00256', '256'),  # Проверка ввода числа с ведущими нулями
# ])
#     def test_input_fields(self, calculator_page, field, input_value, expected_result):
#         calculator_page.enter_number(field, input_value)
#         result = calculator_page.get_text(field)
#         assert result == expected_result