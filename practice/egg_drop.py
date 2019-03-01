# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/


def helper(n, f):
    if f < 2:
        return f
    if n == 1:
        return f

    min_so_far = float('inf')
    for i in range(1, f+1):
        min_so_far = min(min_so_far, max(helper(n-1, i-1), helper(n, f-i)))
    return 1 + min_so_far


def solve(n, f):
    return helper(n, f)


print(solve(2, 10))
