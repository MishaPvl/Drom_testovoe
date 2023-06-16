from locators.calculator_locators import CalculatorLocators
import pytest


class TestCalculatorInputFields:
    def test_empty_input_fields_on_startup(self, calculator_page):
        # Проверяем, что при запуске приложения оба поля пустые.
        calculator_page.check_initial_input_fields_empty()

    def test_integer_input_first_field(self, calculator_page):
        # Введите целое число в первое поле ввода и убедитесь, что оно правильно принимает вводимые данные.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '10')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '10'

    def test_integer_input_second_field(self, calculator_page):
        # Введите целое число во второе поле ввода и убедитесь, что оно правильно принимает вводимые данные.
        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '5')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '5'

    @pytest.mark.xfail
    def test_invalid_input(self, calculator_page):
        # Введите недопустимые символы в любое из полей ввода и убедитесь, что они не приняты.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, 'abc')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == ''

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '@#$')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == ''

    def test_very_large_number_input(self, calculator_page):
        # Введите очень большое число в оба поля и убедитесь, что оно принято и отображается правильно..
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '999999999999999')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '999999999999999'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '999999999999999')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '999999999999999'

    def test_decimal_number_input(self, calculator_page):
        # Введите десятичное число в оба поля ввода и убедитесь, что оно принято и отображается правильно.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '3.14')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '3.14'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '2.5')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '2.5'

    def test_negative_number_input(self, calculator_page):
        # Проверка ввода отрицательных чисел
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '-7')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '-7'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '-2')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '-2'

    def test_zero_input(self, calculator_page):
        # Введите 0 и убедитесь, что число принято и отображается правильно.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '0')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '0'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '0')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '0'
    
    def test_valid_number_single_field(self, calculator_page):
        # Убедитесь, что калькулятор не выполняет никаких вычислений, если число есть только в одном поле
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '10')
        result = calculator_page.get_text(CalculatorLocators.RESULT_TEXT)
        assert result == ''
    
    @pytest.mark.xfail
    # Проверка ввода числа с ведущими нулями
    def test_leading_zeros_input(self, calculator_page):
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '00123')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '123'

        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '00256')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '256'

class TestCalculatorAddition():
    @pytest.mark.parametrize("left_operand, right_operand, expected_result", [
        ('2', '5', '2.00 + 5.00 = 7.00'),  # Проверка сложения двух положительных целых чисел
        ('-2', '-5', '-2.00 + -5.00 = -7.00'),  # Проверка сложения двух отрицательных целых чисел
        ('2', '-5', '2.00 + -5.00 = -3.00'),  # Проверка сложения положительного и отрицательного числа
        ('0', '5', '0.00 + 5.00 = 5.00'),  # Проверка сложения числа с нулём
        ('2', '2', '2.00 + 2.00 = 4.00'),  # Проверка сложения числа с самим собой
        ('9999999999', '9999999999', '9999999999.00 + 9999999999.00 = 19999999998.00'),  # Проверка сложения очень больших чисел
        ('2147483647', '1', '2147483647.00 + 1.00 = 2147483648.00'),  # Проверка сложения чисел с использованием границ целочисленного типа
        ('3.14', '2.86', '3.14 + 2.86 = 6.00'),  # Проверка сложения чисел с десятичной частью
        ('2.1', '3.2', '2.10 + 3.20 = 5.30'),  # Проверка сложения чисел с использованием десятичной дроби и большого количества знаков после запятой
        ('-1.5', '-2.7', '-1.50 + -2.70 = -4.20'),  # Проверка сложения чисел с использованием отрицательных десятичных дробей
        ('5', '0', '5.00 + 0.00 = 5.00'),  # Проверка сложения чисел, где одно из них равно нулю
        ('00123', '0.456', '123.00 + 0.46 = 123.46'),  # Проверка сложения чисел, где одно из чисел имеет ведущие нули
        ('2e6', '3e7', '2000000.00 + 30000000.00 = 32000000.00'),  # Проверка сложения чисел с использованием чисел, представленных в научной нотации
])
    def test_addition_positive(self, calculator_page, left_operand, right_operand, expected_result):
        self.perform_addition(calculator_page, left_operand, right_operand)
        self.verify_result(calculator_page, expected_result)

    def perform_addition(self, calculator_page, left_operand, right_operand):
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, str(left_operand))
        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, str(right_operand))
        calculator_page.click_addition_button()
        
    def verify_result(self, calculator_page, expected_result):
        result = calculator_page.get_text(CalculatorLocators.RESULT_TEXT)
        assert result == expected_result, f'Ожидаемый результат {expected_result} не соответсвует фактическому {result}'

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

    def verify_error_message(self, calculator_page, expected_error_message):
        error_message = calculator_page.get_text(CalculatorLocators.RESULT_TEXT)
        assert error_message ==  expected_error_message











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