from locators.calculator_locators import CalculatorLocators
import pytest

'''
    Класс TestCalculatorInputFields содержит тесты для проверки ввода данных в поля калькулятора.
    При ручном тестировании поля для ввода не позволяют вводить невалидные значения, такие как буквы или символы. Однако, в автотестах при использовании метода send_keys(), можно передавать любые значения в поле. Важно отметить, что большая часть невалидных значений будет обработана при выполнении операций (+, -, и т.д.).
'''

class TestCalculatorInputFields:
    # def test_empty_input_fields_on_startup(self, calculator_page):
    #     # Проверяем, что при запуске приложения оба поля пустые.
    #     calculator_page.check_input_fields_empty()

    def test_integer_input_fields(self, calculator_page):
        # Введите целое число в первое и второе поле для ввода и убедитесь, что они правильно принимают вводимые данные.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '10')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '10', 'Поле ввода левого операнда содержит неверное значение.'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '5')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '5', 'Поле ввода правого операнда содержит неверное значение.'

    def test_invalid_input(self, calculator_page):
        # Введите недопустимые символы в оба поля для ввода и убедитесь, что они не приняты.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, 'abc')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '', 'Поле ввода левого операнда приняло недопустимые символы'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '@#$')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '', 'Поле ввода правого операнда приняло недопустимые символы'

    def test_very_large_number_input(self, calculator_page):
        # Введите очень большое число в оба поля и убедитесь, что оно принято и отображается правильно..
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '999999999999999')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '999999999999999', 'Поле ввода левого операнда содержит неверное значение.'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '999999999999999')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '999999999999999', 'Поле ввода правого операнда содержит неверное значение.'

    def test_decimal_number_input(self, calculator_page):
        # Введите десятичное число в оба поля ввода и убедитесь, что оно принято и отображается правильно.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '3.14')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '3.14', 'Поле ввода левого операнда некорректно отображает десятичное число'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '2.5')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '2.5', 'Поле ввода правого операнда некорректно отображает десятичное число'

    def test_negative_number_input(self, calculator_page):
        # Проверка ввода отрицательных чисел
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '-7')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '-7', 'Поле ввода левого операнда некорректно отображает отрицательное число'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '-2')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '-2', 'Поле ввода правого операнда некорректно отображает отрицательное число'

    def test_zero_input(self, calculator_page):
        # Введите 0 и убедитесь, что число принято и отображается правильно.
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '0')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '0', 'Поле ввода левого операнда содержит неверное значение'

        calculator_page.enter_number(CalculatorLocators.RIGHT_INPUT_FIELD, '0')
        result = calculator_page.get_text(CalculatorLocators.RIGHT_INPUT_FIELD)
        assert result == '0', 'Поле ввода правого операнда содержит неверное значение'
    
    def test_valid_number_single_field(self, calculator_page):
        # Убедитесь, что калькулятор не выполняет никаких вычислений, если число есть только в одном поле
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '10')
        result = calculator_page.get_text(CalculatorLocators.RESULT_TEXT)
        assert result == '', 'Калькулятор выполняет вычисление при наличии числа только в одном поле'
    
    def test_leading_zeros_input(self, calculator_page):
        # Проверка ввода числа с ведущими нулями
        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '00123')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '123', 'Поле ввода левого операнда содержит неверное значение'

        calculator_page.enter_number(CalculatorLocators.LEFT_INPUT_FIELD, '00256')
        result = calculator_page.get_text(CalculatorLocators.LEFT_INPUT_FIELD)
        assert result == '256', 'Поле ввода правого операнда содержит неверное значение'