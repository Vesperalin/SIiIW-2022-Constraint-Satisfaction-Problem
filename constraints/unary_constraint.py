from typing import TypeVar, Dict, Callable


from constraints.constraint import Constraint


V = TypeVar('V')
D = TypeVar('D')


class UnaryConstraint(Constraint[V, D]):
    def __init__(self, value: V, unary_predicate: Callable[[D], bool]):
        super().__init__([value])
        self.value = value                         # value to obiekt klasy Position
        self.unary_predicate = unary_predicate     # sprawdza, czy to co podane na wejściu jest zgodne

    def is_satisfied(self, assignment: Dict[V, D]):
        if self.value not in assignment:
            return True

        return self.unary_predicate(assignment[self.value])
