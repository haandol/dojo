def search(arr, l, h, val):
  if h < l:
    return -1

  m = int(l + (h - l) / 2)

  if val < arr[m]:
    return search(arr, l, m - 1, val)
  elif arr[m] < val:
    return search(arr, m + 1, h, val)
  return m


arr = [ 2, 3, 4, 10, 40 ] 
assert 3 == search(arr, 0, len(arr) - 1, 10)
