from typing import Dict, Callable

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if variable has constant value (determined by data input of puzzle)
class UnaryConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variable: VariablePosition, value: int):
        super().__init__([variable])
        # value - Position object
        self.variable: VariablePosition = variable
        self.value: int = value

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        if self.variable not in assignment:
            return True
        else:
            return assignment[self.variable] == self.value
