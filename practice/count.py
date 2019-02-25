def bisect_left(arr, x, lo, hi):
    if lo < 0:
        return -1

    while lo < hi:
        mid = (lo+hi)//2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(arr, x, lo, hi):
    if lo < 0:
        return -1

    while lo < hi:
        mid = (lo+hi)//2
        if x < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def count(arr, n):
    lo = bisect_left(arr, n, 0, len(arr))
    hi = bisect_right(arr, n, 0, len(arr))
    return hi-lo


print(count([1, 2, 3, 3, 4, 5], 3))
