pieces = [
  [(0, 0), (1, 0), (0, 1)],
  [(0, 0), (0, 1), (1, 1)],
  [(0, 0), (1, 0), (1, 1)],
  [(0, 0), (1, 0), (1, -1)]
]

def cover(board, kind, y, x, delta):
  height = len(board)
  width = len(board[0])
  is_coverable = True
  for dy, dx in pieces[kind]:
    if y+dy < 0 or height <= y+dy or x+dx < 0 or width <= x+dx:
      is_coverable = False
    else:
      board[y+dy][x+dx] += delta
      if 1 < board[y+dy][x+dx]:
        is_coverable = False
  return is_coverable


def solve(board):
  height = len(board)
  width = len(board[0])

  y = -1
  x = -1
  for i in range(height):
    for j in range(width):
      if board[i][j] == 0:
        y = i
        x = j
        break
    if y != -1:
      break
  if y == -1:
    return 1

  ret = 0
  for kind in range(len(pieces)):
    if cover(board, kind, y, x, 1):
      ret += solve(board)
    cover(board, kind, y, x, -1)
  return ret


if __name__ == '__main__':
  board = [
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1]
  ]
  assert 0 == solve(board)

  board = [
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1]
  ]
  assert 2 == solve(board)

  board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  ]
  assert 1514 == solve(board)