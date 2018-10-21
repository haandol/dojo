# https://www.geeksforgeeks.org/power-set/amp/

def powerset(arr, n):
  n = pow(2, n)

  for i in range(n):
    for j in range(n):
      if 0 < (i & (1 << j)):
        print(arr[j], end='')
    print()


arr = ['a', 'b', 'c']
powerset(arr, 3); 