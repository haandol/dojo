def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot <= arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def sort(arr, lo, hi):
    if lo < hi:
        pi = partition(arr, lo, hi)

        sort(arr, lo, pi-1)
        sort(arr, pi+1, hi)


L = [7, 5, 3, 1, 0, 9, 2, 4]
sort(L, 0, len(L)-1)
print(L)
