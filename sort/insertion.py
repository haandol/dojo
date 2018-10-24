def sort(arr):
  n = len(arr)
  for i in range(1, n):
    val = arr[i]
    j = i - 1
    while 0 <= j and val < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = val

arr = [12, 11, 13, 5, 6]
sort(arr)
assert [5, 6, 11, 12, 13] == arr
