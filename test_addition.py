from add import calculate_add


def test_positive_numbers():
    assert calculate_add(20, 40) == 60


def test_zero():
    assert calculate_add(50, 0) == 50


def test_negative_numbers():
    assert calculate_add(-50, -10) == -60
{
    "test_addition.py::test_zero": true,
    "test_addition.py::test_positive": true,
    "test_addition.py::test_negative": true
}