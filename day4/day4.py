"""Advent of Code, Day 4
"""
from typing import List


def _parse_puzzle_input(puzzle_input: str):
    """Parse the puzzle input"""
    puzzle_input = [line.strip() for line in puzzle_input.split('\n\n')]
    numbers, boards = puzzle_input[0], puzzle_input[1:]

    numbers = [int(i.strip()) for i in numbers.strip().split(',')]
    boards_dict = {}
    for n, board in enumerate(boards, start=1):
        board = [[int(cell.strip()) for cell in row.split()]
                 for row in board.split('\n')]
        boards_dict[f'board_{n}'] = board
    return numbers, boards_dict


def transpose(mtx: List[list]):
    """Transpose the board"""
    transposed_tuples = list(zip(*mtx))
    return [list(sublist) for sublist in transposed_tuples]


class Bingo:

    def __init__(self, puzzle_input: str, marker: str = 'X'):
        self.marker = marker
        self.numbers, self.boards_dict = _parse_puzzle_input(puzzle_input)

    def mark_board(self, board: List[list], number: int):
        """Mark the board"""
        return [[self.marker if cell == number else cell for cell in row]
                for row in board]

    def check_win(self, board: List[list]):
        """Check if this is a winning board"""
        for row in board:
            if all(cell == self.marker for cell in row):
                return True
        for col in transpose(board):
            if all(cell == self.marker for cell in col):
                return True
        return False     

    def play_game_to_win(self):
        """Play the game, and win"""
        for number in self.numbers:
            for board_name, board in self.boards_dict.items():
                marked_board = self.mark_board(board, number)
                if self.check_win(marked_board):
                    return marked_board, number
                self.boards_dict[board_name] = marked_board
        return None, number

    def play_game_to_lose(self):
        """Play the game, and lose"""
        winners, n_boards = set(), len(self.boards_dict)
        for number in self.numbers:
            for board_name, board in self.boards_dict.items():
                if board_name in winners: continue
                marked_board = self.mark_board(board, number)
                if self.check_win(marked_board):
                    winners.add(board_name)
                    if len(winners) == n_boards:
                        return marked_board, number
                self.boards_dict[board_name] = marked_board
        return None, number

    def play_game_and_calculate_score(self, win=True, verbose=False):
        """Calculate the winning score"""
        board, number = self.play_game_to_win() if win else self.play_game_to_lose()
        if board is None: return -1
        summed = sum(cell for row in board for cell in row if cell != self.marker)
        return summed * number


if __name__ == '__main__':

    test = (
        """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
        8  2 23  4 24
        21  9 14 16  7
        6 10  3 18  5
        1 12 20 15 19

        3 15  0  2 22
        9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
        2  0 12  3  7"""
    )

    with open('./input.txt') as fbuffer:
        puzzle_input = fbuffer.read()

    print('Problem 1 (Test): ', Bingo(test).play_game_and_calculate_score())
    print('Problem 1 (Full): ', Bingo(puzzle_input).play_game_and_calculate_score())
    print('Problem 2 (Test): ', Bingo(test).play_game_and_calculate_score(win=False))
    print('Problem 2 (Full): ', Bingo(puzzle_input).play_game_and_calculate_score(win=False))