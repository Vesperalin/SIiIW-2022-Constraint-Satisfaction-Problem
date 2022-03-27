from utils.data_reader import read_data_from_file
from puzzle.binary_puzzle import BinaryPuzzle
from puzzle.puzzle import Puzzle
from puzzle.futoshiki_puzzle import Futoshiki_Puzzle
from solvers.CSP_backtracking_solver import CSPBacktrackingSolver


def print_result_binary(result, size):
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


def print_result_futoshiki(result, size):
    grid = []
    for i in range(size):
        grid.append([0 for j in range(size)])

    for key in result.keys():
        grid[key.row_number // 2][key.column_number // 2] = result[key]

    for y in grid:
        to_print: str = ''
        for x in y:
            to_print += (str(x) + ' ')
        print(to_print)


if __name__ == '__main__':
    """data: str = read_data_from_file('binary_6x6')
    puzzle: Puzzle = BinaryPuzzle(6, data)"""
    data: str = read_data_from_file('futoshiki_6x6')
    puzzle: Puzzle = Futoshiki_Puzzle(6, data)

    csp = CSPBacktrackingSolver(puzzle)
    csp.backtracking_search({})
    results = csp.results

    if len(results) == 0:
        print('Solutions not found')
    else:
        print('Found {} solutions'.format(len(results)))
        print("First result")
        if type(puzzle) == BinaryPuzzle:
            print_result_binary(results[0], puzzle.size)
        else:
            print_result_futoshiki(results[0], puzzle.size)