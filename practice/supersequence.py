def helper(s1, s2, m, n, s):
    if m < 0 or n < 0:
        return s

    if s1[m] == s2[n]:
        return helper(s1, s2, m-1, n-1, s1[m]+s)
    else:
        res = helper(s1, s2, m-1, n, s)
        if len(res) < len(s):
            res = s
        res = helper(s1, s2, m, n-1, s)
        if len(res) < len(s):
            res = s
        return res


def solve(s1, s2):
    m = len(s1)
    n = len(s2)
    lcs = helper(s1, s2, m-1, n-1, '')
    print(lcs)
    res = []
    i, j = 0, 0
    for k in range(len(lcs)):
        while i < m:
            if s1[i] == lcs[k]:
                i += 1
                break
            res.append(s1[i])
            i += 1
        while j < n:
            if s2[j] == lcs[k]:
                j += 1
                break
            res.append(s2[j])
            j += 1
        res.append(lcs[k])

    while i < m:
        res.append(s1[i])
        i += 1

    while j < n:
        res.append(s2[j])
        j += 1

    return ''.join(res)


print(solve('geek', 'eke'))
print(solve('AGGTAB', 'GXTXAYB'))
