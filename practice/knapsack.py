def helper(W, V, cap, i, v):
    if cap == 0:
        return v
    if i < 0:
        return 0

    if cap < W[i]:
        return helper(W, V, cap, i-1, v)

    return max(
        helper(W, V, cap - W[i], i-1, v + V[i]),
        helper(W, V, cap, i-1, v)
    )


def solve(W, V, cap):
    n = len(W)
    dp = [
        [0] * (cap+1)
        for _ in range(n+1)
    ]

    for i in range(1, n+1):
        for j in range(1, cap+1):
            if j < W[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i-1]] + V[i-1])
    
    return dp[n][cap]


assert 220 == solve([10, 20, 30], [60, 100, 120], 50)
assert 11 == solve([1, 3, 4, 5], [1, 4, 5, 7], 8)
