# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

def solution(n):
  prime = [True for _ in range(n)]

  for i in range(2, 10):
    for j in range(2, int(n)):
      if n <= i * j:
        break
      prime[i * j] = False

  result = []
  for i in range(2, n):
    if prime[i]:
      result.append(i)
  
  return result


assert [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] == solution(50)