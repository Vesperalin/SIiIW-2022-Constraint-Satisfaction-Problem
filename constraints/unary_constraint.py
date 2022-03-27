from typing import Dict, Callable

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if variable has constant value (determined by data input of puzzle)
class UnaryConstraint(Constraint[VariablePosition, int]):
    def __init__(self, value: VariablePosition, predicate: Callable[[int], bool]):
        super().__init__([value])
        # value - Position object
        self.position: VariablePosition = value
        # predicate - function that checks constant at position. predicate has a closure (from puzzle class)
        self.predicate: Callable[[int], bool] = predicate

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        if self.position not in assignment:
            return True
        else:
            return self.predicate(assignment[self.position])
