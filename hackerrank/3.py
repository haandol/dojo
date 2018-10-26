# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c):
  i = 0
  n = len(c)
  steps = 0
  while i < n:
    if i + 2 < n and c[i+2] == 0:
      i += 2
    else:
      i += 1
    steps += 1
    
  return steps - 1