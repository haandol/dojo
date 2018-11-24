def partition(arr, l, r):
  pi = r
  pivot = arr[pi]

  r -= 1
  while l <= r:
    if pivot < arr[l] and arr[r] < pivot:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
    elif arr[l] <= pivot:
      l += 1
    elif pivot <= arr[r]:
      r -= 1
  
  arr[pi], arr[l] = arr[l], arr[pi]
  return l


def qsort(arr, l, r):
  if l < r:
    pi = partition(arr, l, r)
    qsort(arr, l, pi - 1)
    qsort(arr, pi + 1, r)


def sort(arr):
  qsort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
  arr = [7, 1, 3, 2, 4, 5, 6]
  sort(arr)
  assert [1, 2, 3, 4, 5, 6, 7] == arr

  arr = [7, 6, 5, 4, 3, 2, 1]
  sort(arr)
  assert [1, 2, 3, 4, 5, 6, 7] == arr

  arr = [1, 2, 3, 4, 5, 6, 7]
  sort(arr)
  assert [1, 2, 3, 4, 5, 6, 7] == arr

  arr = [1, 1, 5, 4, 3, 2, 1]
  sort(arr)
  assert [1, 1, 1, 2, 3, 4, 5] == arr
