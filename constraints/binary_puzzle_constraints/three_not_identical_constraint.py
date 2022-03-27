from typing import List, Dict


from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


class ThreeNotIdenticalConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variables: List[VariablePosition]):  # dostaje row z VariablePosition
        super().__init__(variables)

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        for i in range(len(self.variables) - 2):
            if self.variables[i] in assignment and self.variables[i + 1] in assignment and self.variables[i + 2] in assignment:
                if assignment[self.variables[i]] == assignment[self.variables[i + 1]] == assignment[self.variables[i + 2]]:
                    return False
        return True
