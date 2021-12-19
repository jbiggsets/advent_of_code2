"""Advent of Code, Day 5
"""


def _parse_puzzle_input(puzzle_input: str):
    """Parse the puzzle input"""
    puzzle_input = [line.strip().split(' -> ') for line in puzzle_input.strip().split('\n')]
    coordinates = [(i.split(','), j.split(',')) for i, j in puzzle_input]
    coordinates = [(int(x1), int(y1), int(x2), int(y2)) for (x1, y1), (x2, y2) in coordinates]
    return coordinates


class Board:

    def __init__(self, coordinates: tuple):
        self._board = self._create_board(coordinates)
        self._coord = coordinates

    def _create_board(self, coordinates: tuple):
        maximum = max(max(i) for i in coordinates)
        board = [[0 for i in range(maximum + 1)] for _ in range(maximum + 1)]
        return board

    def add_coordinate(self, coordinate: tuple, with_diag: bool = False):
        """Add coordinate"""
        x1, y1, x2, y2 = coordinate
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        # add horizontal 
        if abs(x1 - x2) > 0 and y1 == y2:
            for x in range(x1, x2 + x_step, x_step):
                self._board[y1][x] += 1
        # add vertical
        elif abs(y1 - y2) > 0 and x1 == x2:
            for y in range(y1, y2 + y_step, y_step):
                self._board[y][x1] += 1
        # add diagonal
        elif abs(x1 - x2) == abs(y1 - y2) != 0 and with_diag:
            x, y = x1, y1
            while True:
                self._board[y][x] += 1
                if x == x2 and y == y2: break
                x += x_step
                y += y_step

    def solve(self, with_diag: bool = False):
        """Solve the problem"""
        for coordinate in self._coord:
            self.add_coordinate(coordinate, with_diag)
        return sum(1 for i in self._board for j in i if j >= 2)



if __name__ == '__main__':

    test = (
        """
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2"""
    )

    with open('./input.txt') as fbuffer:
        coord = fbuffer.read()

    print('Problem 1 (Test): ', Board(_parse_puzzle_input(test)).solve())
    print('Problem 2 (Test): ', Board(_parse_puzzle_input(test)).solve(with_diag=True))
    print('Problem 1 (Full): ', Board(_parse_puzzle_input(coord)).solve())
    print('Problem 2 (Full): ', Board(_parse_puzzle_input(coord)).solve(with_diag=True))
