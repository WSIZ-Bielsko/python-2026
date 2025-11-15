import pytest


def get_max_above_average(data: list[float]) -> float:
    avg = sum(data) / len(data)
    mx = data[0] - avg
    for d in data:
        mx = max(mx, d - avg)
    return mx


def test_1():
    data = [1, 2, 3]
    assert get_max_above_average(data) == 1


def test_2():
    data = [0, 2, 2, 2, 4]
    assert get_max_above_average(data) == 2


def test_3():
    data = [0, 1]
    assert get_max_above_average(data) == pytest.approx(0.5)
    # assert 0.1 + 0.2 == pytest.approx(0.3)


def get_max_acceleration(velocities: list[float]) -> float:
    acc = []
    for i in range(len(velocities) - 1):
        acc.append(velocities[i + 1] - velocities[i])
    return max(acc)


def test_a1():
    vel = [1, 2, 3]
    assert get_max_acceleration(vel) == pytest.approx(1)


def test_a2():
    vel = [1, 2, 3, 10]
    assert get_max_acceleration(vel) == pytest.approx(7)
