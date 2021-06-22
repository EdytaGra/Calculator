from unittest import mock
from math import sqrt
import math

import pytest


@pytest.mark.usefixtures('setup_calc')
class TestCalculator:

    @pytest.mark.parametrize('inputs', [['1.1', '-1.0', '0.5', '0.0'], ['2', '-0.1', '-1'], ['-10.0', '-0.3', '-99.0']])
    def test_get_user_input_input_ok(self, setup_calc, inputs):
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = inputs
            result = [float(x) for x in inputs]
            messages = ['' for x in inputs]
            assert setup_calc.get_user_input(messages) == result

    def test_get_user_input_input_incorrect(self, setup_calc):
        with pytest.raises(ValueError), \
                mock.patch('builtins.input') as mocked_input:
            mocked_input.return_value = 'some string'
            setup_calc.get_user_input([' '])

    @pytest.mark.parametrize('a, b', [(1, 2), (0.9, 0.2), (0, 0), (-1, -9)])
    def test_addition(self, setup_calc, a, b):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a, b]
            assert setup_calc.addition() == a + b

    @pytest.mark.parametrize('a', [1, 0.7, -1, -0.2, 0])
    @pytest.mark.parametrize('b', [6, 2.6, -5, 1, 0])
    def test_subtraction(self, setup_calc, a, b):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a, b]
            assert setup_calc.subtraction() == a - b

    @pytest.mark.parametrize('a', [1, 0.1, -1, 0, -0.1])
    @pytest.mark.parametrize('b', [3, 1, -2, 0.5, -0.5])
    def test_multiplication(self, setup_calc, a, b):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a, b]
            assert setup_calc.multiplication() == a * b

    def test_ZeroDivisionError(self, setup_calc):
        with pytest.raises(ZeroDivisionError), \
                mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [1, 0]
            setup_calc.division()

    @pytest.mark.parametrize('a', [1, 0.1, -1, 0, -0.1])
    @pytest.mark.parametrize('b', [3, 0.4, -6, -2, 0.5])
    def test_division(self, setup_calc, a, b):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a, b]
            assert setup_calc.division() == a / b

    @pytest.mark.parametrize('a', [1, 0.1, -3, 0.6, 0])
    @pytest.mark.parametrize('b', [3, 0.7, -2, 0.5, 1])
    def test_exponentiation(self, setup_calc, a, b):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a, b]
            assert setup_calc.exponentiation() == a ** b

    @pytest.mark.parametrize('a', [-1, -0.1, -10])
    def test_square_root_input_not_ok2(self, setup_calc, a):
        with pytest.raises(ValueError), \
                mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a]
            assert setup_calc.square_root() == sqrt(a)

    @pytest.mark.parametrize('a', [1, 0.1, 2.3])
    def test_square_root(self, setup_calc, a):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a]
            assert setup_calc.square_root() == sqrt(a)

    @pytest.mark.parametrize('a', [1, -0.1, -3, 0.1, 100])
    def test_square_area(self, setup_calc, a):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a]
            assert setup_calc.square_area() == a * a

    @pytest.mark.parametrize('a', [1, -0.1, 0, -3, 0.1])
    @pytest.mark.parametrize('b', [3, -0.4, 1, -2, 0.5])
    def test_rectangle_area(self, setup_calc, a, b):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a, b]
            assert setup_calc.rectangle_area() == a * b

    @pytest.mark.parametrize('a', [1, -0.1, 0, -3, 0.1])
    @pytest.mark.parametrize('b', [3, -0.4, 1, -2, 0.5])
    def test_triangle_area(self, setup_calc, a, b):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a, b]
            assert setup_calc.triangle_area() == a * b / 2

    @pytest.mark.parametrize('a', [1, -0.1, 0, -3, 0.1])
    def test_circle_area(self, setup_calc, a):
        with mock.patch('calculator.Calculator.get_user_input') as mocked_input:
            mocked_input.return_value = [a]
            assert setup_calc.circle_area() == math.pi * a ** 2
