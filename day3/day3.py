"""Advent of Code, Day 3
"""
from collections import Counter
from typing import List


def criterion_common(sub_arr: list, most_common: bool = True):
    """Get the most or least common elmement in array
    """
    counter = Counter(sub_arr)
    return counter.most_common()[0 if most_common else 1][0]


def criterion_equal(sub_arr: list) -> bool:
    """Check of elements in array are equally likely
    """
    values = list(Counter(sub_arr).values())
    return values.count(values[0]) == len(values)


def criterion_bit(arr: list, j_col: int, most_common: bool = True):
    """The bit criteria
    """
    sub_arr = [row[j_col] for row in arr]
    if criterion_equal(sub_arr):
        criterion = '1' if most_common else '0'
    else:
        criterion = criterion_common(sub_arr, most_common)
    return [i for i, row in enumerate(arr) if row[j_col] == criterion]


def calculate_diagnostic(arr: List[str], most_common: bool = True):
    """Calculate diagnostic
    """
    numbers = []
    for j_col in range(len(arr[0])):
        number = criterion_common([row[j_col] for row in arr], most_common)
        numbers.append(number)
    return int(''.join(numbers), 2)


def calculate_rating(arr: List[str], most_common: bool = True):
    """Calculate rating
    """
    numbers = [row for row in arr]
    for j_col in range(len(arr[0])):
        indexes = criterion_bit(numbers, j_col, most_common)
        if len(indexes) == 1:
            return int(numbers[indexes[0]], 2)
        numbers = [row for i, row in enumerate(numbers) if i in indexes]


def calculate_power_consumption(arr: List[str]):
    """Calculate the overall power consumption
    """
    gamma = calculate_diagnostic(arr, True)
    epsilon = calculate_diagnostic(arr, False)
    return epsilon * gamma


def calculate_life_support_rating(arr: List[str]):
    """Calculate the life support rating
    """
    oxygen = calculate_rating(arr, True)
    scrubber = calculate_rating(arr, False)
    return oxygen * scrubber


if __name__ == '__main__':

    test = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    with open('./input.txt') as fbuffer:
        diag = [line.strip() for line in fbuffer.readlines()]

    print('Problem 1 (Test): ', calculate_power_consumption(test))
    print('Problem 2 (Test): ', calculate_life_support_rating(test))
    print('Problem 1 (Full): ', calculate_power_consumption(diag))
    print('Problem 2 (Full): ', calculate_life_support_rating(diag))
