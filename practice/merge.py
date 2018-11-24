def _merge(arr, l, m, r):
  tmp = []
  i = l
  j = m + 1
  while i <= m and j <= r:
    if arr[i] <= arr[j]:
      tmp.append(arr[i])
      i += 1
    else:
      tmp.append(arr[j])
      j += 1
  
  for k in range(i, m+1):
    tmp.append(arr[k])
  for k in range(j, r+1):
    tmp.append(arr[k])

  for i, el in enumerate(tmp):
    arr[l+i] = el


def _sort(arr, l, r):
  if l < r:
    m = int((l + r) / 2)
    _sort(arr, l, m)
    _sort(arr, m + 1, r)
    _merge(arr, l, m, r)


def sort(arr):
  n = len(arr) - 1
  _sort(arr, 0, n)


if __name__ == '__main__':
  arr = [38, 27, 43, 3, 9, 82, 10]
  sort(arr)
  assert [3, 9, 10, 27, 38, 43, 82] == arr

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
