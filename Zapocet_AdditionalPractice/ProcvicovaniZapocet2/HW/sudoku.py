import os

import numpy as np


class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, file_path: str) -> None:

        # list of lists (rows)
        loaded_rows: list[list[int]] = []
        # TODO implement loading of the file
        with open(file_path,"r",encoding="utf-8") as f:
            for line in f:
                currentLine = line.strip().split(";")
                currentRow = []
                for n in currentLine:
                    currentRow.append(int(n))
                loaded_rows.append(currentRow)

        # convert nested list to numpy array
        self.field = np.array(loaded_rows)



    def check_sequence(self, sequence: np.ndarray) -> bool:
        return True


    def check_row(self, row_index: int) -> bool:
        row = self.field[row_index]
        return self.check_sequence(row)

    def check_column(self, column_index: int) -> bool:
        column = self.field[:,column_index]
        return self.check_column(column)

    def check_block(self, row_index: int, column_index: int) -> bool:
        block = self.field[row_index:,column_index:]
        return self.check_sequence(block)


    def check_one_cell(self, row_index: int , column_index: int) -> bool:
        cell = self.field[row_index,column_index]
        row = np.array(self.field[row_index])
        column = np.arange(self.field[:,column_index])
        for n in row:
            if n == cell:
                return False
        for n in column:
            if n == cell:
                return False
        return True
    
    def get_empty_cell(self) -> tuple[int, int] | None:
        """ Gets the coordinates of the next empty field. """
        return None

    def solve(self) -> bool:
        """ Recursively solves the sudoku. """
        return False





def main() -> None:
    sudoku_solver = SudokuSolver()
    sudoku_solver.load("sudoku.csv")

if __name__ == "__main__":
    main()