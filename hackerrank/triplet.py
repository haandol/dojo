# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def countTriplets(arr, r):
  n = len(arr)
  count = 0

  D = {}
  for el in arr:
    if el in D:
      continue

    v = el
    c = 0
    while 0 < el:
      el = int(el / r)
      c += 1
    D[v] = c
  
  for i1 in range(n):
    v1 = D[arr[i1]]
    for i2 in range(i1+1, n):
      v2 = D[arr[i2]]
      for i3 in range(i2+1, n):
        v3 = D[arr[i3]]
        if v1 + 2 == v2 + 1 == v3:
          count += 1

  return count


if __name__ == '__main__':
  arr = [1, 2, 2, 4]
  assert 2 == countTriplets(arr, 2)

  arr = [1, 3, 9, 9, 27, 81]
  assert 6 == countTriplets(arr, 3)

  arr = [1, 5, 5, 25, 125]
  assert 4 == countTriplets(arr, 5)