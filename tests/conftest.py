import pytest

from calculator import Calculator


@pytest.fixture()
def setup_calc():
    calc = Calculator()
    return calc
