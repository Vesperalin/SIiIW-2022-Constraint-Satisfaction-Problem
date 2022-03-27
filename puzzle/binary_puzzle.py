from typing import Dict

from puzzle.variable_position import VariablePosition
from constraints.unary_constraint import UnaryConstraint
from constraints.binary_puzzle_constraints.three_not_identical_constraint import ThreeNotIdenticalConstraint
from constraints.binary_puzzle_constraints.unique_constraint import UniqueConstraint
from constraints.binary_puzzle_constraints.same_amount_zeros_as_ones import SameAmountZerosAsOnes
from puzzle.puzzle import Puzzle
from constraints.constraint import Constraint


# class represents binary puzzle
class BinaryPuzzle(Puzzle):
    def __init__(self, size: int, data: str):
        super().__init__()
        # override values from parent
        self.variables: list[VariablePosition] = []
        self.domains: Dict[VariablePosition, list[int]] = {}
        self.constraints: list[Constraint] = []
        self.size: int = size
        self.data: str = data.replace('\n', '')
        # defining fields content
        self.__create_variables()
        self.__create_domains_for_variables()
        # generate constraints
        self.__generate_unary_constraints()
        self.__generate_three_not_identical_constraints()
        self.__generate_same_amount_zeros_as_ones_constraint()
        self.__generate_unique_cols_and_rows_constraint()

    # fill self.variables list
    def __create_variables(self):
        for y in range(0, self.size):
            for x in range(0, self.size):
                self.variables.append(VariablePosition(y, x))

    # fill self.domains list
    def __create_domains_for_variables(self):
        for position in self.variables:
            self.domains[position] = [0, 1]

    # creates constraints that check if columns are unique and rows are unique and add to self.constraints
    def __generate_unique_cols_and_rows_constraint(self):
        self.constraints.append(UniqueConstraint(self.variables, self.size))

    # create unary constraints based on given data (self.data) and add to self.constraints
    def __generate_unary_constraints(self):
        for i in range(len(self.data)):
            if self.data[i] != 'x':
                self.constraints.append(UnaryConstraint(self.variables[i],
                                                        lambda assignment,
                                                        value=int(self.data[i]): assignment == value))

    # creates constraints that check if amounts of 0 and 1 are equal (in fully filled rows / columns)
    # and add to self.constraints
    def __generate_same_amount_zeros_as_ones_constraint(self):
        for y in range(self.size):
            low_index = y * self.size
            high_index = (y + 1) * self.size
            self.constraints.append(SameAmountZerosAsOnes(self.variables[low_index: high_index]))

        for i in range(self.size):
            column: list[VariablePosition] = []
            for variable in self.variables:
                if variable.column_number == i:
                    column.append(variable)
            self.constraints.append(SameAmountZerosAsOnes(column))

    # create constraints that check if no 3x1 or 3x0 side by side (in rows and columns) and add to self.constraints
    def __generate_three_not_identical_constraints(self):
        for y in range(self.size):
            low_index = y * self.size
            high_index = (y + 1) * self.size
            self.constraints.append(ThreeNotIdenticalConstraint(self.variables[low_index: high_index]))

        for i in range(self.size):
            column: list[VariablePosition] = []
            for variable in self.variables:
                if variable.column_number == i:
                    column.append(variable)

            self.constraints.append(ThreeNotIdenticalConstraint(column))

    def __str__(self):
        return f'Binary puzzle - size: {self.size} data: {len(self.data)} domains: {self.domains}'
