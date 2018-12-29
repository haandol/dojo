# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapsack(W, V, cap, i, cache):
  if i == len(V):
    return 0

  ret = cache[cap][i]
  if not ret:
    ret = knapsack(W, V, cap, i+1, cache)
  
  if W[i] <= cap:
    ret = max(ret, V[i] + knapsack(W, V, cap-W[i], i+1, cache))

  cache[cap][i] = ret
  return ret


if __name__ == '__main__':
  V = [60, 100, 120]
  W = [10, 20, 30]
  cap = 50
  n = len(V)
  cache = [[0] * (n+1) for _ in range(cap+1)]
  assert 220 == knapsack(W, V, cap, 0, cache)