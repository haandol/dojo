def helper(arr, n, s):
    if s == 0:
        return True
    if n == 0:
        return False
    if s < arr[n-1]:
        return helper(arr, n-1, s)
    return helper(arr, n-1, s-arr[n-1]) or helper(arr, n-1, s)


def solve(arr, s):
    n = len(arr)
    dp = [
        [False] * (s+1)
        for _ in range(n+1)
    ]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, s+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(1, s+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[n][s]


assert solve([3, 34, 4, 12, 5, 2], 9)
assert solve([3, 34, 4, 12, 5, 2], 7)
assert not solve([3, 4, 12, 2], 8)
