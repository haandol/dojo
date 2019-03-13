def helper(arr, k, path):
    if k == len(path):
        print(path)
        return

    for i in range(len(arr)):
        helper(arr[:i]+arr[i+1:], k, path+[arr[i]])


def solve(arr, k):
    helper(arr, k, [])


L = [1, 2, 3]
print(solve(L, 2))
