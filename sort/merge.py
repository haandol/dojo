# https://www.geeksforgeeks.org/merge-sort/

def sort(arr, l, h):
  if h - l < 1:
    return

  m = int((l + h) / 2)

  sort(arr, l, m)
  sort(arr, m + 1, h)
  merge(arr, l, m, h)


def merge(arr, l, m, h):
  L = [0] * (m - l + 1)
  R = [0] * (h - m)

  for i in range(len(L)):
    L[i] = arr[l + i]

  for i in range(len(R)):
    R[i] = arr[m + i + 1]

  i = 0
  j = 0
  k = l
  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  for p in range(i, len(L)):
    arr[k] = L[p]
    k += 1

  for p in range(j, len(R)):
    arr[k] = R[p]
    k += 1


if __name__ == '__main__':
  arr = [12, 11, 13, 5, 6, 7]
  n = len(arr) - 1
  sort(arr, 0, n)
  print(arr)
  assert [5, 6, 7, 11, 12, 13] == arr