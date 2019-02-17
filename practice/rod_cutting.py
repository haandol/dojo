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
    return helper(P, n)


print(solve([1, 5, 8, 9, 10, 17, 17, 20]))
