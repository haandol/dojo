from pprint import pprint


def helper(s, path, res):
  if not s:
    res.append(path[:])
    return

  n = len(s)
  for length in range(1, n+1):
    helper(s[length:], path+[s[:length]], res)


def solve(s):
  res = []
  helper(s, [], res)
  return res


pprint(solve('DDMF'))