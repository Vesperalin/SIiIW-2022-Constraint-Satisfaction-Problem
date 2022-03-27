from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Dict, List

from constraints.constraint import Constraint

V = TypeVar('V')


# common abstract class for Puzzle classes
class Puzzle(Generic[V], ABC):
    def __init__(self):
        self.variables: List[V] = []
        self.domains: Dict[V, list[int]] = {}
        self.constraints: List[Constraint] = []
        self.size: int = 0
        self.data = []

    @abstractmethod
    def __str__(self):
        ...
