# https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/


directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]


def helper(matrix, row, col):
    n = len(matrix)
    res = 1
    for y, x in directions:
        dy = row + y
        dx = col + x
        if dy < 0 or dx < 0 or n <= dy or n <= dx:
            continue
        if matrix[dy][dx] == matrix[row][col] + 1:
            res = max(res, 1 + helper(matrix, dy, dx))
    return res


def helper_dp(matrix, i, j, dp):
    n = len(matrix)
    if -1 < dp[i][j]:
        return dp[i][j]

    for y, x in directions:
        dy = i + y
        dx = j + x
        if dy < 0 or dx < 0 or n <= dy or n <= dx:
            continue
        if matrix[dy][dx] == matrix[i][j] + 1:
            dp[i][j] = 1 + helper_dp(matrix, dy, dx, dp)
            return dp[i][j]
    dp[i][j] = 1
    return dp[i][j]


def solve(matrix):
    n = len(matrix)
    dp = [
        [-1] * n
        for _ in range(n)
    ]
    res = 1
    for i in range(n):
        for j in range(n):
            helper_dp(matrix, i, j, dp)
            res = max(res, dp[i][j])
    return res


matrix = [
    [1, 1],
    [1, 1]
]
assert 1 == solve(matrix)

matrix = [
    [1, 2, 9],
    [5, 3, 8],
    [4, 6, 7]
]
assert 4 == solve(matrix)

matrix = [
    [1, 2, 9, 10],
    [3, 5, 8, 8],
    [9, 4, 7, 6],
    [1, 2, 4, 5]
]
assert 7 == solve(matrix)
