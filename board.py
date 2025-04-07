from enum import Enum

class Board:
    def __init__(self, connections, requireds):
        self.rows = 6
        self.cols = 6
        self.connections = connections
        self.requireds = requireds
        self.board = [[Cell.EMPTY for _ in range(6)] for _ in range(6)]
        for requirement in requireds:
            self.board[requirement.pos.row][requirement.pos.col] = requirement.cell

    def print_board(self):
        cell_symbols = {
            Cell.EMPTY: " . ",
            Cell.SUN: " O ",
            Cell.MOON: " C "
        }

        def get_relation(pos1, pos2):
            for conn in self.connections:
                if (conn.posA == pos1 and conn.posB == pos2) or (conn.posB == pos1 and conn.posA == pos2):
                    return "=" if conn.relation == Relation.EQ else "x"
            return " "  # No connection

        for row in range(self.rows):
            line = ""
            for col in range(self.cols):
                line += cell_symbols[self.board[row][col]]
                if col < self.cols - 1:
                    line += get_relation(Position(row, col), Position(row, col + 1))
            print(line)
            if row < self.rows - 1:
                between = " "
                for col in range(self.cols):
                    between += get_relation(Position(row, col), Position(row + 1, col))
                    if col < self.cols - 1:
                        between += "   "  # space between vertical connections
                print(between)


class Connection:
    def __init__(self, posA, posB, relation):
        if checkAdj(posA, posB):
            self.posA = posA
            self.posB = posB
            self.relation = relation
        else:
            raise Exception("Connected positions must be adjacent")

class Position:
    def __init__(self, row, col):
        if row >= 0 and row < 6:
            self.row = row
        else:
            raise Exception("Row must be between 0 and 5")
        if col >= 0 and col < 6:
            self.col = col
        else:
            raise Exception("Col must be between 0 and 5")
    def __eq__(self, other):
        return isinstance(other, Position) and self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))



class Required:
    def __init__(self, pos, cell):
        if cell == Cell.EMPTY:
            raise Exception("Cannot require an empty cell")
        else:
            self.pos = pos
            self.cell = cell

class Relation(Enum):
    EQ = 1
    NEQ = 2

class Cell(Enum):
    EMPTY = 0
    SUN = 1
    MOON = 2


def checkAdj(posA, posB):
    if (abs(posA.row - posB.row) == 1 and posA.col == posB.col):
        return True
    elif (abs(posA.col - posB.col) == 1 and posA.row == posB.row):
        return True
    else:
        return False


requireds = [
    Required(Position(0, 0), Cell.SUN),
    Required(Position(0, 1), Cell.MOON),
    Required(Position(1, 0), Cell.MOON),
    Required(Position(1, 1), Cell.SUN),
]

connections = [
    Connection(Position(0, 0), Position(0, 1), Relation.NEQ),
    Connection(Position(0, 0), Position(1, 0), Relation.EQ),
    Connection(Position(0, 1), Position(1, 1), Relation.EQ),
]

board = Board(connections, requireds)
board.print_board()
