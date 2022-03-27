from typing import Generic, TypeVar, Dict, List
from abc import ABC, abstractmethod


V = TypeVar('V')
D = TypeVar('D')


# Each Constraint consists of the variables it constrains and a method that checks whether it is satisfied()
class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]):
        pass
