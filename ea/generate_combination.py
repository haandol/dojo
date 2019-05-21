from pprint import pprint


def helper(s, i, path, res):
  if i == len(s):
    res.append(sorted(path))
    return

  helper(s, i+1, path+[s[i]], res)
  for j in range(len(path)):
    helper(s, i+1, path[:j]+[path[j]+s[i]]+path[j+1:], res)


def solve(s):
  res = list()
  helper(s, 1, [s[0]], res)
  return sorted(res)


pprint(solve('DDFM'))