from typing import Generic, TypeVar, Dict, List

from constraints.constraint import Constraint

V = TypeVar('V')
D = TypeVar('D')


class CSPSolver(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]):
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}  # constraints for all variables (for all positions)
        self.solutions = []

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise ValueError("Each variable should have a domain assigned to it")

    def add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise ValueError("Such variable does not exist in domain")
            self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]):
        for constraint in self.constraints[variable]:
            if not constraint.is_satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D]):
        if len(assignment) == len(self.variables):  # przypisano każdej zmiennej wartosc
            self.solutions.append(assignment)
            return

        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        to_be_assigned: V = unassigned[0]
        for value in self.domains[to_be_assigned]:
            local_assignment = assignment.copy()
            local_assignment[to_be_assigned] = value
            if self.consistent(to_be_assigned, local_assignment):
                self.backtracking_search(local_assignment)
