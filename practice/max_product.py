def max_product(arr, i, n, res):
    if n == 0:
        return res

    max_so_far = 0
    for j in range(i, len(arr)):
        max_so_far = max(max_so_far, max_product(arr, j+1, n-1, res*arr[j]))
    return max_so_far

print(max_product([1, 2, 3], 0, 2, 1))