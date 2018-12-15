def partition(arr, l, r):
  pivot = arr[r]
  i = l
  j = r - 1
<<<<<<< HEAD
=======

>>>>>>> 13d031344372357aeb6bef1ea890a123b428a5b9
  while i <= j:
    if pivot < arr[i] and arr[j] < pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j -= 1
    elif arr[i] <= pivot:
      i += 1
    elif pivot <= arr[j]:
      j -= 1

<<<<<<< HEAD
  arr[i], arr[r] = arr[r], arr[i]
=======
  arr[r], arr[i] = arr[i], arr[r]
>>>>>>> 13d031344372357aeb6bef1ea890a123b428a5b9
  return i


def _sort(arr, l, r):
  if r <= l:
    return
<<<<<<< HEAD

  pi = partition(arr, l, r)
  _sort(arr, l, pi - 1)
  _sort(arr, pi + 1, r)
=======
>>>>>>> 13d031344372357aeb6bef1ea890a123b428a5b9

  pi = partition(arr, l, r)

  _sort(arr, l, pi-1)
  _sort(arr, pi+1, r)
  

def sort(arr):
  _sort(arr, 0, len(arr) - 1)


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
