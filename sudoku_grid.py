def row_correct(sudoku: list, row_no: int):
    numbers_in_row = []

    for integer in sudoku[row_no]:
        if integer in numbers_in_row:
            return False

        if 1 <= integer <= 9:
            numbers_in_row.append(integer)

    return True

def column_correct(sudoku: list, column_no: int):
    matching_numbers = []

    for row in sudoku:
        if row[column_no] in matching_numbers:
            return False

        if 1 <= row[column_no] <= 9:
            matching_numbers.append(row[column_no])
        
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []

    for row in sudoku[row_no: row_no + 3]:
        for integer in row[column_no: column_no + 3]:
            if integer in numbers:
                return False
            
            if 1 <= integer <= 9:
                numbers.append(integer)
    
    return True

def sudoku_grid_correct(sudoku: list):
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False
    
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False
    
    for row_no in [0,3,6]:
        for column_no in [0,3,6]:
            if not block_correct(sudoku, row_no, column_no):
                return False
    

    return True

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))
