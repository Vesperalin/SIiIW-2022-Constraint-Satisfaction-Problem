from typing import Dict

from constraints.unary_constraint import UnaryConstraint
from constraints.futoshiki_puzzle_constraints.compare_constraint import CompareConstraint
from constraints.futoshiki_puzzle_constraints.completeness_constraint import CompletenessConstraint
from puzzle.variable_position import VariablePosition
from puzzle.puzzle import Puzzle
from constraints.constraint import Constraint


# class represents futoshiki puzzle
class Futoshiki_Puzzle(Puzzle):
    def __init__(self, size: int, data: str):
        super().__init__()
        # override values from parent
        self.size: int = size
        self.data: list[str] = (data + '-').split('\n')
        self.variables: list[VariablePosition] = []
        self.domains: Dict[VariablePosition, list[int]] = {}
        self.constraints: list[Constraint[VariablePosition, list[Constraint]]] = []
        # defining fields content
        self.__transform_data()
        # generate constraints
        self.__generate_comparison_constraints()
        self.__generate_completeness_constraints()

    # transforms data from input and fills self.variables list
    def __transform_data(self):
        for y in list(filter(lambda e: e % 2 != 1, list(range(0, 2 * self.size - 1)))):
            for x in range(len(self.data[y])):
                if not self.data[y][x] == '>' and not self.data[y][x] == '<' and not self.data[y][x] == '-':
                    variable = VariablePosition(y, x)
                    self.variables.append(variable)
                    self.domains[variable] = list(range(1, self.size + 1))
                    if self.data[y][x] != 'x':
                        self.constraints.append(UnaryConstraint(variable,
                                                                lambda assignment,
                                                                v=int(self.data[y][x]): assignment == v))

    # helpers - finds VariablePosition object by coordinates
    def __find_variable_position(self, y, x):
        return list(filter(lambda var_position: var_position.row_number == y and var_position.column_number == x,
                           self.variables))[0]

    # create comparison constraints based on data (self.data) and add to self.constraints
    def __generate_comparison_constraints(self):
        for y in range(2 * self.size - 1):
            for x in range(len(self.data[y])):
                if not self.data[y][x] == '>' and not self.data[y][x] == '<' and not self.data[y][x] == '-':
                    pass
                elif y % 2 == 0:
                    if self.data[y][x] == '>':
                        greater_position = self.__find_variable_position(y, x - 1)
                        smaller_position = self.__find_variable_position(y, x + 1)
                        self.constraints.append(CompareConstraint(smaller_position, greater_position))
                    elif self.data[y][x] == '<':
                        greater_position = self.__find_variable_position(y, x + 1)
                        smaller_position = self.__find_variable_position(y, x - 1)
                        self.constraints.append(CompareConstraint(smaller_position, greater_position))
                else:
                    if self.data[y][x] == '>':
                        greater_position = self.__find_variable_position(y - 1, 2 * x)
                        smaller_position = self.__find_variable_position(y + 1, 2 * x)
                        self.constraints.append(CompareConstraint(smaller_position, greater_position))
                    elif self.data[y][x] == '<':
                        greater_position = self.__find_variable_position(y + 1, 2 * x)
                        smaller_position = self.__find_variable_position(y - 1, 2 * x)
                        self.constraints.append(CompareConstraint(smaller_position, greater_position))

    # create completeness constraints and add to self.constraints
    def __generate_completeness_constraints(self):
        for y in range(self.size):
            row_coords = []
            for x in range(self.size):
                row_coords.append(self.__find_variable_position(2 * y, 2 * x))

            self.constraints.append(CompletenessConstraint(row_coords))

        for x in range(self.size):
            column_coords = []
            for y in range(self.size):
                column_coords.append(self.__find_variable_position(2 * y, 2 * x))

            self.constraints.append(CompletenessConstraint(column_coords))

    def __str__(self):
        return f'Futoshiki puzzle - size: {self.size} data: {self.data}'
