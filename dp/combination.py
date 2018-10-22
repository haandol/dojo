# https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/

def combine(arr, n, r):
  _combine(arr, n, r, [None] * r, 0, 0)


def _combine(arr, n, r, data, index, i):
  if index == r:
    print(data)
    return

  if n <= i:
    return
  
  data[index] = arr[i]
  _combine(arr, n, r, data, index + 1, i + 1)
  _combine(arr, n, r, data, index, i + 1)


arr = ['A', 'B', 'C', 'D', 'E']
combine(arr, len(arr), 3)