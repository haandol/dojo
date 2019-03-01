# https://www.careercup.com/question?id=5738178221178880
# find subset S that min(S) + max(S) <= k


def solve(arr, k):
    n = len(arr)

    res = []
    for i in range(n**2):
        tmp = []
        for j in range(n):
            if 0 < i & (1 << j):
                tmp.append(arr[j])
        if tmp and min(tmp) + max(tmp) <= k:
            res.append(tmp)
    return res


print(solve([2, 4, 5, 7], 8))
