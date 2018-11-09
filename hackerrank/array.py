# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def arrayManipulation(n, queries):
  arr = [0] * n
  m = len(queries)
  L = [
    [0] * n
    for _ in range(m)
  ]
  print(L)

  for start, end, val in queries:
    for i in range(start-1, end):
      arr[i] += val

  return max(arr)


n = 5
queries = [
  [1, 2, 100],
  [2, 5, 100],
  [3, 4, 100]
]
assert 200 == arrayManipulation(n, queries)