# https://www.geeksforgeeks.org/quick-sort/

def sorted(arr, n):
  if not arr:
    return []

  pivot = arr[n]

  left = list(filter(lambda x: x < pivot, arr))
  mid = list(filter(lambda x: x == pivot, arr))
  right = list(filter(lambda x: x > pivot, arr))

  return sorted(left, len(left) - 1) + mid + sorted(right, len(right) - 1)


def partition(arr, low, high):
  pivot = arr[low]
  i = low + 1
  j = high

  while i <= j:
    if pivot <= arr[j]:
      j -= 1
    elif arr[i] <= pivot:
      i += 1
    else:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1

  arr[j], arr[low] = arr[low], arr[j] 
  return j 

def sort(arr, low, high):
  if high <= low:
    return

  pi = partition(arr, low, high)
  sort(arr, low, pi - 1)
  sort(arr, pi + 1, high)


if __name__ == '__main__':
  arr = [10, 7, 8, 9, 1, 5] 
  result = sorted(arr, len(arr) - 1)
  assert [1, 5, 7, 8, 9, 10] == result

  arr = [7, 1, 3, 2, 4, 5, 6]
  sort(arr, 0, len(arr) - 1)
  assert [1, 2, 3, 4, 5, 6, 7] == arr

  arr = [7, 6, 5, 4, 3, 2, 1]
  sort(arr, 0, len(arr) - 1)
  assert [1, 2, 3, 4, 5, 6, 7] == arr

  arr = [1, 2, 3, 4, 5, 6, 7]
  sort(arr, 0, len(arr) - 1)
  assert [1, 2, 3, 4, 5, 6, 7] == arr