#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


class NQueensSolver:
    """Class Solution"""
    def __init__(self, N):
        """Initialize a new Solver.

        Args:
            N (int): The width and height of the new chessboard.
        """
        self._N = N
        self.solutions = []

    @property
    def N(self):
        """Get/set the chessboard dimensions."""
        return self._N

    @N.setter
    def N(self, value):
        if not isinstance(value, int):
            self.print_and_exit("N must be a number")
        if value < 4:
            self.print_and_exit("N must be at least 4")
        self._N = value

    @staticmethod
    def print_and_exit(message):
        """Print Error Message and exit."""
        print(message)
        sys.exit(1)

    def is_safe(self, board, row, col):
        """Check if there is a queen in the same column


        Args:
            row (int): The cell row id of the chessboard.
            col (int): The cell column id of the chessboard.
            board : The chessboard array of N X N
        """
        for i in range(row):
            if board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, self.N)):
            if board[i][j] == 1:
                return False
        return True

    def solve_n_queens_util(self, board, row):
        """Backtracking function to check each cell


        Args:
            row (int): The cell row id of the chessboard.
            board : The chessboard array of N X N
        """
        if row == self.N:
            solution = []
            for i in range(self.N):
                for j in range(self.N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            self.solutions.append(solution)
            return

        for col in range(self.N):
            if self.is_safe(board, row, col):
                board[row][col] = 1
                self.solve_n_queens_util(board, row + 1)
                board[row][col] = 0

    def solve_n_queens(self):
        board = [[0] * self.N for _ in range(self.N)]
        self.solutions = []
        self.solve_n_queens_util(board, 0)
        return self.solutions

if __name__ == "__main__":


    if len(sys.argv) != 2:
        NQueensSolver.print_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        NQueensSolver.print_and_exit("N must be a number")

    solver = NQueensSolver(N)
    solutions = solver.solve_n_queens()

    if solutions:
        for solution in solutions:
            print(solution)
    else:
        print(f"No solutions found for N = {N}")
