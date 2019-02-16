def helper(s1, s2, m, n):
    if m < 0 or n < 0:
        return 0

    if s1[m] == s2[n]:
        return 1 + helper(s1, s2, m-1, n-1)
    else:
        return max(
            helper(s1, s2, m-1, n),
            helper(s1, s2, m, n-1)
        )


def solve(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [
        [0] * (n+1)
        for _ in range(m+1)
    ]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[m][n]


assert 2 == solve('ABCT', 'AECK')
assert 2 == solve('GEEK', 'EKE')
