from typing import TypeVar, Dict, Callable, Tuple


from constraints.constraint import Constraint


V = TypeVar('V')
D = TypeVar('D')


class UnaryConstraint(Constraint[Tuple[int, int], int]):
    def __init__(self, value: int, predicate: Callable[[int], bool]):
        super().__init__([value])
        self.value = value                   # value to obiekt klasy Position w binary
        self.predicate = predicate           # sprawdza, czy to co podane na wejściu jest zgodne

    def satisfied(self, assignment: Dict[Tuple[int, int], int]):
        if self.value not in assignment:
            return True
        else:
            return self.predicate(assignment[self.value])  # dla binary sprawdza, czy funkcja predicate zgodna dla wartosci w pozycji
