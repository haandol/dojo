# https://www.geeksforgeeks.org/coin-change-dp-7/


def helper(S, C, n):
    if C == 0:
        return 1
    if C < 0:
        return 0
    if n < 0:
        return 0
    return helper(S, C, n-1) + helper(S, C-S[n], n)


def solve(S, C):
    return helper(S, C, len(S)-1)


print(solve([1, 2, 3], 4))
