def sort(arr):
  n = len(arr)
  data = [0] * (max(arr) + 1)

  for i in range(n):
    data[arr[i]] += 1

  for i in range(len(data) - 1):
    data[i+1] += data[i]

  result = [-1] * n
  for i in range(n - 1, -1, -1):
    result[data[arr[i]] - 1] = arr[i]
    data[arr[i]] -= 1
  
  return result


if __name__ == '__main__':
  arr = [10, 7, 8, 9, 1, 5] 
  assert [1, 5, 7, 8, 9, 10] == sort(arr)
