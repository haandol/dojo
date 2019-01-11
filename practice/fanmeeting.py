def solve(members, fans, m, n):
  count = 0
  k = 0
  while k <= n-m:
    i = 0
    j = k
    matched = True
    while i < m:
      if members[i] == 'M' and fans[j] == 'M':
        matched = False
        break
      i += 1
      j += 1
    if matched:
      count += 1 

    k += 1
  
  return count


if __name__ == '__main__':
  members = 'FFFMMM'
  fans = 'MMMFFF'
  assert 1 == solve(members, fans, len(members), len(fans))

  members = 'FFFFF'
  fans = 'FFFFFFFFFF'
  assert 6 == solve(members, fans, len(members), len(fans))

  members = 'FFFFM'
  fans = 'FFFFFMMMMF'
  assert 2 == solve(members, fans, len(members), len(fans))

  members = 'MFMFMFFFMMMFMF'
  fans = 'MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF'
  assert 2 == solve(members, fans, len(members), len(fans))