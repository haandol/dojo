def helper(arr, n, s):
    if s == 0:
        return True
    if n == 0:
        return False
    if s < arr[n-1]:
        return helper(arr, n-1, s)
    return helper(arr, n-1, s-arr[n-1]) or helper(arr, n-1, s)


def solve(arr, s):
    return helper(arr, len(arr), s)


assert solve([3, 34, 4, 12, 5, 2], 9)
assert solve([3, 34, 4, 12, 5, 2], 7)
assert not solve([3, 4, 12, 2], 8)
