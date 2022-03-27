from typing import List, Dict


from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


class UniqueColsAndRowsConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variables: List[VariablePosition], size):
        super().__init__(variables)
        self.size = size

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        full_rows = []
        full_columns = []

        for i in range(self.size):
            current_row: list[int] = []
            current_column: list[int] = []

            for position in assignment.keys():
                if position.row_number == i:
                    current_row.append(assignment[position])

                if position.column_number == i:
                    current_column.append(assignment[position])

            if len(current_row) == self.size:
                full_rows.append(current_row)

            if len(current_column) == self.size:
                full_columns.append(current_column)

        list_of_rows = map(tuple, full_rows)
        list_of_columns = map(tuple, full_columns)

        rows_set = {*list_of_rows}
        columns_set = {*list_of_columns}

        return len(full_rows) == len(rows_set) and len(full_columns) == len(columns_set)
