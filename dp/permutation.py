def permute(arr, i, n):
  if i == n-1:
    print(''.join(arr))
    return
    
  for j in range(i, n):
    arr[i], arr[j] = arr[j], arr[i]
    permute(arr, i+1, n)
    arr[i], arr[j] = arr[j], arr[i]


arr = 'ABC'
permute(list(arr), 0, len(arr))