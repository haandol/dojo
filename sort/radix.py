# https://www.geeksforgeeks.org/radix-sort/

def counting_sort(arr, base):
  n = len(arr)
  result = [0] * n
  counts = [0] * 10

  for i in range(n):
    index = int(arr[i] / base) % 10
    counts[index] += 1

  for i in range(1, 10):
    counts[i] += counts[i-1]

  for i in range(n):
    index = int(arr[i] / base) % 10
    result[counts[index]-1] = arr[i]
    counts[index] -= 1

  for i in range(n):
    arr[i] = result[i]


def sort(arr):
  val = max(arr)
  i = 1
  while 0 < int(val / i):
    counting_sort(arr, i)
    i *= 10 


if __name__ == '__main__':
  arr = [170, 45, 75, 90, 802, 24, 2, 66] 
  sort(arr)
  print(arr)
  