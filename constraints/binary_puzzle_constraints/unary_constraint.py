from typing import TypeVar, Dict, Callable


from constraints.constraint import Constraint
from puzzle.variable_position import VariablePosition


V = TypeVar('V')
D = TypeVar('D')


class UnaryConstraint(Constraint[VariablePosition, int]):
    def __init__(self, value: VariablePosition, predicate: Callable[[int], bool]):
        super().__init__([value])
        self.value = value                   # value to obiekt klasy Position w binary
        self.predicate = predicate           # sprawdza, czy to co podane na wejściu jest zgodne

    def satisfied(self, assignment: Dict[VariablePosition, int]):
        if self.value not in assignment:
            return True
        else:
            return self.predicate(assignment[self.value])  # dla binary sprawdza, czy funkcja predicate zgodna dla wartosci w pozycji
