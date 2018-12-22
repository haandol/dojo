# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

def get_lps(pat):
  n = len(pat)
  lps = [0] * n    # longest proper prefix which is also suffix
  i = 1
  l = 0
  while i < n:
    if pat[i] == pat[l]:
      l += 1
      lps[i] = l
      i += 1
    else:
      if 0 < l:
        l = lps[l-1]
      else:
        i += 1

  return lps

def find(text, pat):
  res = []
  n = len(text)
  m = len(pat)

  i = 0
  l = 0
  lps = get_lps(pat)
  while i < n:
    if text[i] == pat[l]:
      i += 1
      l += 1
    else:
      if 0 < l:
        l = lps[l-1]
      else:
        i += 1

    if l == m:
      res.append(i-m)
      l = lps[l-1]

  return res


if __name__ == '__main__':
  text = 'THIS IS A TEST TEXT'
  pat = 'TEST'
  [10] == find(text, pat)

  text = 'AABAACAADAABAABA'
  pat = 'AABA'
  [0, 9, 12] == find(text, pat)

  assert [0, 1, 2, 3]== get_lps('AAAA')
  assert [0, 1, 2, 0]== get_lps('AAAB')
  assert [0, 1, 0, 1]== get_lps('AABA')
  assert [0, 0, 1, 2]== get_lps('ABAB')
  assert [0, 1, 0, 1, 2] == get_lps('AACAA')