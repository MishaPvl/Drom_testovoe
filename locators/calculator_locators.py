from appium.webdriver.common.mobileby import MobileBy


class CalculatorLocators:
    LEFT_INPUT_FIELD = (MobileBy.ACCESSIBILITY_ID, 'inputFieldLeft')
    RIGHT_INPUT_FIELD = (MobileBy.ACCESSIBILITY_ID, 'inputFieldRight')
    ADDITION_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'additionButton')
    SUBTRACTION_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'subtractButton')
    MULTIPLICATION_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'multiplicationButton')
    DIVISION_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'divisionButton')
    RESET_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'resetButton')
    RESULT_TEXT = (MobileBy.ACCESSIBILITY_ID, 'resultTextView')
