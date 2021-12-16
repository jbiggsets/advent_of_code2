"""Advent of Code, Day 1
"""


def check_increase_or_decrease(arr: list, window: int = 3) -> str:
    """Solve increasing/decreasing problem, with rolling windows"""
    for i in range(len(arr) - window):
        res1, res2 = sum(arr[i: i + window]), sum(arr[i + 1: i + window + 1])
        if res1 < res2: yield 'increase'
        elif res1 == res2: yield 'no change'
        else: yield 'decrease'


def count_increasing(arr: list, window: int = 3) -> int:
    """Count the nuber increasing"""
    return sum(1 for m in check_increase_or_decrease(arr, window) if m == 'increase')


if __name__ == '__main__':

    test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    with open('./input.txt') as fbuffer:
        arr = [int(line.strip()) for line in fbuffer.readlines()]

    print('Problem 1 (Test): ', count_increasing(test, window=1))
    print('Problem 2 (Test): ', count_increasing(test, window=3))
    print('Problem 1 (Full): ', count_increasing(arr, window=1))
    print('Problem 2 (Full): ', count_increasing(arr, window=3))
