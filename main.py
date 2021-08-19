from termcolor import colored
import sys
import time

"""
sample = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
"""

sample = [
    [0, 6, 5, 1, 0, 0, 0, 2, 0],
    [1, 0, 0, 0, 0, 6, 0, 8, 0],
    [0, 0, 9, 2, 3, 0, 0, 0, 0],
    [0, 1, 0, 0, 6, 0, 0, 0, 0],
    [3, 5, 0, 0, 0, 1, 0, 6, 2],
    [0, 9, 0, 0, 2, 0, 5, 0, 3],
    [0, 0, 0, 6, 0, 0, 9, 0, 8],
    [0, 7, 0, 9, 1, 0, 0, 4, 0],
    [0, 4, 6, 5, 0, 0, 2, 3, 0],
]


def print_puzzle(puzzle, guess, row, col):
    for r in range(9):
        for c in range(9):
            if row == r and col == c:
                print(colored(f"{guess}", "green"), end="\r")
            else:
                print(puzzle[r][c], end="  ")
        print()

    time.sleep(5)


def find_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None


def is_valid(puzzle, row, col, guess):
    # check row values
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # check col values
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # check squar values
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def solver(puzzle):

    row, col = find_next_empty(puzzle)

    # Puzzle is completed
    if row is None:
        return True

    # Loop through all guesses (backtracking)
    for guess in range(1, 10):

        print_puzzle(puzzle, guess, row, col)
        time.sleep(speed)
        if is_valid(puzzle, row, col, guess):
            puzzle[row][col] = guess

            if solver(puzzle):
                return True

        puzzle[row][col] = 0
    return False


speed = 10 ** (-2)
# solver(sample)
print(sample)
