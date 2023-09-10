#You are given a list of integers. Write a Python function that returns the average of the numbers in the list. Your function should be able to handle empty lists and return 0 in that case.

def calculate_average(numbers) -> int:
    return sum(numbers) / len(numbers) if numbers else 0

