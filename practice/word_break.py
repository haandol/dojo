def helper(D, s, i):
    if not s:
        return True
    if i == len(D):
        return False

    for i in range(i, len(D)):
        if helper(D, s.replace(D[i], '', 1), i+1):
            return True
    return False


def solve(D, s):
    return helper(D, s, 0)


D = [
    'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream',
    'man', 'go', 'mango'
]
print(solve(D, 'ilikesamsung'))
