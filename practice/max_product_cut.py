def helper(n):
    if n < 2:
        return 1

    max_so_far = 0
    for i in range(1, n):
        max_so_far = max([max_so_far, i * (n-i), i * helper(n-i)])
    return max_so_far


def solve(n):
    return helper(n)


assert 1 == solve(0)
assert 1 == solve(1)
assert 1 == solve(2)
assert 2 == solve(3)
assert 4 == solve(4)
assert 6 == solve(5)
assert 36 == solve(10)
