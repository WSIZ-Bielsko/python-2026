import pytest
from python_2026.gg1.sum_avg import sum_and_avg  # <- dostosuj nazwę modułu


def test_positive_integers():
    assert sum_and_avg([1, 2, 3, 4, 5]) == (15.0, 3.0)


def test_floats():
    total, avg = sum_and_avg([2.5, 3.5, 4.0])
    assert total == 10.0
    assert avg == pytest.approx(3.3333333333)


def test_negative_numbers():
    total, avg = sum_and_avg([-3, -7, -10])
    assert total == -20.0
    assert avg == pytest.approx(-6.6666666667)


def test_mixed_numbers():
    assert sum_and_avg([-2, 5, 10, -3]) == (10.0, 2.5)


def test_single_element():
    assert sum_and_avg([42]) == (42.0, 42.0)


def test_empty_list_returns_zeroes():
    assert sum_and_avg([]) == (0.0, 0.0)


def test_large_numbers():
    total, avg = sum_and_avg([1_000_000, 2_000_000, 3_000_000])
    assert total == 6_000_000.0
    assert avg == 2_000_000.0
