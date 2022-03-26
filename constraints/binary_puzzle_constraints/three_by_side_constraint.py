from typing import List, Dict


from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


class ThreeBySideConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variables: List[VariablePosition]):
        super().__init__(variables)

    def is_satisfied(self, assignment: Dict[VariablePosition, int]):
        for index in range(len(self.variables) - 2):
            if self.variables[index] not in assignment or self.variables[index + 1] not in assignment or self.variables[index + 2] not in assignment:
                continue
            if assignment[self.variables[index]] == assignment[self.variables[index + 1]] == assignment[self.variables[index + 2]]:
                return False
        return True
