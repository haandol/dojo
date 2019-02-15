def eggdrop(e, f):
    dp = [
        [0] * (f+1)
        for _ in range(e+1)
    ]

    for i in range(e+1):
        dp[i][0] = 0
        dp[i][1] = 0

    for i in range(1, f+1):
        dp[1][i] = i

    for i in range(2, e+1):
        for j in range(2, f+1):
            dp[i][j] = float('inf')
            for k in range(1, j):
                res = 1 + max(dp[i-1][k-1], dp[i][j-k])
                dp[i][j] = min(dp[i][j], res)

    return dp[e][f]


if __name__ == '__main__':
    print(eggdrop(2, 10))
    print(eggdrop(2, 36))