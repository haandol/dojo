# https://www.geeksforgeeks.org/bubble-sort/

def sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(1, n - i):
      if arr[j] < arr[j-1]:
        arr[j-1], arr[j] = arr[j], arr[j-1]


if __name__ == '__main__':
  arr = [10, 7, 8, 9, 1, 5] 
  sort(arr)
  assert [1, 5, 7, 8, 9, 10] == arr
