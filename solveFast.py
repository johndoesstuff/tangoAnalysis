# god has granted my a divine vision for a faster solution algorithm that only searches 1.6m combinations instead of 150 quadrillion

from board import Board, Connection, Required, Position, Relation, Cell
import copy

m = Cell.MOON
s = Cell.SUN

solvedRows = [
        [0, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0],
]

solvedRowsInv = [[0 for _ in range(6)] for _ in range(7)]
for r in range(7):
    for c in range(6):
        solvedRowsInv[r][c] = 1 - solvedRows[r][c]

def findSolutions():
    print("Searching Solution Space")
    print(solvedRows)
    print(solvedRowsInv)
    solutions = []
    for a in range(14):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    for e in range(7):
                        for f in range(7):
                            for g in range(7):
                                solutions.append(generateSolutionTree(a, b, c, d, e, f, g))
    print("Validating Solutions")
    solutionsFinal = []
    for solution in solutions:
        board = Board(connections=[], requireds=[])
        for r in range(6):
            for c in range(6):
                if (solution[r][c] == 0):
                    board.board[r][c] = Cell.MOON
                else:
                    board.board[r][c] = Cell.SUN
        if (board.is_solved()):
            solutionsFinal.append(board)
        # board.print_board()
    return solutionsFinal

def generateSolutionTree(a, b, c, d, e, f, g):
    solution = [[0 for _ in range(6)] for _ in range(6)]
    for i in range(6):
        if a < 7:
            solution[i][0] = solvedRows[a][i]
        elif a < 14:
            solution[i][0] = solvedRowsInv[a-7][i]
        else:
            raise Exception("a must be between 0-13")

    if solution[0][0] == 0:
        solution[0] = solvedRows[b]
    else:
        solution[0] = solvedRowsInv[b]

    if solution[1][0] == 0:
        solution[1] = solvedRows[c]
    else:
        solution[1] = solvedRowsInv[c]

    if solution[2][0] == 0:
        solution[2] = solvedRows[d]
    else:
        solution[2] = solvedRowsInv[d]

    if solution[3][0] == 0:
        solution[3] = solvedRows[e]
    else:
        solution[3] = solvedRowsInv[e]

    if solution[4][0] == 0:
        solution[4] = solvedRows[f]
    else:
        solution[4] = solvedRowsInv[f]

    if solution[5][0] == 0:
        solution[5] = solvedRows[g]
    else:
        solution[5] = solvedRowsInv[g]

    return solution


print(len(findSolutions()))
