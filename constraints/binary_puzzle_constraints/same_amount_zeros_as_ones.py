from typing import Dict

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if same amount of 0 as 1 in full row / column (in list of variables)
class SameAmountZerosAsOnes(Constraint[VariablePosition, int]):
    def __init__(self, variables: list[VariablePosition]):
        super().__init__(variables)

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        zeros_amount = 0
        ones_amount = 0

        for variable in self.variables:
            if variable in assignment and assignment[variable] == 0:
                zeros_amount += 1
            elif variable in assignment and assignment[variable] == 1:
                ones_amount += 1

        return zeros_amount <= (len(self.variables) / 2) and ones_amount <= (len(self.variables) / 2)
