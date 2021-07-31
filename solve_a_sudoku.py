from itertools import product


def print_sudoku(puzzle):
    for i in range(len(puzzle)):
        row_string = ''
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 0:
                row_string += f' {puzzle[i][j]} '
            else:
                row_string += ' * '
            # handles the vertical dividers
            if j % 3 == 2 and j != len(puzzle[i]) - 1:
                row_string += " | "
        # handles the horizontal dividers
        if i % 3 == 0 and i != 0:
            print("-" * 33)
        print(row_string)


def solve_sudoku(puzzle):
    if not puzzle:
        return

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    valid = True
                    # check if num is in the row or column already
                    for i in range(0, 9):
                        if (puzzle[i][col] == num) or (puzzle[row][i] == num):
                            valid = False
                            break
                    # check if num is in the block
                    for i in range(3):
                        for j in range(3):
                            if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                                valid = False
                                break
                    if valid:
                        # num is valid so assign to current row, col in puzzle
                        # then solve the sudoku for new sudoku
                        puzzle[row][col] = num
                        solution = solve_sudoku(puzzle)
                        if solution:
                            return solution
                        else:
                            puzzle[row][col] = 0
                return False  # num if not valid in row, col, or block
    return puzzle


def solution(puzzle):
    for (row, col) in product(range(0,9), repeat=2):
        if puzzle[row][col] == 0: # find an unassigned cell
            for num in range(1,10):
                allowed = True # check if num is allowed in row/col/box
                for i in range(0,9):
                    if (puzzle[i][col ] == num) or (puzzle[row][i] == num):
                        allowed = False; break # not allowed in row or col
                for (i, j) in product(range(0,3), repeat=2):
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False; break # not allowed in box
                if allowed:
                    puzzle[row][col] = num
                    #if trial := solve_sudoku(puzzle):
                    #    return trial
                    #else:
                    #    puzzle[row][col] = 0
            return False # could not place a number in this cell
    return puzzle