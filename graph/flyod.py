# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

def solution(graph):
  D = { s: {e: (0 if s == e else float('inf')) for e in graph} for s in graph }
  for s in G:
    for e in G[s]:
      D[s][e] = G[s][e]

  for m in graph:
    for s in graph:
      for e in graph:
        if D[s][m] + D[m][e] < D[s][e]:
          D[s][e] = D[s][m] + D[m][e]

  return D


G = {
  '0': {
    '1': 5,
    '3': 10,
  },
  '1': {
    '2': 3,
  },
  '2': {
    '3': 1,
  },
  '3': {
  }
}

print(sorted(solution(G).items(), key=lambda x: x[0]))