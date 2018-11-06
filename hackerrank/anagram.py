# https://www.hackerrank.com/challenges/sherlock-and-anagrams

def get_substrings(s, l, n):
  words = []
  for i in range(n - l + 1):
    words.append((i, s[i:i+l]))
  return words

def get_words(s, n):
  words = []
  l = 1
  while l < n: 
    words.extend(get_substrings(s, l, n))
    l += 1
  return words

def solution(s):
  result = []
  n = len(s)
  words = get_words(s, n)
  for i, word in words:
    word_n = len(word)
    for j in range(i + 1, n - word_n + 1):
      if sorted(word) == sorted(s[j:j+word_n]):
        result.append((word, s[j:j+word_n]))
  return len(result)


if __name__ == '__main__':
  assert [(0, 'a'), (1, 'b'), (2, 'b'), (3, 'a')] == get_substrings('abba', 1, len('abba'))
  assert [(0, 'ab'), (1, 'bb'), (2, 'ba')] == get_substrings('abba', 2, len('abba'))
  assert [(0, 'abb'), (1, 'bba')] == get_substrings('abba', 3, len('abba'))
  print(solution('abba'))
  print(solution('kkkk'))
  print(solution('ifailuhkqq'))