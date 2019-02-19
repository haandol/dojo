def helper(P, n):
    if n == 0:
        return 0
    if n == 1:
        return P[0]

    res = 0
    for i in range(n):
        res = max(res, P[i] + helper(P, n-i-1))
    return res


def solve(P):
    n = len(P)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        max_so_far = 0
        for j in range(i):
            max_so_far = max(max_so_far, P[j] + dp[i-j-1])
        dp[i] = max_so_far

    return dp[n]


print(solve([1, 5, 8, 9, 10, 17, 17, 20]))
