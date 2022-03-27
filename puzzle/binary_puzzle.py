from puzzle.variable_position import VariablePosition
from constraints.binary_puzzle_constraints.unary_constraint import UnaryConstraint
from constraints.binary_puzzle_constraints.three_not_identical_constraint import ThreeNotIdenticalConstraint
from constraints.binary_puzzle_constraints.unique_cols_and_rows_constraint import UniqueColsAndRowsConstraint
from constraints.binary_puzzle_constraints.same_amount_zeros_as_ones import SameAmountZerosAsOnes


class BinaryPuzzle:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = data.replace('\n', '')
        self.variables = []  # lista z obiektami klasy Position
        self.domains = {}  # słownik, gdzie kluczem jest position, a wartościami dziedzina zaminnej
        self.constraints = []
        # defining fields content
        self.__create_variables()
        self.__create_domains_for_variables()
        self.__generate_unary_constraints()
        self.__generate_three_not_identical_constraints()
        self.__generate_same_amount_zeros_as_ones_constraint()
        self.__generate_unique_cols_and_rows_constraint()

    def __create_variables(self):
        for y in range(0, self.rows):
            for x in range(0, self.columns):
                self.variables.append(VariablePosition(y, x))

    def __create_domains_for_variables(self):
        for position in self.variables:
            self.domains[position] = [0, 1]

    def __generate_unary_constraints(self):
        for i in range(len(self.data)):
            if self.data[i] != 'x':
                self.constraints.append(UnaryConstraint(self.variables[i], lambda assignment, value=int(self.data[i]): assignment == value))
                    # obiekt klasy Position dla odpowiedniej liczby, która ma być zapisana [0 lub  1],
                    # lambda z parametrem assignment, sprawdza, czy podana liczba spełnia predykat

    def __generate_three_not_identical_constraints(self):
        for y in range(self.rows):
            self.constraints.append(ThreeNotIdenticalConstraint(self.variables[y * self.columns: (y + 1) * self.columns]))

        for i in range(self.columns):
            column = []
            for variable in self.variables:
                if variable.column_number == i:
                    column.append(variable)

            self.constraints.append(ThreeNotIdenticalConstraint(column))

    def __generate_same_amount_zeros_as_ones_constraint(self):
        for y in range(self.rows):
            self.constraints.append(SameAmountZerosAsOnes(self.variables[y * self.columns: (y + 1) * self.columns]))

        for i in range(self.columns):
            column = []
            for variable in self.variables:
                if variable.column_number == i:
                    column.append(variable)
            self.constraints.append(SameAmountZerosAsOnes(column))

    def __generate_unique_cols_and_rows_constraint(self):
        self.constraints.append(UniqueColsAndRowsConstraint(self.variables, self.rows))

    def __str__(self):
        return f'Binary puzzle - rows: {self.rows} cols: {self.columns} data: {len(self.data)} domains: {self.domains}'
