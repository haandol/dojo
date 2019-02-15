def helper(s1, s2, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if s1[m] == s2[n]:
        return helper(s1, s2, m-1, n-1)
    else:
        return 1 + min(
            helper(s1, s2, m, n-1),
            helper(s1, s2, m-1, n),
            helper(s1, s2, m-1, n-1)
        )


def solve(s1, s2):
    return helper(s1, s2, len(s1)-1, len(s2)-1)


assert 1 == solve('geek', 'gesek')
assert 1 == solve('cat', 'cut')
assert 3 == solve('sunday', 'saturday')
