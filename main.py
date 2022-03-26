from utils.data_reader import read_data_from_file
from puzzle.binary_puzzle import BinaryPuzzle
from puzzle.futoshiki_puzzle import Futoshiki_Puzzle
from solvers.CSP_solver import CSPSolver

# TODO add types
# TODO refactor names
# TODO add comments
# TODO - zrozumieć constrainty
# TODO - zrozumieć binary i futo
# TODO zmienić w futo i binary rows i columns na jeden wymiar tylko np size
# TODO - ogólnie te fory przepisać na starodawne fory
# TODO - constrainty przepisać - nazwy i zmienne
# TODO - pozmieniać to co się printuje na błędach
# TODO - pozmieniać w CSP_Solver
# TODO - pozmieniać w mainie troche
# TODO - zmienić sposób rozruchu aplikacji
# TODO - refactor UniqueColsAndRowsConstraint - już sił nie miałam


if __name__ == '__main__':
    # for binary puzzle
    data = read_data_from_file('binary_6x6')
    binary = BinaryPuzzle(6, 6, data)
    csp = CSPSolver(binary.variables, binary.domains)

    for constraint in binary.constraints:
        csp.add_constraint(constraint)

    csp.backtracking_search({})

    solutions = csp.solutions

    if len(solutions) == 0:
        print(f"No solutions found for Binary {binary.rows} x {binary.columns}")
    else:
        print(f'Found {len(solutions)} solutions for Binary {binary.rows} x {binary.columns}')
        print("Sample result")

        sample = list(solutions[0].values())

        for index in range(len(sample)):
            print(sample[index], end=' ')

            if index % binary.rows == binary.rows - 1:
                print()

    data = read_data_from_file('futoshiki_4x4')
    futoshiki = Futoshiki_Puzzle(4, 4, data)
    # print(futoshiki)
    csp = CSPSolver(futoshiki.variables, futoshiki.domains)

    for constraint in futoshiki.constraints:
        csp.add_constraint(constraint)

    csp.backtracking_search({})

    solutions = csp.solutions

    if len(solutions) == 0:
        print(f"No solutions found for Binary {futoshiki.rows} x {futoshiki.columns}")
    else:
        print(f'Found {len(solutions)} solutions for Binary {futoshiki.rows} x {futoshiki.columns}')
        print("Sample result")

        sample = list(solutions[0].values())

        for index in range(len(sample)):
            print(sample[index], end=' ')

            if index % futoshiki.rows == futoshiki.rows - 1:
                print()
