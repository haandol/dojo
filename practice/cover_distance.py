def solve(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return solve(n-1) + solve(n-2) + solve(n-3)


print(solve(4))
