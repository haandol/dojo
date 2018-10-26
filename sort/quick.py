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
  i = high
  pivot = arr[high]
  high -= 1

  while low <= high:
    if pivot < arr[low]:
      if arr[high] < pivot:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
      else:
        high -= 1
    else:
      low += 1

  arr[i], arr[low] = arr[low], arr[i]
  return low


def sort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)

    sort(arr, low, pi - 1)
    sort(arr, pi + 1, high)


if __name__ == '__main__':
  arr = [10, 7, 8, 9, 1, 5] 
  result = sorted(arr, len(arr) - 1)
  assert [1, 5, 7, 8, 9, 10] == result

  sort(arr, 0, len(arr) - 1)
  assert [1, 5, 7, 8, 9, 10] == arr