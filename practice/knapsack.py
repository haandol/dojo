# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapsack(W, V, cap, n):
  if n == 0:
    return 0

  if W[n-1] > cap:
    return knapsack(W, V, cap, n-1)
  else:
    return max(
      V[n-1] + knapsack(W, V, cap - W[n-1], n-1),
      knapsack(W, V, cap, n-1)
    )


if __name__ == '__main__':
  V = [60, 100, 120]
  W = [10, 20, 30]
  cap = 50
  n = len(V)
  assert 220 == knapsack(W, V, cap, n)