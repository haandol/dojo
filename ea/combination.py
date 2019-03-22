def helper(arr, s, i, path):
    if s == len(path):
        print(sorted(path))
        return 

    n = len(arr)
    for j in range(i, n):
        helper(arr, s, j, path+[arr[j]])


def combine(arr, s):
  helper(arr, s, 0, ['F', 'M', 'D'])


combine(['F', 'M', 'D'], 4)
