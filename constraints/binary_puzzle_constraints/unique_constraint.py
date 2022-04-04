from typing import Dict

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if rows columns (variables) have unique arrangement
class UniqueConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variables: list[VariablePosition], size):
        super().__init__(variables)
        self.size = size  # size is width/height of puzzle

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        fully_filled_rows = []
        fully_filled_columns = []

        for i in range(self.size):
            current_row: list[int] = []
            current_column: list[int] = []
            current_row_vars: list[VariablePosition] = []
            current_column_vars: list[VariablePosition] = []

            for position in assignment.keys():
                if position.row_number == i:
                    current_row_vars.append(position)

                if position.column_number == i:
                    current_column_vars.append(position)

            current_column_vars = sorted(current_column_vars, key=lambda x: x.row_number)
            current_column = [assignment[position] for position in current_column_vars]

            current_row_vars = sorted(current_row_vars, key=lambda x: x.column_number)
            current_row = [assignment[position] for position in current_row_vars]

            if len(current_row) == self.size:
                fully_filled_rows.append(current_row)

            if len(current_column) == self.size:
                fully_filled_columns.append(current_column)

        list_of_rows = map(tuple, fully_filled_rows)
        list_of_columns = map(tuple, fully_filled_columns)

        rows_set = {*list_of_rows}
        columns_set = {*list_of_columns}

        return len(fully_filled_rows) == len(rows_set) and len(fully_filled_columns) == len(columns_set)
