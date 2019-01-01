def _search(arr, l, r, val):
  if r < l:
    return -1

  m = int((l+r) / 2)
  if val < arr[m]:
    return _search(arr, l, m-1, val)
  elif arr[m] < val:
    return _search(arr, m+1, r, val)
  else:
    return m

def search(arr, val):
  return _search(arr, 0, len(arr)-1, val)


if __name__ == '__main__':
  arr = [1, 3, 5, 7, 9]
  assert 1 == search(arr, 3)
  assert 4 == search(arr, 9)
  assert -1 == search(arr, 2)

  arr = [1, 1, 1, 3, 5]
  assert 2 == search(arr, 1)