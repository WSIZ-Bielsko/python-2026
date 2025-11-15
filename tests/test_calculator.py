import pytest
from python_2026.gg1.calculator import add, sub, mul, div


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, -6) == -10


def test_sub_result_positive():
    assert sub(10, 3) == 7


def test_sub_result_negative():
    assert sub(3, 10) == -7


def test_mul_basic():
    assert mul(4, 5) == 20


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

