from typing import Dict, Tuple


from constraints.constraint import Constraint


class CompareConstraint(Constraint[Tuple[int, int], int]):
    def __init__(self, smaller, bigger):
        super().__init__([smaller, bigger])
        self.smaller = smaller  # (row_number, column_number) chyba
        self.bigger = bigger  # (row_number, column_number)

    def satisfied(self, assignment: Dict[Tuple[int, int], int]):
        if self.smaller not in assignment or self.bigger not in assignment:
            return True
        return assignment[self.smaller] < assignment[self.bigger]
