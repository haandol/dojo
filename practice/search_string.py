def search(s, t):
  n = len(s)
  m = len(t)
  i = 0
  j = 0
  res = []
  while i < n:
    if s[i] == t[j]:
      i += 1
      j += 1
    else:
      i -= (j - 1)
      j = 0

    if j == m:
      res.append(i-m)
      i -= (j - 1)
      j = 0

  return res


if __name__ == '__main__':
  string = 'ABCABABCDEFAAAB'
  target = 'ABC'
  assert [0, 5] == search(string, target)

  string = 'AAAAAA'
  target = 'AAA'
  assert [0, 1, 2, 3] == search(string, target)