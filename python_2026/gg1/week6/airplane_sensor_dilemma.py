def verify_sensors(values: list[int]) -> str | int:
    """
    Returns "sensor readings correct" if all values are equal, or
    number of sensor (0-based) if one is incorrect or
    "general error" otherwise.

    len(values)==3
    """
    # todo


def test_all_values_equal_returns_correct_message():
    assert verify_sensors([100, 100, 100]) == "sensor readings correct"


def test_first_sensor_different_returns_zero():
    assert verify_sensors([100, 101, 101]) == 0


def test_second_sensor_different_returns_one():
    assert verify_sensors([101, 100, 101]) == 1


def test_third_sensor_different_returns_two():
    assert verify_sensors([101, 101, 100]) == 2


def test_two_different_sensors_returns_general_error():
    assert verify_sensors([100, 101, 102]) == "general error"


def test_all_three_different_returns_general_error():
    assert verify_sensors([1, 2, 3]) == "general error"


def test_empty_list_returns_general_error():
    assert verify_sensors([]) == "general error"


if __name__ == '__main__':
    pass
