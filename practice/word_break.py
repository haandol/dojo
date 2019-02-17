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
    n = len(s)
    dp = [False] * (n+1)

    for i in range(n+1):
        for j in range(1, n+1):
            if s[i:j] in D:
                if i == 0 or dp[j-(j-i)]:
                    dp[j] = True

    return dp[n]


D = [
    'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream',
    'icecream', 'man', 'go', 'mango'
]
print(solve(sorted(D, key=lambda x: len(x), reverse=True), 'ilikesamsung'))
print(solve(sorted(D, key=lambda x: len(x), reverse=True), 'ilikemangoice'))
