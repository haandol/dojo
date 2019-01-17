def solve(arr):
  n = len(arr)
  lis = [1 for _ in range(n)]
  for i in range(1, n):
    for j in range(0, i):
      if arr[j] < arr[i] and lis[i] < 1 + lis[j]:
        lis[i] = 1 + lis[j]

  return max(lis)


arr = [3, 10, 2, 1, 20]
assert 3 == solve(arr)

arr = [3, 2]
assert 1 == solve(arr)

arr = [50, 3, 10, 7, 40, 80]
assert 4 == solve(arr)