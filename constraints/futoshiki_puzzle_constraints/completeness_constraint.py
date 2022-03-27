from typing import Dict, Tuple, List


from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


class CompletenessConstraint(Constraint[VariablePosition, int]):
    def __init__(self, variables: List[VariablePosition]):
        super().__init__(variables)

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        assigned: list[int] = []
        for variable in self.variables:
            if variable in assignment:
                assigned.append(assignment[variable])

        return len(assigned) == len(set(assigned))
