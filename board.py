from enum import Enum

class Board:
    def __init__(self, connections, requireds):
        self.rows = 6
        self.cols = 6
        self.connections = connections
        self.requireds = requireds


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
