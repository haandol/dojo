from pprint import pprint


def helper(s, path, k, res):
  if not s:
    for item in path:
      if k == len(item):
        res.insert(0, path[:])
        return

    res.append(path[:])
    return

  n = len(s)

  for length in range(1, n+1):
    helper(s[length:], path+[s[:length]], k, res)


def solve(s, k):
  res = []
  helper(s, [], k, res)
  return res


pprint(solve('TJMAS', 2))