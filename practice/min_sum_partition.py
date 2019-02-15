def helper(arr, path, res, s):
    if s - sum(path) < 0:
        res.append(abs(s - sum(path)))
        return

    for i in range(len(arr)):
        helper(arr[:i]+arr[i+1:], path + [arr[i]], res, s-arr[i])


def solve(arr):
    res = []
    helper(arr, [], res, sum(arr))
    return min(res)


assert 1 == solve([1, 6, 11, 5])
