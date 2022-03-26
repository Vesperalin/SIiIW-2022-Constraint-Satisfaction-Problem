from typing import Generic, TypeVar, Dict, List
from abc import ABC, abstractmethod


V = TypeVar('V')
D = TypeVar('D')


class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]):
        self.variables = variables

    @abstractmethod
    def is_satisfied(self, assignment: Dict[V, D]):
        pass
