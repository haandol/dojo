# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

def solution(graph):
  dist = {
    sk: {
      ek: graph[sk].get(ek, float('inf')) for ek in graph
    } for sk in graph
  }

  for k in graph:
    dist[k][k] = 0

  for m in graph:
    for s in graph:
      for e in graph:
        dist[s][e] = min(dist[s][e], dist[s][m] + dist[m][e])

  return dist


G = {
  0: {
    1: 5,
    3: 10
  },
  1: {
    2: 3
  },
  2: {
    3: 1
  },
  3: {
  }
}

dist = solution(G)
for k in dist:
  print(sorted(dist[k].items(), key=lambda x: x[0]))
