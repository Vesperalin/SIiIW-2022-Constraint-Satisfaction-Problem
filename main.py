import matplotlib.pyplot as plt
from math import sqrt

from utils.data_reader import read_data_from_file
from puzzle.binary_puzzle import BinaryPuzzle
from puzzle.puzzle import Puzzle
from puzzle.futoshiki_puzzle import Futoshiki_Puzzle
from solvers.CSP_solver import CSPSolver


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


def show_graphs(x_axis, y_axis_nodes_1, y_axis_nodes_2, y_axis_time_1, y_axis_time_2, label1, label2):
    plt.subplots()
    plt.plot(x_axis, y_axis_nodes_1, label=label1)
    plt.plot(x_axis, y_axis_nodes_2, label=label2)
    plt.ylabel("nodes")
    plt.xlabel("puzzle size")
    plt.legend()

    plt.subplots()
    plt.plot(x_axis, y_axis_time_1, label=label1)
    plt.plot(x_axis, y_axis_time_2, label=label2)
    plt.ylabel("time")
    plt.xlabel("puzzle size")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    binary_data_4: str = read_data_from_file('binary_4x4')
    puzzle_binary_4: Puzzle = BinaryPuzzle(4, binary_data_4)

    binary_data_6: str = read_data_from_file('binary_6x6')
    puzzle_binary_6: Puzzle = BinaryPuzzle(6, binary_data_6)

    binary_data_8: str = read_data_from_file('binary_8x8')
    puzzle_binary_8: Puzzle = BinaryPuzzle(8, binary_data_8)

    binary_data_10: str = read_data_from_file('binary_10x10')
    puzzle_binary_10: Puzzle = BinaryPuzzle(10, binary_data_10)

    binary_data_12: str = read_data_from_file('binary_12x12')
    puzzle_binary_12: Puzzle = BinaryPuzzle(12, binary_data_12)

    binary_data_14: str = read_data_from_file('binary_14x14')
    puzzle_binary_14: Puzzle = BinaryPuzzle(14, binary_data_14)

    futoshuiki_data_3: str = read_data_from_file('futoshiki_3x3')
    puzzle_futoshiki_3: Puzzle = Futoshiki_Puzzle(3, futoshuiki_data_3)

    futoshuiki_data_4: str = read_data_from_file('futoshiki_4x4')
    puzzle_futoshiki_4: Puzzle = Futoshiki_Puzzle(4, futoshuiki_data_4)

    futoshuiki_data_5: str = read_data_from_file('futoshiki_5x5')
    puzzle_futoshiki_5: Puzzle = Futoshiki_Puzzle(5, futoshuiki_data_5)

    futoshuiki_data_6: str = read_data_from_file('futoshiki_6x6')
    puzzle_futoshiki_6: Puzzle = Futoshiki_Puzzle(6, futoshuiki_data_6)

    futoshuiki_data_7: str = read_data_from_file('futoshiki_7x7')
    puzzle_futoshiki_7: Puzzle = Futoshiki_Puzzle(7, futoshuiki_data_7)

    futoshuiki_data_8: str = read_data_from_file('futoshiki_8x8')
    puzzle_futoshiki_8: Puzzle = Futoshiki_Puzzle(8, futoshuiki_data_8)

    binary_puzzles = [puzzle_binary_4, puzzle_binary_6, puzzle_binary_8, puzzle_binary_10, puzzle_binary_12, puzzle_binary_14]
    futoshiki_puzzles = [puzzle_futoshiki_3, puzzle_futoshiki_4, puzzle_futoshiki_5, puzzle_futoshiki_6, puzzle_futoshiki_7, puzzle_futoshiki_8]

# ***************************************** studies *****************************************
# MRV heuristic studies - for binary puzzle
    """algo_modes = ['FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_con = []
    y_axis_nodes_mrv = []
    y_axis_time_con = []
    y_axis_time_mrv = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results
                    if var_heu == 'CON':
                        y_axis_nodes_con.append(csp.nodes)
                        y_axis_time_con.append(csp.time)
                    else:
                        y_axis_nodes_mrv.append(csp.nodes)
                        y_axis_time_mrv.append(csp.time)

                    print("Binary {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')
    show_graphs(x_axis, y_axis_nodes_con, y_axis_nodes_mrv, y_axis_time_con, y_axis_time_mrv, "CON", "MRV")"""

# MRV heuristic studies - for futoshiki puzzle
    """algo_modes = ['FC']
        variable_heuristics = ['CON', 'MRV']
        value_heuristics = ['CON']
    
        x_axis: list[int] = [3, 4, 5, 6, 7, 8]
        y_axis_nodes_con = []
        y_axis_nodes_mrv = []
        y_axis_time_con = []
        y_axis_time_mrv = []
    
        for puzzle in futoshiki_puzzles:
            for mode in algo_modes:
                for var_heu in variable_heuristics:
                    for val_heu in value_heuristics:
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if var_heu == 'CON':
                            y_axis_nodes_con.append(csp.nodes)
                            y_axis_time_con.append(csp.time)
                        else:
                            y_axis_nodes_mrv.append(csp.nodes)
                            y_axis_time_mrv.append(csp.time)
    
                        print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))
    
                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
            print('**********************************************************************************')
        show_graphs(x_axis, y_axis_nodes_con, y_axis_nodes_mrv, y_axis_time_con, y_axis_time_mrv, "CON", "MRV")"""

# LCV heuristic studies - for binary puzzle
    """algo_modes = ['FC']
    variable_heuristics = ['CON']
    value_heuristics = ['CON', 'LCV']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_con = []
    y_axis_nodes_lcv = []
    y_axis_time_con = []
    y_axis_time_lcv = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results
                    if val_heu == 'CON':
                        y_axis_nodes_con.append(csp.nodes)
                        y_axis_time_con.append(csp.time)
                    else:
                        y_axis_nodes_lcv.append(csp.nodes)
                        y_axis_time_lcv.append(csp.time)

                    print("Binary {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')
    show_graphs(x_axis, y_axis_nodes_con, y_axis_nodes_lcv, y_axis_time_con, y_axis_time_lcv, "CON", "LCV")"""

# LCV heuristic studies - for futoshiki puzzle
    """algo_modes = ['FC']
    variable_heuristics = ['CON']
    value_heuristics = ['CON', 'LCV']

    x_axis: list[int] = [3, 4, 5, 6, 7, 8]
    y_axis_nodes_con = []
    y_axis_nodes_lcv = []
    y_axis_time_con = []
    y_axis_time_lcv = []

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results
                    if val_heu == 'CON':
                        y_axis_nodes_con.append(csp.nodes)
                        y_axis_time_con.append(csp.time)
                    else:
                        y_axis_nodes_lcv.append(csp.nodes)
                        y_axis_time_lcv.append(csp.time)

                    print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')
    show_graphs(x_axis, y_axis_nodes_con, y_axis_nodes_lcv, y_axis_time_con, y_axis_time_lcv, "CON", "LCV")"""

# MRV + LCV - for binary puzzle
    """algo_modes = ['FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON', 'LCV']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_con = []
    y_axis_nodes_mrv_lcv = []
    y_axis_time_con = []
    y_axis_time_mrv_lcv = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (val_heu == 'CON' and var_heu == 'CON') or (val_heu == 'LCV' and var_heu == 'MRV'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if val_heu == 'CON':
                            y_axis_nodes_con.append(csp.nodes)
                            y_axis_time_con.append(csp.time)
                        else:
                            y_axis_nodes_mrv_lcv.append(csp.nodes)
                            y_axis_time_mrv_lcv.append(csp.time)

                        print("Binary {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')
    show_graphs(x_axis, y_axis_nodes_con, y_axis_nodes_mrv_lcv, y_axis_time_con, y_axis_time_mrv_lcv, "CON+CON", "MVR+LCV")"""

# MRV + LCV - for futoshiki puzzle
    """algo_modes = ['FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON', 'LCV']

    x_axis: list[int] = [3, 4, 5, 6, 7,  8]
    y_axis_nodes_con = []
    y_axis_nodes_mrv_lcv = []
    y_axis_time_con = []
    y_axis_time_mrv_lcv = []

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (val_heu == 'CON' and var_heu == 'CON') or (val_heu == 'LCV' and var_heu == 'MRV'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if val_heu == 'CON':
                            y_axis_nodes_con.append(csp.nodes)
                            y_axis_time_con.append(csp.time)
                        else:
                            y_axis_nodes_mrv_lcv.append(csp.nodes)
                            y_axis_time_mrv_lcv.append(csp.time)

                        print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')
    show_graphs(x_axis, y_axis_nodes_con, y_axis_nodes_mrv_lcv, y_axis_time_con, y_axis_time_mrv_lcv, "CON+CON", "MVR+LCV")"""

# BT (CON, CON) vs FC (CON, CON) - for binary puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON']
    value_heuristics = ['CON']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results
                    if mode == 'BT':
                        y_axis_nodes_bt.append(csp.nodes)
                        y_axis_time_bt.append(csp.time)
                    else:
                        y_axis_nodes_fc.append(csp.nodes)
                        y_axis_time_fc.append(csp.time)

                    print("Binary {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, CON) vs FC (CON, CON) - for futoshiki puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON']
    value_heuristics = ['CON']

    x_axis: list[int] = [3, 4, 5, 6, 7, 8]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results
                    if mode == 'BT':
                        y_axis_nodes_bt.append(csp.nodes)
                        y_axis_time_bt.append(csp.time)
                    else:
                        y_axis_nodes_fc.append(csp.nodes)
                        y_axis_time_fc.append(csp.time)

                    print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, CON) vs FC (MRV, CON) - for binary puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (mode == 'BT' and var_heu == 'CON' and val_heu == 'CON') \
                            or (mode == 'FC' and var_heu == 'MRV' and val_heu == 'CON'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if mode == 'BT':
                            y_axis_nodes_bt.append(csp.nodes)
                            y_axis_time_bt.append(csp.time)
                        else:
                            y_axis_nodes_fc.append(csp.nodes)
                            y_axis_time_fc.append(csp.time)

                        print("Binary {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, CON) vs FC (MRV, CON) - for futoshiki puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON']

    x_axis: list[int] = [3, 4, 5, 6, 7, 8]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (mode == 'BT' and var_heu == 'CON' and val_heu == 'CON') \
                            or (mode == 'FC' and var_heu == 'MRV' and val_heu == 'CON'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if mode == 'BT':
                            y_axis_nodes_bt.append(csp.nodes)
                            y_axis_time_bt.append(csp.time)
                        else:
                            y_axis_nodes_fc.append(csp.nodes)
                            y_axis_time_fc.append(csp.time)

                        print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, LCV) vs FC (CON, LCV) - for binary puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON']
    value_heuristics = ['LCV']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results
                    if mode == 'BT':
                        y_axis_nodes_bt.append(csp.nodes)
                        y_axis_time_bt.append(csp.time)
                    else:
                        y_axis_nodes_fc.append(csp.nodes)
                        y_axis_time_fc.append(csp.time)

                    print("Binary {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, LCV) vs FC (CON, LCV) - for futoshiki puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON']
    value_heuristics = ['LCV']

    x_axis: list[int] = [3, 4, 5, 6, 7, 8]
    # x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                    csp.solve()
                    results = csp.results
                    if mode == 'BT':
                        y_axis_nodes_bt.append(csp.nodes)
                        y_axis_time_bt.append(csp.time)
                    else:
                        y_axis_nodes_fc.append(csp.nodes)
                        y_axis_time_fc.append(csp.time)

                    print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                    if len(results) == 0:
                        print('Solutions not found')
                    else:
                        print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                              .format(len(results), mode, var_heu, val_heu, csp.time))
                        print("Visited nodes: " + str(csp.nodes))
                        print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, LCV) vs FC (MRV, LCV) - for binary puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['LCV']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (mode == 'BT' and var_heu == 'CON') or (mode == 'FC' and var_heu == 'MRV'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if mode == 'BT':
                            y_axis_nodes_bt.append(csp.nodes)
                            y_axis_time_bt.append(csp.time)
                        else:
                            y_axis_nodes_fc.append(csp.nodes)
                            y_axis_time_fc.append(csp.time)

                        print("Binary {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, LCV) vs FC (MRV, LCV) - for futoshiki puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['LCV']

    x_axis: list[int] = [3, 4, 5, 6, 7, 8]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (mode == 'BT' and var_heu == 'CON') or (mode == 'FC' and var_heu == 'MRV'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if mode == 'BT':
                            y_axis_nodes_bt.append(csp.nodes)
                            y_axis_time_bt.append(csp.time)
                        else:
                            y_axis_nodes_fc.append(csp.nodes)
                            y_axis_time_fc.append(csp.time)

                        print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')"""

# BT (CON, CON) vs FC (MRV, LCV) - for binary puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON', 'LCV']

    x_axis: list[int] = [4, 6, 8, 10, 12, 14]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in binary_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (mode == 'BT' and var_heu == 'CON' and val_heu == 'CON') \
                            or (mode == 'FC' and var_heu == 'MRV' and val_heu == 'LCV'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if mode == 'BT':
                            y_axis_nodes_bt.append(csp.nodes)
                            y_axis_time_bt.append(csp.time)
                        else:
                            y_axis_nodes_fc.append(csp.nodes)
                            y_axis_time_fc.append(csp.time)

                        print("Binary {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""

# BT (CON, CON) vs FC (MRV, LCV) - for futoshiki puzzle
    """algo_modes = ['BT', 'FC']
    variable_heuristics = ['CON', 'MRV']
    value_heuristics = ['CON', 'LCV']

    x_axis: list[int] = [3, 4, 5, 6, 7, 8]
    y_axis_nodes_bt = []
    y_axis_nodes_fc = []
    y_axis_time_bt = []
    y_axis_time_fc = []

    for puzzle in futoshiki_puzzles:
        for mode in algo_modes:
            for var_heu in variable_heuristics:
                for val_heu in value_heuristics:
                    if (mode == 'BT' and var_heu == 'CON' and val_heu == 'CON') \
                            or (mode == 'FC' and var_heu == 'MRV' and val_heu == 'LCV'):
                        csp = CSPSolver(puzzle, mode, var_heu, val_heu)
                        csp.solve()
                        results = csp.results
                        if mode == 'BT':
                            y_axis_nodes_bt.append(csp.nodes)
                            y_axis_time_bt.append(csp.time)
                        else:
                            y_axis_nodes_fc.append(csp.nodes)
                            y_axis_time_fc.append(csp.time)

                        print("Futoshiki {}x{}".format(puzzle.size, puzzle.size))

                        if len(results) == 0:
                            print('Solutions not found')
                        else:
                            print('Found {} solutions for {}, variable heuristic: {}, value heuristic: {}, time: {} s'
                                  .format(len(results), mode, var_heu, val_heu, csp.time))
                            print("Visited nodes: " + str(csp.nodes))
                            print(" ")
        print('**********************************************************************************')

    show_graphs(x_axis, y_axis_nodes_bt, y_axis_nodes_fc, y_axis_time_bt, y_axis_time_fc, "BT", "FC")"""
