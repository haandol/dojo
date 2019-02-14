def partition(arr, l, r):
  pivot = arr[r]
  i = l
  for j in range(l, r):
    if arr[j] <= pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1

  arr[r], arr[i] = arr[i], arr[r]
  return i


def sort(arr, l, r):
  if l < r:
    pi = partition(arr, l, r)
    sort(arr, l, pi - 1)
    sort(arr, pi + 1, r)


L = [7, 5, 3, 1, 0, 9, 2, 4]
sort(L, 0, len(L)-1)
print(L)