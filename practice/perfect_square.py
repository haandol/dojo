def solve(n):
  dp = [i for i in range(n+1)]
  squares = [
    i ** 2
    for i in range(1, n)
    if i ** 2 < n
  ]

  for i in range(1, n+1):
    for square in squares:
      if 0 <= i - square:
        dp[i] = min(dp[i], 1 + dp[i-square])

  return dp[n]

print(solve(8))