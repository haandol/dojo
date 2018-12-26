from pprint import pprint


def _solve(visited, n, matrix):
  node = -1
  for i in range(n):
    if not visited[i]:
      node = i
      break

  if node == -1:
    return 1

  ret = 0
  for friend in range(node+1, n):
    if not visited[friend] and matrix[node][friend]:
      visited[node] = True
      visited[friend] = True
      ret += _solve(visited, n, matrix)
      visited[node] = False
      visited[friend] = False

  return ret


def solve(n, data):
  visited = [False] * n
  matrix = [[False] * n for _ in range(n)]
  for i in range(0, len(data), 2):
    node1 = int(data[i])
    node2 = int(data[i+1])
    row = min(node1, node2)
    col = max(node1, node2)
    matrix[row][col] = True
  # pprint(matrix)
  return _solve(visited, n, matrix)


if __name__ == '__main__':
  assert 1 == solve(2, '01')
  assert 3 == solve(4, '011223300213')
  assert 4 == solve(6, '01021213142324343545')