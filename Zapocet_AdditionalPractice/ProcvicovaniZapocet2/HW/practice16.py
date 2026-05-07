import random
import stat
import os

import numpy as np


class SudokuSolver:
    def __init__(self):
        self.field = np.zeros([9, 9], dtype=int)

    def load(self, file_path: str) -> None:

        # list of lists (rows)
        loaded_rows: list[list[int]] = []
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                line_field = line.strip().split(";")
                radek = []
                for c in line_field:
                    radek.append(int(c))
                loaded_rows.append(radek)

        # convert nested list to numpy array
        self.field = np.array(loaded_rows)

    def check_sequence(self, sequence: np.ndarray) -> bool:
        seen = set()
        for i in sequence:
            if i == 0:
                continue
            if i in seen:
                return False
            seen.add(i)
        return True

    def check_row(self, row_index: int) -> bool:
        row = self.field[row_index]
        return self.check_sequence(row)

    def check_column(self, column_index: int) -> bool:
        # : vezme všechny řádky a column_index sloupec, což nám dá celý sloupec jako pole
        column = self.field[:, column_index]
        return self.check_sequence(column)

    # vypočítáme indexy pro blok, který obsahuje buňku (row_index, column_index), a zkontrolujeme, jestli v něm nejsou duplicitní čísla
    # aritmetika pro zajištění toho, že pro indexy 0-2 se vrátí 0, pro 3-5 se vrátí 3 a pro 6-8 se vrátí 6, což nám umožní získat správný blok
    def check_block(self, row_index: int, column_index: int) -> bool:
        calculate_row_index = (row_index // 3) * 3  # 0-2 -> 0, 3-5 -> 3, 6-8 -> 6
        calculate_column_index = (column_index // 3) * 3  # 0-2 -> 0, 3-5 -> 3, 6-8 -> 6
        # vyřízne blok o velikosti 3x3 z pole, začínající na vypočítaných indexech
        block = self.field[
            # řádky od calculate_row_index do calculate_row_index + 3 (ne včetně)
            calculate_row_index : calculate_row_index + 3,
            # sloupce od calculate_column_index do calculate_column_index + 3 (ne včetně)
            calculate_column_index : calculate_column_index + 3,
        ]
        return self.check_sequence(block.flatten())

    def check_one_cell(self, row_index: int, column_index: int) -> bool:
        return (
            self.check_block(row_index, column_index)
            and self.check_row(row_index)
            and self.check_column(column_index)
        )

    def get_empty_cell(self) -> tuple[int, int] | None:
        """Gets the coordinates of the next empty field."""
        for x in range(len(self.field)):
            for y in range(len(self.field[x])):
                if self.field[x][y] == 0:
                    return (x, y)
        return None

    def solve(self) -> bool:

        # najdu prazdne misto
        empty_cell = self.get_empty_cell()

        if empty_cell is None:  # neni prazdne misto, jsem hotov, jsme na konci
            return True

        x, y = empty_cell

        # zkusim vsechny mozne cisla
        for i in range(1, 10):
            self.field[empty_cell] = i  # zkusím vločit číslo do pole
            # zkontroluji, jestli je vložené číslo v pořádku
            if not self.check_one_cell(x, y):
                continue  # pokud není, zkouším další číslo

            # rekurzině zkusím vyřešit zbytek pole, vezme se následující prádné místo a provede se totéž
            if self.solve():
                return True

        # pokud žádné číslo nefungovalo, vrátím pole do původního stavu a vrátím False, což způsobí,
        # že se algoritmus vrátí o krok zpět a zkusí jiné číslo pro předchozí prázdné místo
        self.field[x][y] = 0

        # return False
        return False


def main() -> None:
    sudoku_solver = SudokuSolver()
    sudoku_solver.load("sudoku.csv")
    print(sudoku_solver.field)
    sudoku_solver.solve()
    print(" ")
    print(sudoku_solver.field)

    # print(sudoku_solver.field)
    # print(sudoku_solver.check_row(0))
    # print(sudoku_solver.check_column(0))
    # sudoku_solver.field[0][0] = 4
    # print(sudoku_solver.field)
    # print(sudoku_solver.check_block(1, 1))

    # print(sudoku_solver.get_empty_cell())

    pole = np.array([1, 2, 3, 4, 5, 6])
    twodpole = pole.reshape(2, 3)
    print(np.sum(twodpole, axis=0))  # 1 + 4, 2 + 5, 3 + 6
    pole2 = pole.copy()
    pole2[0] = 2
    print(np.unique(pole2))  # vrátí pole s unikátními hodnotami
    print(pole[pole < 4])  # vrátí pole s hodnotami menšími než 4
    print(
        twodpole[twodpole < 4]
    )  # funguje i pro 2D pole, vrátí všechny hodnoty menší než 4 a vrátí je jako 1D pole


if __name__ == "__main__":
    main()