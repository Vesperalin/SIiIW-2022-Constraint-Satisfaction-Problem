from typing import List, Dict


from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


class SameAmountZerosAsOnes(Constraint[VariablePosition, int]):
    def __init__(self, variables: List[VariablePosition]):
        super().__init__(variables)
        self.half_length = len(variables) / 2  # tu wczesniej bylo //

    def is_satisfied(self, assignment: Dict[VariablePosition, int]):
        zeros_amount = 0
        ones_amount = 0

        for variable in self.variables:
            if variable in assignment and assignment[variable] == 0:
                zeros_amount += 1
            elif variable in assignment and assignment[variable] == 1:
                ones_amount += 1

        return zeros_amount <= self.half_length and ones_amount <= self.half_length
