def _solve(arr, start):
  n = len(arr)

  ret = 1
  for i in range(start, n):
    if arr[start] < arr[i]:
      ret = max(ret, 1 + _solve(arr, i))
  return ret


def solve(arr):
  n = len(arr)
  ret = 1
  for i in range(n):
    ret = max(ret, _solve(arr, i))
  return ret


if __name__ == '__main__':
  L = [3, 10, 2, 1, 20]
  assert 3 == solve(L)

  L = [3, 1]
  assert 1 == solve(L)

  L = [50, 3, 10, 7, 40, 80]
  assert 4 == solve(L)

  L = [10, 22, 9, 33, 21, 50, 41, 60, 80]
  assert 6 == solve(L)