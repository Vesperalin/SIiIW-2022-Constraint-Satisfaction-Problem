from constraints.futoshiki_puzzle_constraints.unary_constraint import UnaryConstraint
from constraints.futoshiki_puzzle_constraints.compare_constraint import CompareConstraint
from constraints.futoshiki_puzzle_constraints.completeness_constraint import CompletenessConstraint
from puzzle.variable_position import VariablePosition


class Futoshiki_Puzzle:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = (data + '-').split('\n')
        self.variables = []  # krotki (y, x)
        self.domains = {}
        self.constraints = []
        self.__transform_data()
        self.__generate_comparison_constraints()
        self.__generate_completeness_constraints()

    def __transform_data(self):
        for row in list(filter(lambda x: x % 2 != 1, list(range(0, 2 * self.rows - 1)))):
            for column in range(len(self.data[row])):
                if not self.data[row][column] == '>' and not self.data[row][column] == '<' and not self.data[row][column] == '-':
                    variable = VariablePosition(row, column)
                    self.variables.append(variable)
                    self.domains[variable] = list(range(1, self.rows + 1))
                    if self.data[row][column] != 'x':
                        self.constraints.append(UnaryConstraint(variable, lambda assignment, v=int(self.data[row][column]): assignment == v))

    def __find_variable_position(self, row, column):
        return list(filter(lambda var_position: var_position.row_number == row and var_position.column_number == column, self.variables))[0]

    def __generate_comparison_constraints(self):
        for row in range(2 * self.rows - 1):
            for column in range(len(self.data[row])):
                if not self.data[row][column] == '>' and not self.data[row][column] == '<' and not self.data[row][column] == '-':
                    pass
                elif row % 2 == 0:
                    if self.data[row][column] == '>':
                        bigger = self.__find_variable_position(row, column - 1)
                        smaller = self.__find_variable_position(row, column + 1)
                        self.constraints.append(CompareConstraint(smaller, bigger))
                    elif self.data[row][column] == '<':
                        bigger = self.__find_variable_position(row, column + 1)
                        smaller = self.__find_variable_position(row, column - 1)
                        self.constraints.append(CompareConstraint(smaller, bigger))

                else:
                    if self.data[row][column] == '>':
                        bigger = self.__find_variable_position(row - 1, 2 * column)
                        smaller = self.__find_variable_position(row + 1, 2 * column)
                        self.constraints.append(CompareConstraint(smaller, bigger))
                    elif self.data[row][column] == '<':
                        bigger = self.__find_variable_position(row + 1, 2 * column)
                        smaller = self.__find_variable_position(row - 1, 2 * column)
                        self.constraints.append(CompareConstraint(smaller, bigger))

    def __generate_completeness_constraints(self):
        for y in range(self.rows):
            row_coords = []
            for x in range(self.columns):
                row_coords.append(self.__find_variable_position(2 * y, 2 * x))

            self.constraints.append(CompletenessConstraint(row_coords))

        for x in range(self.columns):
            column_coords = []
            for y in range(self.rows):
                column_coords.append(self.__find_variable_position(2 * y, 2 * x))

            self.constraints.append(CompletenessConstraint(column_coords))

    def __str__(self):
        return f'Futoshiki puzzle - rows: {self.rows} columns: {self.columns} data: {self.data}'
