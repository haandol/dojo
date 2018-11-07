# https://www.hackerrank.com/challenges/minimum-swaps-2/

def minimumSwaps(arr):
  table = [None] * (max(arr) + 1)
  for i, el in enumerate(arr):
    table[el] = i

  sorted_arr = sorted(arr)

  count = 0
  n = len(arr)
  for i in range(n):
    if arr[i] != sorted_arr[i]:
      j = table[sorted_arr[i]]
      arr[i], arr[j] = arr[j], arr[i]
      table[arr[i]], table[arr[j]] = table[arr[j]], table[arr[i]]
      count += 1

  return count


if __name__ == '__main__':
  arr = [4, 3, 1, 2]
  assert 3 == minimumSwaps(arr)
  arr = [2, 3, 4, 1, 5]
  assert 3 == minimumSwaps(arr)
  arr = [1, 3, 5, 2, 4, 6, 8]
  assert 3 == minimumSwaps(arr)
  arr = [7, 1, 3, 2, 4, 5, 6]
  assert 5 == minimumSwaps(arr)