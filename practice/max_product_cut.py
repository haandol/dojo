def helper(n):
    if n < 2:
        return 1

    max_so_far = 0
    for i in range(1, n):
        max_so_far = max([max_so_far, i * (n-i), i * helper(n-i)])
    return max_so_far


def solve(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(1, n+1):
        max_so_far = dp[i]
        for j in range(1, i):
            max_so_far = max([max_so_far, j * dp[i-j], j * (i-j)])
        dp[i] = max_so_far

    return dp[n]


assert 1 == solve(1)
assert 1 == solve(2)
assert 2 == solve(3)
assert 4 == solve(4)
assert 6 == solve(5)
assert 36 == solve(10)
