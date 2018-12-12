# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/amp/
import math


def _travel(graph, path, visited, length) -> int:
  ret = math.inf
  for node in graph:
    if visited.get(node, False):
      continue
    
    current = path[-1]
    path.append(node)
    visited[node] = True
    ret = _travel(graph, path, visited, min(ret, length + graph[current][node]))
    visited[node] = False
    path.pop()

  return ret



def travel(graph) -> int:
  path = [1]
  visited = {1: True}
  return _travel(graph, path, visited, 0)


if '__main__' == __name__:
  graph = {
    1: {
      2: 10,
      3: 15
    },
    2: {
      1: 10,
      3: 35,
      4: 25
    },
    3: {
      1: 15,
      2: 35,
      4: 30
    },
    4: {
      1: 20,
      2: 25,
      3: 30
    }
  }
  assert 80 == travel(graph)
