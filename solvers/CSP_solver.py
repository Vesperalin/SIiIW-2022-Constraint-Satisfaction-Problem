from typing import Generic, TypeVar, Dict
from copy import deepcopy
import time

from constraints.constraint import Constraint
from constraints.unary_constraint import UnaryConstraint
from puzzle.puzzle import Puzzle

V = TypeVar('V')
D = TypeVar('D')


# V will be VariableConstraint and D int
# class represents CSP solver with backtracking, forward checking, look ahead
class CSPSolver(Generic[V, D]):
    def __init__(self, puzzle: Puzzle, solving_mode: str, variable_heuristic: str, value_heuristic: str):
        self.puzzle = puzzle
        self.variables: list[V] = puzzle.variables  # variables to be constrained
        self.domains: Dict[V, list[D]] = puzzle.domains  # domain of each variable
        self.constraints: Dict[V, list[Constraint[V, D]]] = {}  # dictionary for list of constraints for all variables
        self.results: list[Dict[V, D]] = []
        self.nodes: int = 0
        self.solving_mode: str = solving_mode  # BT (backtracking), FC (forward checking), FC_C (forward checking with constraint propagation)
        self.variable_heuristic: str = variable_heuristic  # CON (consecutive), MRV (Minimum Remaining Values)
        self.values_heuristic: str = value_heuristic  # CON (consecutive), LCV (Least Constraining Value)
        self.unary_constraints: list[V] = []
        self.time = 0

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise ValueError("Every variable should have a domain assigned to it")

        for constraint in puzzle.constraints:
            self.__add_constraint(constraint)
            if self.solving_mode == 'FC' or self.solving_mode == 'FC_C':
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
        start_time = time.time()
        initial_assignment = self.__extract_unary_constraints()
        if self.solving_mode == 'BT':
            self.__backtracking_search(initial_assignment)
        elif self.solving_mode == 'FC':
            self.__forward_checking_search(initial_assignment)
        elif self.solving_mode == 'FC_C':
            self.__forward_checking_with_constraint_propagation_search(initial_assignment)
        self.time = time.time() - start_time

    # ************************************ variable heuristics ************************************
    def __get_variables_by_heuristic(self, assignment: Dict[V, D]):
        if self.variable_heuristic == 'CON':
            return self.__get_consecutive_variable_heuristic(assignment)
        elif self.variable_heuristic == 'MRV':
            return self.__get_mrv_variable_heuristic(assignment)

    # get all variables that are not assigned a value - consecutive not empty variables
    def __get_consecutive_variable_heuristic(self, assignment: Dict[V, D]):
        unassigned: list[V] = []
        for v in self.variables:
            if v not in assignment:
                unassigned.append(v)
        return unassigned

    # get all variables that are not assigned a value - Minimum Remaining Values heuristic
    def __get_mrv_variable_heuristic(self, assignment: Dict[V, D]):
        unassigned: list[V] = []
        for v in self.variables:
            if v not in assignment:
                unassigned.append(v)

        unassigned = sorted(unassigned, key=lambda x: len(self.domains[x]))
        return unassigned

    # ************************************ value heuristics ************************************
    def __get_values_by_heuristic(self, unassigned: V, assignment: Dict[V, D]):
        if self.values_heuristic == 'CON':
            return self.__get_consecutive_value_heuristic(unassigned)
        elif self.values_heuristic == 'LCV':
            return self.__get_lcv_value_heuristic(unassigned, assignment)

    # get all values consecutively from domain - consecutive not empty variables
    def __get_consecutive_value_heuristic(self, unassigned: V):
        return self.domains[unassigned]

    # get all values from domain by least constraining value
    def __get_lcv_value_heuristic(self, unassigned: V, assignment: Dict[V, D]):
        ranking: Dict[int, int] = {}
        all_constraints = self.constraints[unassigned]
        local_variables = []

        for value_from_domain in self.domains[unassigned]:
            temp_assignment = assignment.copy()
            temp_assignment[unassigned] = value_from_domain

            if self.consistent(unassigned, temp_assignment):
                for d in self.domains[unassigned]:
                    ranking[d] = 0

                # get all EMPTY variables where [first] VariablePosition included in same constraints as var
                for const in all_constraints:
                    for var in const.variables:
                        if var != unassigned and var not in assignment and var not in local_variables:
                            local_variables.append(var)

                for var in local_variables:
                    # get constraints where [var] and [first] are together
                    constraints_to_check = []
                    for const in all_constraints:
                        if var in const.variables and unassigned in const.variables:
                            constraints_to_check.append(const)

                    # add unary constraints
                    constraints_to_check.extend(self.unary_constraints)

                    # check values from domain
                    for value in self.domains[var]:
                        local_copy_assignment = temp_assignment.copy()
                        local_copy_assignment[var] = value
                        if_satisfied_forward = self.if_consistent_for_two_variables(local_copy_assignment,
                                                                                    constraints_to_check)
                        if not if_satisfied_forward:
                            ranking[value_from_domain] = ranking[value_from_domain] + 1

        results = [(k, v) for k, v in ranking.items()]
        results = sorted(results, key=lambda x: x[1])
        values = []
        for r in results:
            values.append(r[0])

        return values

    # ************************************ unary constraint helper ************************************
    def __extract_unary_constraints(self):
        assignment: Dict[V, D] = {}
        for constraint in self.puzzle.constraints:
            # assign unary constraints
            if type(constraint) is UnaryConstraint:
                assignment[constraint.variables[0]] = constraint.value
        return assignment

    # ************************************ backtracking ************************************
    def __backtracking_search(self, assignment: Dict[V, D]):
        # if every variable has assigned value
        if len(assignment) == len(self.variables):
            self.results.append(assignment)
            return

        unassigned: list[V] = self.__get_variables_by_heuristic(assignment)
        first = unassigned[0]
        domain_of_unassigned: list[int] = self.__get_values_by_heuristic(first, assignment)
        for value_from_domain in domain_of_unassigned:
            self.nodes += 1
            temp_assignment = assignment.copy()
            temp_assignment[first] = value_from_domain
            if self.consistent(first, temp_assignment):
                self.__backtracking_search(temp_assignment)

    # ************************************ forward checking ************************************
    def __forward_checking_search(self, assignment: Dict[V, D]):
        # if every variable has assigned value
        if len(assignment) == len(self.variables):
            self.results.append(assignment)
            return

        unassigned: list[V] = self.__get_variables_by_heuristic(assignment)
        first: V = unassigned[0]
        domain_of_unassigned: list[int] = self.__get_values_by_heuristic(first, assignment)
        for value_from_domain in domain_of_unassigned:
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

    # ********************************* forward checking with constraints propagation *********************************
    def __forward_checking_with_constraint_propagation_search(self, assignment: Dict[V, D]):
        # if every variable has assigned value
        if len(assignment) == len(self.variables):
            print(len(self.results))
            self.results.append(assignment)
            return

        unassigned: list[V] = self.__get_variables_by_heuristic(assignment)
        first: V = unassigned[0]
        domain_of_unassigned: list[int] = self.__get_values_by_heuristic(first, assignment)

        for value_from_domain in domain_of_unassigned:
            self.nodes += 1
            temp_assignment = assignment.copy()
            temp_assignment[first] = value_from_domain

            if self.consistent(first, temp_assignment):
                # all constraints with [first]
                all_constraints = self.constraints[first]
                local_variables = []

                # get all EMPTY variables where [first] VariablePosition included in same constraints as var
                for const in all_constraints:
                    for var in const.variables:
                        if var != first and var not in temp_assignment and var not in local_variables:
                            local_variables.append(var)

                # save domains of local_variables
                saved_domains: Dict[V, list[int]] = {}
                for key in local_variables:
                    saved_domains[key] = deepcopy(self.domains[key])

                # flag for turn back
                if_domains_empty = False

                # check all variables if var have domain length 1 of [first] with value value_from_domain
                for var in local_variables:
                    # get constraints where [var] and [first] are together
                    if not if_domains_empty:
                        constraints_to_check = []
                        for const in all_constraints:
                            if var in const.variables and first in const.variables:
                                constraints_to_check.append(const)

                        # add unary constraints
                        constraints_to_check.extend(self.unary_constraints)

                        # check values from domain of [var]
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

                        # if domain length equal to 1, look deeper
                        if len(self.domains[var]) == 1:
                            local_copy_assignment = temp_assignment.copy()
                            local_copy_assignment[var] = self.domains[var][0]
                            # call helper to look deeper
                            response = self.__forward_checking_with_constraint_propagation_helper(local_copy_assignment, var)

                            """if response:
                                #temp_assignment[var] = self.domains[var][0]
                                # to wpisuję do siatki zmienną,
                                #pass
                                pass"""

                            # if error occurred - start to turn back
                            if not response:
                                if_domains_empty = True

                if not if_domains_empty:
                    self.__forward_checking_with_constraint_propagation_search(temp_assignment)

                # restore domains
                for key in local_variables:
                    self.domains[key] = saved_domains[key]

    def __forward_checking_with_constraint_propagation_helper(self, assignment: Dict[V, D], variable: V):
        # if every variable has assigned value
        if len(assignment) == len(self.variables):
            return True

        all_constraints = self.constraints[variable]
        local_variables = []

        # get all EMPTY variables where [variable] VariablePosition included in same constraints as var
        for const in all_constraints:
            for var in const.variables:
                if var != variable and var not in assignment and var not in local_variables:
                    local_variables.append(var)

        saved_domains: Dict[V, list[int]] = {}
        for key in local_variables:
            saved_domains[key] = deepcopy(self.domains[key])

        for var in local_variables:
            # get constraints where [var] and [first] are together
            constraints_to_check = []
            for const in all_constraints:
                if var in const.variables and variable in const.variables:
                    constraints_to_check.append(const)

            # add unary constraints
            constraints_to_check.extend(self.unary_constraints)

            # check values from domain
            for value in saved_domains[var]:
                local_copy_assignment = assignment.copy()
                local_copy_assignment[var] = value
                if_satisfied_forward = self.if_consistent_for_two_variables(local_copy_assignment,
                                                                            constraints_to_check)
                if not if_satisfied_forward:
                    self.domains[var].remove(value)

            # if domain empty - start to turn back
            if len(self.domains[var]) == 0:
                for key in local_variables:
                    self.domains[key] = saved_domains[key]
                return False

            if len(self.domains[var]) == 1:
                local_copy_assignment = assignment.copy()
                local_copy_assignment[var] = self.domains[var][0]
                response = self.__forward_checking_with_constraint_propagation_helper(local_copy_assignment, var)
                for key in local_variables:
                    self.domains[key] = saved_domains[key]
                return response

        for key in local_variables:
            self.domains[key] = saved_domains[key]
        return True
