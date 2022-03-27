from typing import Generic, TypeVar, Dict, List


from constraints.constraint import Constraint


V = TypeVar('V')
D = TypeVar('D')


# dla Binary V to VariablePosition, D to int
class CSPSolver(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]):
        self.variables: List[V] = variables  # variables to be constrained
        self.domains: Dict[V, List[D]] = domains  # domain of each variable
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}  # dictionary for list of constraints for all variables
        self.solutions = []

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise ValueError("Each variable should have a domain assigned to it")

    # goes through all of the variables touched by a given constraint and adds itself to the constraints mapping for each of them.
    def add_constraint(self, constraint: Constraint[V, D]):  # ona propaguje ograniczenia grupowe na wszystkie zmienne, których ono dotyczy
        for variable in constraint.variables:
            if variable not in self.variables:
                raise ValueError("Such variable does not exist in domain")
            self.constraints[variable].append(constraint)

    # checks every constraint for a given variable against an assignment to see if the variable’s value in the assignment works for the constraints
    def consistent(self, variable: V, assignment: Dict[V, D]):  # assignment to w binary słownik {VariablePosition, przypisana wartosc}
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}):
        if len(assignment) == len(self.variables):  # przypisano każdej zmiennej wartosc
            self.solutions.append(assignment)
            return

        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        to_be_assigned: V = unassigned[0]
        for value in self.domains[to_be_assigned]:
            local_assignment = assignment.copy()
            local_assignment[to_be_assigned] = value
            if self.consistent(to_be_assigned, local_assignment):
                # print(local_assignment)
                self.backtracking_search(local_assignment)
