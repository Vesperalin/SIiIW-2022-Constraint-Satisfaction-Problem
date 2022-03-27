from typing import Dict, Tuple


from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


class CompareConstraint(Constraint[VariablePosition, int]):
    def __init__(self, smaller, bigger):
        super().__init__([smaller, bigger])
        self.smaller = smaller                              # VariablePosition
        self.bigger = bigger                                # VariablePosition

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        if self.smaller in assignment and self.bigger in assignment:
            return assignment[self.smaller] < assignment[self.bigger]
        else:
            return True
