# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

from heapq import heappush, heappop


def solution(graph, start=0):
  heap = []
  queue = [start]
  visited = []
  W = 0

  while queue:
    node = queue.pop(0)
    visited.append(node)

    for edge, weight in graph[node].items():
      heappush(heap, (weight, edge))

    while heap:
      weight, edge = heappop(heap) 
      if edge not in visited:
        queue.append(edge)
        W += weight
        break

  print(visited)
  return W

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
