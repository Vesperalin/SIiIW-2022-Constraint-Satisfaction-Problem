from typing import Dict, Tuple, List


from constraints.constraint import Constraint


class CompletenessConstraint(Constraint[Tuple[int, int], int]):
    def __init__(self, variables: List[Tuple[int, int]]):
        super().__init__(variables)

    def is_satisfied(self, assignment: Dict[Tuple[int, int], int]):
        assigned = []
        for variable in self.variables:
            if variable in assignment:
                assigned.append(assignment[variable])

        return len(assigned) == len(set(assigned))
