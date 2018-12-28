def match(p, s):
  pos = 0
  while pos < len(p) and pos < len(s) and (p[pos] == '?' or p[pos] == s[pos]):
    pos += 1

  if pos == len(p):
    return pos == len(s)
  
  if p[pos] == '*':
    for skip in range(len(s)-pos+1):
      if match(p[pos+1:], s[pos+skip:]):
        return True

  return False


if __name__ == '__main__':
  pattern = 'he?p'
  assert True == match(pattern, 'help')
  assert True == match(pattern, 'heap')
  assert False == match(pattern, 'helpp')

  pattern = '*p*'
  assert True == match(pattern, 'help')
  assert True == match(pattern, 'papa')
  assert False == match(pattern, 'hello')