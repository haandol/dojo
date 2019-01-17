cache = []

def _sum(A, B, C, D, i, j, k, l):
  n = len(A)
  if i == n or j == n or k == n or l == n:
    return 0

  s = 0
  if 0 == sum([A[i], B[j], C[k], D[l]]):
    key = (i, j, k, l)
    if key not in cache:
      cache.append(key)
      s = 1

  return s + (
    _sum(A, B, C, D, i+1, j, k, l) +
    _sum(A, B, C, D, i, j+1, k, l) +
    _sum(A, B, C, D, i, j, k+1, l) +
    _sum(A, B, C, D, i, j, k, l+1)
  )


def fourSumCount(A, B, C, D):
  return _sum(A, B, C, D, 0, 0, 0, 0)


A = [1, 2]
B = [-2,-1]
C = [-1, 2]
D = [0, 2]
print(fourSumCount(A, B, C, D))