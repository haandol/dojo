def find_pivot(nums, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if nums[hi] < nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo


arr = [4, 5, 6, 7, 0, 1, 2, 3]
print(find_pivot(arr, 0, len(arr)-1))
