from typing import Generic, TypeVar, Dict, List
from abc import ABC, abstractmethod

V = TypeVar('V')
D = TypeVar('D')


# Each Constraint consists of the variables (list) it constrains
# and a method (satisfied()) that checks whether it is satisfied
class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]):
        # assignment is a dict: key, value: assigned value from variable domain
        pass
