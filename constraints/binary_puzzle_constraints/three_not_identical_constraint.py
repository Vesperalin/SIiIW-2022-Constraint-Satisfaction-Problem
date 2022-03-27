from typing import Dict

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if 3 (adjacent) given variables are not the same (3x0 or 3x1)
class ThreeNotIdenticalConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variables: list[VariablePosition]):
        super().__init__(variables)

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        for i in range(len(self.variables) - 2):
            if self.variables[i] in assignment and self.variables[i + 1] in assignment \
                    and self.variables[i + 2] in assignment:
                if assignment[self.variables[i]] == assignment[self.variables[i + 1]] \
                        and assignment[self.variables[i + 1]] == assignment[self.variables[i + 2]]:
                    return False
        return True
