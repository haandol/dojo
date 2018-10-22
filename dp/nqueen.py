# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

def is_safe(board, x, y, row, col):
  for i in range(col):
    if board[row][i] == 1:
      return False

  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  for i, j in zip(range(row, y), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  return True


def queen(board, n):
  x = len(board[0])
  y = len(board)
  return _queen(board, n, x, y, 0, 0)


def _queen(board, n, x, y, row, col):
  if n == sum(map(lambda x: sum(x), board)):
    return True

  for i in range(y):
    if is_safe(board, x, y, i, col):
      board[i][col] = 1
      if _queen(board, n, x, y, i, col + 1):
        return True
      board[i][col] = 0

  return False


board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print(queen(board, 4))
for row in board:
  print(row)