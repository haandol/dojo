def helper(arr, n, s):
    if s == 0:
        return True
    if n == 0:
        return False

    return helper(arr, n-1, s-arr[n-1]) or helper(arr, n-1, s)


def solve(arr):
    s = sum(arr)
    if s % 2 == 1:
        return False

    n = len(arr)
    dp = [
        [False] * (s//2+1)
        for _ in range(n+1)
    ]

    for i in range(n):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, s//2+1):
            if arr[i-1] == j:
                dp[i][j] = True
            elif j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]

    return dp[n][s//2]


assert solve([3, 1, 1, 2, 2, 1])
assert solve([1, 5, 11, 5])
assert not solve([1, 5, 3])
