from typing import Dict

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if values in given variables
class CompareConstraint(Constraint[VariablePosition, int]):
    def __init__(self, first_position: VariablePosition, second_position: VariablePosition, sign: str):
        super().__init__([first_position, second_position])
        if sign == '>':
            self.first_position = first_position
            self.second_position = second_position
        else:
            self.first_position = second_position
            self.second_position = first_position

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        if self.first_position in assignment and self.second_position in assignment:
            return assignment[self.first_position] < assignment[self.second_position]
        else:
            return True
