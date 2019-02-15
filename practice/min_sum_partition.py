# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/


def helper(arr, n, path, s):
    if n == 0:
        return abs((s - path) - path)

    return min(
        helper(arr, n-1, path+arr[n], s),
        helper(arr, n-1, path, s)
    )


def solve(arr):
    n = len(arr)
    s = sum(arr)
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
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]

    diff = float('inf')
    for j in range(s//2, -1, -1):
        if dp[n][j]:
            diff = s - 2*j
            break

    return diff


assert 1 == solve([1, 6, 11, 5])
assert 1 == solve([3, 1, 4, 2, 2, 1])
