from unittest import mock
from calculator import Calculator


class TestCalculator:

    def test_addition(self):
        with mock.patch(Calculator.get_user_input) as mocked_input:
            mocked_input.return_value = [1, 2]
            calc = Calculator()
            assert calc.addition() == 3
