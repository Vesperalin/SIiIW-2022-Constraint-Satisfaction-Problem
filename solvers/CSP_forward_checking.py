from typing import Generic, TypeVar, Dict
from copy import deepcopy

from constraints.constraint import Constraint
from puzzle.puzzle import Puzzle


V = TypeVar('V')
D = TypeVar('D')


# V will be VariableConstraint and D int
# class represents CSP solver with backtracking
class CSPForwardCheckingSolver(Generic[V, D]):
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.variables: list[V] = puzzle.variables  # variables to be constrained
        self.domains: Dict[V, list[D]] = puzzle.domains  # domain of each variable
        self.constraints: Dict[V, list[Constraint[V, D]]] = {}  # dictionary for list of constraints for all variables
        self.results: list[Dict[V, D]] = []
        self.nodes: int = 0

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise ValueError("Every variable should have a domain assigned to it")

        for constraint in puzzle.constraints:
            self.__add_constraint(constraint)

    # goes through all the variables touched by a given constraint and adds itself to the constraints mapping
    # for each of them.
    # propagates group constraints on all variables that is constraints
    def __add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise ValueError("Variable in constraint not in CSP")
            self.constraints[variable].append(constraint)

    # checks every constraint for a given variable against an assignment to see if the variable’s value in the
    # assignment works for the constraints
    # assignment in my implementation: {key: VariablePosition, value: int (value at the position)}
    def consistent(self, variable: V, assignment: Dict[V, D]):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def if_consistent_for_two_variables(self, assignment: Dict[V, D], constraints: list[Constraint[V, D]]):
        for constraint in constraints:
            if not constraint.satisfied(assignment):
                return False
        return True

    # legti działający
    """def forward_checking_search(self, assignment: Dict[V, D]):
        # if every variable has assigned value
        if len(assignment) == len(self.variables):
            print(len(self.results))
            self.results.append(assignment)
            return

        unassigned: list[V] = []

        # get all variables that are not assigned a value
        for v in self.variables:
            if v not in assignment:
                unassigned.append(v)

        first: V = unassigned[0]
        domain = self.domains[first]

        for value_from_domain in domain:
            self.nodes += 1

            temp_assignment = assignment.copy()
            temp_assignment[first] = value_from_domain

            if self.consistent(first, temp_assignment):
                saved_domains: Dict[V, list[int]] = {}
                for key in self.domains.keys():
                    saved_domains[key] = deepcopy(self.domains[key])

                all_constraints = self.constraints[first]
                local_variables = set()

                # get all constraints where [first] VariablePosition included
                for const in all_constraints:
                    for var in const.variables:
                        if var != first:
                            local_variables.add(var)

                for var in local_variables:
                    # get constraints where [var] and [first] are together
                    constraints_to_check = []
                    for const in all_constraints:
                        if var in const.variables and first in const.variables:
                            constraints_to_check.append(const)

                    for value in saved_domains[var]:
                        local_copy_assignment = temp_assignment.copy()
                        local_copy_assignment[var] = value
                        if_satisfied_forward = self.if_consistent_for_two_variables(local_copy_assignment,
                                                                                    constraints_to_check)
                        if not if_satisfied_forward:  # domany wywalić??? z self.domains
                            self.domains[var].remove(value)

                    # jeżeli self.domains dla var pusta to powrót, a jak nie to wychodze z 2xfor
                    if len(self.domains[var]) == 0:
                        break

                # if żadna z domen niepusta to ten co w bcktrackingu rekursja
                if_domains_empty = False

                for key in self.domains.keys():
                    if len(self.domains[key]) == 0:
                        if_domains_empty = True

                self.domains = saved_domains

                if not if_domains_empty:
                    # self.domains = saved_domains
                    self.forward_checking_search(temp_assignment)"""

    def forward_checking_search(self, assignment: Dict[V, D]):
        # if every variable has assigned value
        if len(assignment) == len(self.variables):
            print(len(self.results))
            self.results.append(assignment)
            return

        unassigned: list[V] = []

        # get all variables that are not assigned a value
        for v in self.variables:
            if v not in assignment:
                unassigned.append(v)

        first: V = unassigned[0]
        domain = self.domains[first]

        for value_from_domain in domain:
            self.nodes += 1
            temp_assignment = assignment.copy()
            temp_assignment[first] = value_from_domain

            if self.consistent(first, temp_assignment):
                saved_domains: Dict[V, list[int]] = {}
                for key in self.domains.keys():
                    saved_domains[key] = deepcopy(self.domains[key])

                all_constraints = self.constraints[first]
                local_variables = set()

                # get all EMPTY variables where [first] VariablePosition included in same constraints
                for const in all_constraints:
                    for var in const.variables:
                        if var != first and var not in temp_assignment:
                            local_variables.add(var)

                for var in local_variables:
                    # get constraints where [var] and [first] are together
                    constraints_to_check = []
                    for const in all_constraints:
                        if var in const.variables and first in const.variables:
                            constraints_to_check.append(const)

                    for value in saved_domains[var]:
                        local_copy_assignment = temp_assignment.copy()
                        local_copy_assignment[var] = value
                        if_satisfied_forward = self.if_consistent_for_two_variables(local_copy_assignment,
                                                                                    constraints_to_check)
                        if not if_satisfied_forward:
                            self.domains[var].remove(value)

                    # jeżeli self.domains dla var pusta to powrót, a jak nie to wychodze z 2xfor
                    if len(self.domains[var]) == 0:
                        break

                # if żadna z domen niepusta to ten co w bcktrackingu rekursja
                if_domains_empty = False

                for key in self.domains.keys():
                    if len(self.domains[key]) == 0:
                        if_domains_empty = True

                self.domains = saved_domains

                if not if_domains_empty:
                    # self.domains = saved_domains
                    self.forward_checking_search(temp_assignment)
