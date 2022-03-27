from typing import Dict

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if values in given variables
class CompareConstraint(Constraint[VariablePosition, int]):
    def __init__(self, smaller_position: VariablePosition, greater_position: VariablePosition):
        super().__init__([smaller_position, greater_position])
        self.smaller_position = smaller_position
        self.greater_position = greater_position

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        if self.smaller_position in assignment and self.greater_position in assignment:
            return assignment[self.smaller_position] < assignment[self.greater_position]
        else:
            return True
