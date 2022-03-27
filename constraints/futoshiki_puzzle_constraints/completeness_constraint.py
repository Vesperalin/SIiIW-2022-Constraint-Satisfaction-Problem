from typing import Dict

from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


# constraint that checks if values in given variables (in row / column) are unique
class CompletenessConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variables: list[VariablePosition]):
        super().__init__(variables)

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        assigned: list[int] = []
        for variable in self.variables:
            if variable in assignment:
                assigned.append(assignment[variable])

        return len(assigned) == len(set(assigned))
