"""Advent of Code, Day 2
"""
from typing import List


class Submarine:
    """Base class for submarine
    """

    def __init__(self, start_aim: int = 0, start_depth: int = 0, start_position: int = 0):
        self._aim = start_aim
        self._depth = start_depth
        self._position = start_position

    def move(self, instructions: List[str]):
        for instruction in instructions:
            inst, n = instruction.split(' ')
            if not hasattr(self, f'move_{inst}'):
                raise NotImplementedError(f"The instruction {inst} could not be executed "
                                          f"because `move_{inst}()` is not implemented.")
            getattr(self, f'move_{inst}')(int(n))
        return self

    def get_depth_x_position(self):
        return self._position * self._depth


class SubmarineNaive(Submarine):
    """Submarine, with naive navigation
    """

    def move_up(self, n: int):
        self._depth -= n

    def move_down(self, n: int):
        self._depth += n

    def move_forward(self, n: int):
        self._position += n


class SubmarineCorrect(Submarine):
    """Submarine, with correct navigation
    """

    def move_up(self, n: int):
        self._aim -= n

    def move_down(self, n: int):
        self._aim += n

    def move_forward(self, n: int):
        self._position += n
        self._depth += n * self._aim


if __name__ == '__main__':

    test_inst = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    with open('./input.txt') as fbuffer:
        inst = [line.strip() for line in fbuffer.readlines()]

    print('Problem 1 (Test): ', SubmarineNaive().move(test_inst).get_depth_x_position())
    print('Problem 2 (Test): ', SubmarineCorrect().move(test_inst).get_depth_x_position())
    print('Problem 1 (Full): ', SubmarineNaive().move(inst).get_depth_x_position())
    print('Problem 2 (Full): ', SubmarineCorrect().move(inst).get_depth_x_position())
