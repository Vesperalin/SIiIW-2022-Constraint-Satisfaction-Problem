from puzzle.variable_position import VariablePosition
from constraints.unary_constraint import UnaryConstraint
from constraints.binary_puzzle_constraints.three_by_side_constraint import ThreeBySideConstraint
from constraints.binary_puzzle_constraints.unique_cols_and_rows_constraint import UniqueColsAndRowsConstraint
from constraints.binary_puzzle_constraints.same_amount_zeros_as_ones import SameAmountZerosAsOnes


class BinaryPuzzle:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = data.replace('\n', '')
        self.variables = [VariablePosition(row, column) for row in range(0, self.rows) for column in range(0, self.columns)]  # lista z obiektami klasy Position
        self.domains = {position: [0, 1] for position in self.variables}  # słownik, gdzie kluczem jest position, a wartościami dziedzina zaminnej
        self.constraints = []
        self.__generate_unary_constraints()
        self.__generate_three_by_side_row_constraint()
        self.__generate_three_by_side_column_constraint()
        self.__generate_same_amount_zeros_as_ones_row_constraint()
        self.__generate_same_amount_zeros_as_ones_column_constraint()
        self.__generate_unique_cols_and_rows_constraint()

    def __generate_unary_constraints(self):
        for i in range(len(self.data)):
            if self.data[i] != 'x':
                self.constraints.append(UnaryConstraint(self.variables[i], lambda assignment, v=int(self.data[i]): assignment == v))
                    # obiekt klasy Position dla odpowiedniej liczby, która ma być zapisana [0 lub  1],
                    # lambda z parametrem assignment, sprawdza, czy podana liczba spełnia predykat

    def __generate_three_by_side_row_constraint(self):
        for row in range(self.rows):
            self.constraints.append(ThreeBySideConstraint(self.variables[row * self.columns: (row + 1) * self.columns]))

    def __generate_three_by_side_column_constraint(self):
        for i in range(self.columns):
            column = [variable for variable in self.variables if variable.column_number == i]
            self.constraints.append(ThreeBySideConstraint(column))

    def __generate_same_amount_zeros_as_ones_row_constraint(self):
        for row in range(self.rows):
            self.constraints.append(SameAmountZerosAsOnes(self.variables[row * self.columns: (row + 1) * self.columns]))

    def __generate_same_amount_zeros_as_ones_column_constraint(self):
        for i in range(self.columns):
            column = [variable for variable in self.variables if variable.column_number == i]
            self.constraints.append(SameAmountZerosAsOnes(column))

    def __generate_unique_cols_and_rows_constraint(self):
        self.constraints.append(UniqueColsAndRowsConstraint(self.variables, self.rows))

    def __str__(self):
        return f'rows: {self.rows} cols: {self.columns} data: {len(self.data)} domains: {self.domains}'
