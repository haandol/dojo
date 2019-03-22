# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0


def helper(arr, lo, hi, s, lohisum):
    if s == lohisum:
        return (lo+1, hi+1)
    if lohisum < s:
        return (-1, -1)
    if hi < lo:
        return (-1, -1)

    res = helper(arr, lo, hi-1, s, lohisum-arr[hi])
    if res[0] < 0:
        res = helper(arr, lo+1, hi, s, lohisum-arr[lo])
    return res


def subarray_sum(arr, s):
    res = helper(arr, 0, len(arr)-1, s, sum(arr))
    if res[0] < 0:
        return -1
    return res


assert (2, 4) == subarray_sum([1, 2, 3, 7, 5], 12)
assert (1, 5) == subarray_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)