def solve(matrix, row, col, i, keyword):
  if i == len(keyword):
    return True

  if 4 < row or 4 < col:
    return False

  if matrix[row][col] != keyword[i]:
    return False

  direction = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
  ]

  for dy, dx in direction:
    if solve(matrix, row+dy, col+dx, i+1, keyword):
      return True
  return False


if __name__ == '__main__':
  matrix = [
    'URLPM',
    'XPRET',
    'GIAET',
    'XTNZY',
    'XOQRS'
  ]
  assert True == solve(matrix, 1, 1, 0, 'PRETTY')
  assert True == solve(matrix, 2, 0, 0, 'GIRL')
  assert False == solve(matrix, 0, 0, 0, 'YES')