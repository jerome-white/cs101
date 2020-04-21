from collections import namedtuple

Marker = namedtuple('Marker', 'start, open, boundary, goal')
markers = Marker('o', '.', '@', 'x')

def inbounds(board, row, col):
    too_small = row < 0 or col < 0
    too_big = row >= len(board) or col >= len(board[row])
    
    return not too_big and not too_small

def get_board(fname):
    fp = open(fname)
    board = []
    for line in fp:
        board.append(list(line.strip()))
    fp.close()

    return board

def get_start(board):
    for (i, row) in enumerate(board):
        for (j, cell) in enumerate(row):
            if cell == markers.start:
                return (i, j)

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def indent_print(spaces, string):
    print(' ' * spaces, string)
