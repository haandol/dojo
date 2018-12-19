# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

def get_lps(pat):
  m = len(pat)
  lps = [0] * m

  length = 0
  i = 1

  while i < m:
    if pat[i] == pat[length]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length != 0:
        length = lps[length - 1]
      else:
        lps[i] = 0
        i += 1

  return lps


def find(text, pat):
  res = []
  lps = get_lps(pat)

  i = 0
  j = 0
  n = len(text)
  m = len(pat)

  while i < n:
    if text[i] == pat[j]:
      i += 1
      j += 1
      if j == m:
        res.append(i)
        j = lps[j - 1] 
    else:
      if j != 0:
        j = lps[j-1]
      else:
        i += 1

  return res


if __name__ == '__main__':
  text = 'THIS IS A TEST TEXT'
  pat = 'TEST'
  [10] == find(text, pat)

  text = 'AABAACAADAABAABA'
  pat = 'AABA'
  [0, 9, 12] == find(text, pat)