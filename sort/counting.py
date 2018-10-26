# https://www.geeksforgeeks.org/counting-sort/

def sort(arr):
  n = len(arr)
  result = [-1] * n
  counts = [0] * (max(arr) + 1)

  for el in arr:
    counts[el] += 1
  
  for i in range(1, len(counts)):
    counts[i] += counts[i-1]

  for i in range(n):
    result[counts[arr[i]] - 1] = arr[i]
    counts[arr[i]] -= 1

  return result


if __name__ == '__main__':
  arr = [10, 7, 8, 9, 1, 5] 
  assert [1, 5, 7, 8, 9, 10] == sort(arr)
