# https://www.geeksforgeeks.org/coin-change-dp-7/


def helper(arr, c, n):
    if c == 0:
        return 1
    if c < 0:
        return 0
    if n < 0:
        return 0
    return helper(arr, c, n-1) + helper(arr, c-arr[n], n)


def solve(arr, c):
    n = len(arr)
    dp = [
        [0] * (c+1)
        for _ in range(n+1)
    ]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, c+1):
            dp[i][j] = dp[i-1][j]
            if 0 <= j-arr[i-1]:
                dp[i][j] += dp[i][j-arr[i-1]]

    return dp[n][c]


assert 4 == solve([1, 2, 3], 4)
assert 2 == solve([1, 5, 10], 8)
assert 4 == solve([1, 5, 10], 10)
