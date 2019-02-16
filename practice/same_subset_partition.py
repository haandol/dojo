def helper(arr, n, s):
    if s == 0:
        return True
    if n == 0:
        return False

    return helper(arr, n-1, s-arr[n-1]) or helper(arr, n-1, s)


def solve(arr):
    n = len(arr)
    s = sum(arr)
    if s % 2 == 1:
        return False

    return helper(arr, n, sum(arr) // 2)


assert solve([1, 5, 11, 5])
assert not solve([1, 5, 3])
