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