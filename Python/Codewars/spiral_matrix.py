from collections import deque
size = 3
matrix = [input().split() for _ in range(size)]
[print(line) for line in matrix]

visited = []


def down(row, col):
    return move(row, col, 1, 0)


def left(row, col):
    return move(row, col, 0, -1)


def up(row, col):
    return move(row, col, -1, 0)


def right(row, col):
    return move(row, col, 0, 1)


def move(row, col, row_move, col_move):
    while True:
        col += col_move
        row += row_move
        if (row, col) in visited:
            return row - row_move, col - col_move
        if size > row >= 0 and size > col >= 0:
            print(matrix[row][col])
            visited.append((row, col))
            continue
        return row - row_move, col - col_move


directions = deque([right, down, left, up])
row = 0
col = -1

while True:
    if len(visited) == len(matrix) * len(matrix[0]):
        break
    func = directions.popleft()
    directions.append(func)
    row, col = func(row, col)










