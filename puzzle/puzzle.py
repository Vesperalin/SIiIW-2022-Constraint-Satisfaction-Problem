from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Dict, List

from constraints.constraint import Constraint

V = TypeVar('V')
D = TypeVar('D')


# common abstract class for Puzzle classes
class Puzzle(Generic[V, D], ABC):
    def __init__(self):
        self.size: int = 0
        self.data = []
        self.variables: List[V] = []
        self.domains: Dict[V, list[int]] = {}
        self.constraints: List[Constraint[V, D]] = []

    @abstractmethod
    def __str__(self):
        ...
