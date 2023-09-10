from average import calculate_average

def test_average_non_empty_list():
    numbers = [5, 10, 15, 20]
    assert calculate_average(numbers) == 12.5

def test_average_empty_list():
    numbers = []
    assert calculate_average(numbers) == 0

def test_average_single_element_list():
    numbers = [8]
    assert calculate_average(numbers) == 8.0

def test_average_negative_numbers():
    numbers = [-5, -10, -15, -20]
    assert calculate_average(numbers) == -12.5

def test_average_decimal_numbers():
    numbers = [1.5, 2.5, 3.5]
    assert calculate_average(numbers) == 2.5
