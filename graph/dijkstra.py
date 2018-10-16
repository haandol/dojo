# https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/
# using dictionary makes O(V+E)

def solution(graph, start):
  prev = { k: None for k in graph }
  dist = { k: float('inf') for k in graph }
  visited = []
  dist[start] = 0
  queue = [start]

  while queue:
    node = queue.pop(0)
    visited.append(node)

    for edge, weight in graph[node].items():
      if edge not in visited:
        if edge not in queue:
          queue.append(edge)
        alt = dist[node] + weight
        if alt < dist[edge]:
          dist[edge] = alt
          prev[edge] = node

  return prev, dist

G = {
  0: {
    1: 4,
    7: 8
  },
  1: {
    0: 4,
    2: 8,
    7: 11
  },
  2: {
    1: 8,
    3: 7,
    8: 2
  },
  3: {
    2: 7,
    4: 9,
    5: 14
  },
  4: {
    3: 9,
    5: 10
  },
  5: {
    2: 4,
    3: 14,
    4: 10,
    6: 2
  },
  6: {
    5: 2,
    7: 1,
    8: 6
  },
  7: {
    0: 8,
    1: 11,
    6: 1
  },
  8: {
    2: 2,
    6: 6,
    7: 7
  }
}

prev, dist = solution(G, 0)
assert sorted(dist.items(), key=lambda x: x[0]) == [
  (0, 0), (1, 4), (2, 12), (3, 19), (4, 21), (5, 11), (6, 9), (7, 8), (8, 14)
]

node = prev[4]
P = [4]
while node != None:
  P.insert(0, node)
  node = prev[node]
assert [0, 7, 6, 5, 4] == P