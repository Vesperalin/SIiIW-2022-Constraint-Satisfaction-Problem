from copy import deepcopy

from utils.data_reader import read_data_from_file
from puzzle.binary_puzzle import BinaryPuzzle
from puzzle.puzzle import Puzzle
from puzzle.futoshiki_puzzle import Futoshiki_Puzzle
from solvers.CSP_backtracking_solver import CSPBacktrackingSolver
from solvers.CSP_ac3_solver import CSPAC3Solver
from solvers.CSP_forward_checking import CSPForwardCheckingSolver

# TODO implement easy forward checking
# TODO add returns counter in backtracking
# TODO merge CSP backtracking solver and forward checking solver and ac3
# TODO add heuristics for variable
# TODO add heuristic for value
# TODO improve ac3 speed


def print_result(result, size):
    grid = []
    for i in range(size):
        grid.append([0 for j in range(size)])

    for key in result.keys():
        grid[key.row_number][key.column_number] = result[key]

    for y in grid:
        to_print: str = ''
        for x in y:
            to_print += (str(x) + ' ')
        print(to_print)


if __name__ == '__main__':
    binary_data_6: str = read_data_from_file('binary_6x6')
    puzzle_binary_6: Puzzle = BinaryPuzzle(6, binary_data_6)

    binary_data_8: str = read_data_from_file('binary_8x8')
    puzzle_binary_8: Puzzle = BinaryPuzzle(8, binary_data_8)

    binary_data_10: str = read_data_from_file('binary_10x10')
    puzzle_binary_10: Puzzle = BinaryPuzzle(10, binary_data_10)

    futoshuiki_data_4: str = read_data_from_file('futoshiki_4x4')
    puzzle_futoshiki_4: Puzzle = Futoshiki_Puzzle(4, futoshuiki_data_4)

    futoshuiki_data_5: str = read_data_from_file('futoshiki_5x5')
    puzzle_futoshiki_5: Puzzle = Futoshiki_Puzzle(5, futoshuiki_data_5)

    futoshuiki_data_6: str = read_data_from_file('futoshiki_6x6')
    puzzle_futoshiki_6: Puzzle = Futoshiki_Puzzle(6, futoshuiki_data_6)

    binary_puzzles = [puzzle_binary_6, puzzle_binary_8, puzzle_binary_10]
    futoshiki_puzzles = [puzzle_futoshiki_4, puzzle_futoshiki_5, puzzle_futoshiki_6]

    """for puzzle in binary_puzzles:
        csp = CSPBacktrackingSolver(puzzle)
        csp.backtracking_search({})
        results = csp.results

        print("Binray {}x{}".format(puzzle.size, puzzle.size))

        if len(results) == 0:
            print('Solutions not found')
        else:
            print('Found {} solutions for baktracking'.format(len(results)))
            print("First result")
            print_result(results[0], puzzle.size)
            print("Visited nodes: " + str(csp.nodes))

        csp = CSPForwardCheckingSolver(puzzle)
        csp.forward_checking_search({})
        results = csp.results

        if len(results) == 0:
            print('Solutions not found')
        else:
            print('Found {} solutions for forward searching'.format(len(results)))
            print("First result")
            print_result(results[0], puzzle.size)
            print("Visited nodes: " + str(csp.nodes))

        csp = CSPAC3Solver(puzzle)
        csp.ac3_search({})
        results = csp.results

        if len(results) == 0:
            print('Solutions not found')
        else:
            print('Found {} solutions fo ac3'.format(len(results)))
            print("First result")
            print_result(results[0], puzzle.size)
            print("Visited nodes: " + str(csp.nodes))
        
        print('**********************************************************************************')"""

    csp = CSPAC3Solver(puzzle_futoshiki_6)
    csp.ac3_search({})
    results = csp.results

    if len(results) == 0:
        print('Solutions not found')
    else:
        print('Found {} solutions for forward searching'.format(len(results)))
        print("First result")
        print_result(results[0], puzzle_futoshiki_6.size)
        print("Visited nodes: " + str(csp.nodes))

    """for puzzle in futoshiki_puzzles:
        csp = CSPBacktrackingSolver(puzzle)
        csp.backtracking_search({})
        results = csp.results

        print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

        if len(results) == 0:
            print('Solutions not found')
        else:
            print('Found {} solutions for baktracking'.format(len(results)))
            print("First result")
            print_result(results[0], puzzle.size)
            print("Visited nodes: " + str(csp.nodes))

        original_domains = {}
        for key in puzzle.domains.keys():
            original_domains[key] = deepcopy(puzzle.domains[key])

        csp = CSPForwardCheckingSolver(puzzle)
        csp.forward_checking_search({})
        results = csp.results

        if len(results) == 0:
            print('Solutions not found')
        else:
            print('Found {} solutions for forward searching'.format(len(results)))
            print("First result")
            print_result(results[0], puzzle.size)
            print("Visited nodes: " + str(csp.nodes))

        puzzle.domains = original_domains
        csp = CSPAC3Solver(puzzle)
        csp.ac3_search({})
        results = csp.results

        if len(results) == 0:
            print('Solutions not found')
        else:
            print('Found {} solutions fo ac3'.format(len(results)))
            print("First result")
            print_result(results[0], puzzle.size)
            print("Visited nodes: " + str(csp.nodes))

        print('**********************************************************************************')"""
