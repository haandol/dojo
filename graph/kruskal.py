# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

from heapq import heappush, heappop

def union(parent, p1, p2):
  parent[p1] = p2


def find(parent, node):
  while parent[node] != -1:
    node = parent[node]
  return node


def solution(graph, start=0):
  weight = 0
  edges = []
  visited = []
  for src in graph:
    edges.extend([(w, src, dest) for dest, w in list(graph[src].items())])
  edges.sort(key=lambda x: x[0])

  parent = { k: -1 for k in graph }
  while edges:
    w, src, dest = edges.pop(0)
    if dest in visited:
      continue
    visited.append(src)

    p1 = find(parent, src)
    p2 = find(parent, dest)
    if p1 == p2:
      continue
    
    union(parent, p1, p2)
    weight += w

  return weight

if __name__ == '__main__':
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
      5: 4,
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
      6: 1,
      8: 7
    },
    8: {
      2: 2,
      6: 6,
      7: 7
    }
  }
  assert 37 == solution(G)
