from typing import Generic, TypeVar, Dict
from copy import deepcopy

from constraints.constraint import Constraint
from constraints.unary_constraint import UnaryConstraint
from puzzle.puzzle import Puzzle


V = TypeVar('V')
D = TypeVar('D')


# V will be VariableConstraint and D int
# class represents CSP solver with backtracking, forward checking ....................
class CSPSolver(Generic[V, D]):
    def __init__(self, puzzle: Puzzle, solving_mode: str):
        self.puzzle = puzzle
        self.variables: list[V] = puzzle.variables  # variables to be constrained
        self.domains: Dict[V, list[D]] = puzzle.domains  # domain of each variable
        self.constraints: Dict[V, list[Constraint[V, D]]] = {}  # dictionary for list of constraints for all variables
        self.results: list[Dict[V, D]] = []
        self.nodes: int = 0
        self.solving_mode: str = solving_mode  # BT, FC
        self.unary_constraints: list[V] = []

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise ValueError("Every variable should have a domain assigned to it")

        for constraint in puzzle.constraints:
            self.__add_constraint(constraint)
            if self.solving_mode == 'FC':
                if type(constraint) is UnaryConstraint:
                    self.unary_constraints.append(constraint)

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

    # checks only given constraints for given assignment
    @staticmethod
    def if_consistent_for_two_variables(assignment: Dict[V, D], constraints: list[Constraint[V, D]]):
        for constraint in constraints:
            if not constraint.satisfied(assignment):
                return False
        return True

    # main method - to solver puzzle
    def solve(self):
        if self.solving_mode == 'BT':
            self.__backtracking_search({})
        elif self.solving_mode == 'FC':
            self.__forward_checking()

    # backtracking solver
    def __backtracking_search(self, assignment: Dict[V, D]):
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
        for value_from_domain in self.domains[first]:
            self.nodes += 1
            temp_assignment = assignment.copy()
            temp_assignment[first] = value_from_domain
            if self.consistent(first, temp_assignment):
                self.__backtracking_search(temp_assignment)

    # forward checking solver
    def __forward_checking(self):
        assignment: Dict[V, D] = {}
        for constraint in self.puzzle.constraints:
            # assign unary constraints
            if type(constraint) is UnaryConstraint:
                assignment[constraint.variables[0]] = constraint.value

        self.__forward_checking_search(assignment)

    # forward checking solver helper
    def __forward_checking_search(self, assignment: Dict[V, D]):
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
                all_constraints = self.constraints[first]
                local_variables = []

                # get all EMPTY variables where [first] VariablePosition included in same constraints as var
                for const in all_constraints:
                    for var in const.variables:
                        if var != first and var not in temp_assignment and var not in local_variables:
                            local_variables.append(var)

                saved_domains: Dict[V, list[int]] = {}
                for key in local_variables:
                    saved_domains[key] = deepcopy(self.domains[key])

                # flag for turn back
                if_domains_empty = False

                for var in local_variables:
                    # get constraints where [var] and [first] are together
                    constraints_to_check = []
                    for const in all_constraints:
                        if var in const.variables and first in const.variables:
                            constraints_to_check.append(const)

                    # add unary constraints
                    constraints_to_check.extend(self.unary_constraints)

                    # check values from domain
                    for value in saved_domains[var]:
                        local_copy_assignment = temp_assignment.copy()
                        local_copy_assignment[var] = value
                        if_satisfied_forward = self.if_consistent_for_two_variables(local_copy_assignment,
                                                                                    constraints_to_check)
                        if not if_satisfied_forward:
                            self.domains[var].remove(value)

                    # if domain empty - start to turn back
                    if len(self.domains[var]) == 0:
                        if_domains_empty = True
                        break

                if not if_domains_empty:
                    self.__forward_checking_search(temp_assignment)

                # restore domains
                for key in local_variables:
                    self.domains[key] = saved_domains[key]
