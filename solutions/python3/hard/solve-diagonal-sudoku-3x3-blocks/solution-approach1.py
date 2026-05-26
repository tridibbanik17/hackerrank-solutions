# ──────────────────────────────────────────────────
# Problem     Solve Diagonal Sudoku with 3x3 Blocks
# Difficulty  Hard
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-26, 01:56 a.m.
# Technique   backtracking-constraint-solver
# Time        O(9^N)
# Space       O(N)
# Trick       Use recursive backtracking with conditional checks for row, column, block, and both diagonals to prune the search space efficiently.
# Hint        Use row // 3 * 3 for block indexing.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'completeDiagonalSudokuGrid' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def completeDiagonalSudokuGrid(grid):
    def is_valid(grid, row, col, num):
        # Check row
        if num in grid[row]:
            return False
        
        # Check column
        if num in [grid[r][col] for r in range(9)]:
            return False
        
        # Check 3x3 block
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if grid[r][c] == num:
                    return False
        
        # Check main diagonal (top-left to bottom-right)
        if row == col:
            if num in [grid[i][i] for i in range(9)]:
                return False
        
        # Check anti-diagonal (top-right to bottom-left)
        if row + col == 8:
            if num in [grid[i][8 - i] for i in range(9)]:
                return False
        
        return True

    def backtrack(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if backtrack(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    backtrack(grid)
    return grid

if __name__ == '__main__':
    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = completeDiagonalSudokuGrid(grid)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
