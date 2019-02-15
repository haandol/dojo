# https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/


def helper(matrix, row, col):
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]
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


def solve(matrix):
    n = len(matrix)
    res = 0
    for row in range(n):
        for col in range(n):
            res = max(res, helper(matrix, row, col))
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
