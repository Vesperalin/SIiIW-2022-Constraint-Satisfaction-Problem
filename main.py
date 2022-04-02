from copy import deepcopy

from utils.data_reader import read_data_from_file
from puzzle.binary_puzzle import BinaryPuzzle
from puzzle.puzzle import Puzzle
from puzzle.futoshiki_puzzle import Futoshiki_Puzzle
from solvers.CSP_backtracking_solver import CSPBacktrackingSolver
from solvers.CSP_ac3_solver import CSPAC3Solver
from solvers.CSP_forward_checking import CSPForwardCheckingSolver
from solvers.CSP_solver import CSPSolver


# TODO imporve look ahead (add unary constraints, improve domains) and J.K. idea
# TODO delete CSP_backtrackin_solver and CSP_forward_checking - they are in CSP_Solver
# TODO delete print when adding to results in csp


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

    csp = CSPSolver(puzzle_binary_6, 'LA', 'CON', 'CON')
    csp.solve()
    results = csp.results

    if len(results) == 0:
        print('Solutions not found')
    else:
        print('Found {} solutions for forward searching'.format(len(results)))
        print("First result")
        print_result(results[0], puzzle_binary_6.size)
        print("Visited nodes: " + str(csp.nodes))

    """algo_modes = ['BT', 'FC', 'LS']  # 'LA'
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON', 'LCV']"""

    """csp = CSPAC3Solver(puzzle_futoshiki_6)
        csp.ac3_search({})
        results = csp.results"""

    """csp = CSPForwardCheckingSolver(puzzle_binary_6)
    csp.forward_checking()
    results = csp.results"""

    """csp = CSPBacktrackingSolver(puzzle_futoshiki_6)
    csp.backtracking_search({})
    results = csp.results"""

    """if len(results) == 0:
        print('Solutions not found')
    else:
        print('Found {} solutions for forward searching'.format(len(results)))
        print("First result")
        print_result(results[0], puzzle_binary_6.size)
        print("Visited nodes: " + str(csp.nodes))"""

    """csp = CSPSolver(puzzle_binary_10, 'BT', 'RND')
    csp.solve()
    results = csp.results

    print("Binray {}x{}".format(puzzle_binary_10.size, puzzle_binary_10.size))

    if len(results) == 0:
        print('Solutions not found')
    else:
        print('Found {} solutions for {}, {}'.format(len(results), 'BT', 'RND'))
        print("First result")
        print_result(results[0], puzzle_binary_10.size)
        print("Visited nodes: " + str(csp.nodes))"""

    """for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results

                    print("Binray {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}'
                              .format(len(results), mode, var_heu, val_heu))
                        print("First result")
                        print_result(results[0], puzzle.size)
                        print("Visited nodes: " + str(csp.nodes))
        print('**********************************************************************************')"""

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results

                    print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                        print(" ")
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("First result")
                        print_result(results[0], puzzle.size)
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')
