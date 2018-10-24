def sort(arr):
  n = len(arr)
  for i in range(1, n):
    val = arr[i]
    j = i
    while 0 < j:
      if val < arr[j-1]:
        arr[j] = arr[j-1]
        j -= 1
      else:
        break
    arr[j] = val

arr = [12, 11, 13, 5, 6]
sort(arr)
assert [5, 6, 11, 12, 13] == arr
