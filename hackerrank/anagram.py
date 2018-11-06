# https://www.hackerrank.com/challenges/sherlock-and-anagrams

def get_substrings(s, word_n, n):
  words = []
  for i in range(n - word_n + 1):
    words.append((i, word_n, sorted(s[i:i+word_n])))
  return words

def get_words(s, n):
  words = []
  word_n = 1
  while word_n < n: 
    words.extend(get_substrings(s, word_n, n))
    word_n += 1
  return words

def sherlockAndAnagrams(s):
  count = 0
  n = len(s)
  words = get_words(s, n)
  for i, word_n, word in words:
    for j in range(i + 1, n - word_n + 1):
      if word == sorted(s[j:j+word_n]):
        count += 1
  return count


if __name__ == '__main__':
  print(sherlockAndAnagrams('abba'))
  print(sherlockAndAnagrams('kkkk'))
  print(sherlockAndAnagrams('ifailuhkqq'))