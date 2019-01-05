# https://www.geeksforgeeks.org/power-set/amp/

def powerset(arr, n):
  size = 2 ** n

  for i in range(size):
    for j in range(n):
      if i & (1 << j) > 0:
        print(arr[j], end='')
    print()


arr = ['A', 'B', 'C']
powerset(arr, 3); 