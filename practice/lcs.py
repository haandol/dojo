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
    return helper(s1, s2, m-1, n-1)


assert 2 == solve('ABCT', 'AECK')
assert 2 == solve('GEEK', 'EKE')
