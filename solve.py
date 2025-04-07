from board import Board, Connection, Required, Position, Relation, Cell

def solve(board: Board):
    return False



def rule_place_moons_near_suns(board):
    changed = False
    for r in range(board.rows):
        for c in range(board.cols - 1):
            if board.board[r][c] is Cell.SUN and board.board[r][c + 1] is Cell.SUN:
                # Check left
                if c - 1 >= 0 and board.board[r][c - 1] is Cell.EMPTY:
                    board.board[r][c - 1] = Cell.MOON
                    changed = True
                # Check right
                if c + 2 < board.cols and board.board[r][c + 2] is Cell.EMPTY:
                    board.board[r][c + 2] = Cell.MOON
                    changed = True

    for c in range(board.cols):
        for r in range(board.rows - 1):
            if board.board[r][c] is Cell.SUN and board.board[r + 1][c] is Cell.SUN:
                # Check left
                if r - 1 >= 0 and board.board[r - 1][c] is Cell.EMPTY:
                    board.board[r - 1][c] = Cell.MOON
                    changed = True
                # Check right
                if r + 2 < board.rows and board.board[r + 2][c] is Cell.EMPTY:
                    board.board[r + 2][c] = Cell.MOON
                    changed = True
    return changed

def rule_place_suns_near_moons(board):
    changed = False
    for r in range(board.rows):
        for c in range(board.cols - 1):
            if board.board[r][c] is Cell.MOON and board.board[r][c + 1] is Cell.MOON:
                # Check left
                if c - 1 >= 0 and board.board[r][c - 1] is Cell.EMPTY:
                    board.board[r][c - 1] = Cell.SUN
                    changed = True
                # Check right
                if c + 2 < board.cols and board.board[r][c + 2] is Cell.EMPTY:
                    board.board[r][c + 2] = Cell.SUN
                    changed = True

    for c in range(board.cols):
        for r in range(board.rows - 1):
            if board.board[r][c] is Cell.MOON and board.board[r + 1][c] is Cell.MOON:
                # Check left
                if r - 1 >= 0 and board.board[r - 1][c] is Cell.EMPTY:
                    board.board[r - 1][c] = Cell.SUN
                    changed = True
                # Check right
                if r + 2 < board.rows and board.board[r + 2][c] is Cell.EMPTY:
                    board.board[r + 2][c] = Cell.SUN
                    changed = True

    return changed

def rule_fill_overloaded(board):
    changed = False
    for r in range(board.rows):
        moon_sum = 0
        sun_sum = 0
        for c in range(board.cols):
            if board.board[r][c] is Cell.MOON:
                moon_sum += 1
            elif board.board[r][c] is Cell.SUN:
                sun_sum += 1
        if moon_sum >= 3:
            for c in range(board.cols):
                if board.board[r][c] is Cell.EMPTY:
                    board.board[r][c] = Cell.SUN
                    changed = True
        elif sun_sum >= 3:
            for c in range(board.cols):
                if board.board[r][c] is Cell.EMPTY:
                    board.board[r][c] = Cell.MOON
                    changed = True

    for c in range(board.cols):
        moon_sum = 0
        sun_sum = 0
        for r in range(board.rows):
            if board.board[r][c] is Cell.MOON:
                moon_sum += 1
            elif board.board[r][c] is Cell.SUN:
                sun_sum += 1
        if moon_sum >= 3:
            for r in range(board.rows):
                if board.board[r][c] is Cell.EMPTY:
                    board.board[r][c] = Cell.SUN
                    changed = True
        elif sun_sum >= 3:
            for r in range(board.rows):
                if board.board[r][c] is Cell.EMPTY:
                    board.board[r][c] = Cell.MOON
                    changed = True
    return changed

def rule_apply_connections(board):
    changed = False
    for connection in board.connections:
        if connection.relation is Relation.EQ:
            if board.cell_at(connection.posA) != board.cell_at(connection.posB):
                if board.cell_at(connection.posA) is Cell.EMPTY:
                    board.set_cell(connection.posA, board.cell_at(connection.posB))
                    changed = True
                else:
                    board.set_cell(connection.posB, board.cell_at(connection.posA))
                    changed = True
        if connection.relation is Relation.NEQ:
            if board.cell_at(connection.posA) is Cell.EMPTY and not board.cell_at(connection.posB) is Cell.EMPTY:
                if board.cell_at(connection.posB) is Cell.MOON:
                    board.set_cell(connection.posA, Cell.SUN)
                    changed = True
                elif board.cell_at(connection.posB) is Cell.SUN:
                    board.set_cell(connection.posA, Cell.MOON)
                    changed = True
            if board.cell_at(connection.posB) is Cell.EMPTY and not board.cell_at(connection.posA) is Cell.EMPTY:
                if board.cell_at(connection.posA) is Cell.MOON:
                    board.set_cell(connection.posB, Cell.SUN)
                    changed = True
                elif board.cell_at(connection.posA) is Cell.SUN:
                    board.set_cell(connection.posB, Cell.MOON)
                    changed = True
    return changed

rules = [
    rule_place_moons_near_suns,
    rule_place_suns_near_moons,
    rule_fill_overloaded,
    rule_apply_connections,
]
