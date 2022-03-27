from constraints.futoshiki_puzzle_constraints.unary_constraint import UnaryConstraint
from constraints.futoshiki_puzzle_constraints.compare_constraint import CompareConstraint
from constraints.futoshiki_puzzle_constraints.completeness_constraint import CompletenessConstraint


class Futoshiki_Puzzle:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = (data + '-').split('\n')
        self.variables = []  # krotki (y, x)
        self.domains = {}
        self.constraints = []
        self.__transform_data()
        self.__generate_row_completeness_constraints()
        self.__generate_columns_completeness_constraints()

    def __transform_data(self):
        for row in range(2 * self.rows - 1):
            for column in range(len(self.data[row])):
                if not self.data[row][column] == '>' and not self.data[row][column] == '<' and not self.data[row][column] == '-':
                    variable = (row, column)
                    self.variables.append((row, column))
                    self.domains[variable] = list(range(1, self.rows + 1))
                    if self.data[row][column] != 'x':
                        self.constraints.append(UnaryConstraint((row, column), lambda assignment, v=int(self.data[row][column]): assignment == v))

                elif row % 2 == 0:
                    if self.data[row][column] == '>':
                        bigger = (row, column - 1)
                        smaller = (row, column + 1)
                        self.constraints.append(CompareConstraint(smaller, bigger))
                    elif self.data[row][column] == '<':
                        bigger = (row, column + 1)
                        smaller = (row, column - 1)
                        self.constraints.append(CompareConstraint(smaller, bigger))

                else:
                    if self.data[row][column] == '>':
                        bigger = (row - 1, 2 * column)
                        smaller = (row + 1, 2 * column)
                        self.constraints.append(CompareConstraint(smaller, bigger))
                    elif self.data[row][column] == '<':
                        bigger = (row + 1, 2 * column)
                        smaller = (row - 1, 2 * column)
                        self.constraints.append(CompareConstraint(smaller, bigger))

    def __generate_row_completeness_constraints(self):
        for row in range(self.rows):
            self.constraints.append(CompletenessConstraint([(2 * row, 2 * column) for column in range(self.columns)]))

    def __generate_columns_completeness_constraints(self):
        for column in range(self.columns):
            self.constraints.append(CompletenessConstraint([(2 * row, 2 * column) for row in range(self.rows)]))

    def __str__(self):
        return f'Futoshiki puzzle - rows: {self.rows} columns: {self.columns} data: {self.data}'
