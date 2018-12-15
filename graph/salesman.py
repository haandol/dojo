# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/amp/

def _travel(graph, path, visited, length, start) -> int:
  # return to start
  if len(path) == len(graph): return length + graph[path[-1]][start]

  ret = 99999999999999

  for node in graph:
    if visited.get(node, False):
      continue
    
    current = path[-1]
    path.append(node)
    visited[node] = True
    ret = min(ret, _travel(graph, path, visited, length + graph[current].get(node, 0), start))
    visited[node] = False
    path.pop()

  return ret



def travel(graph) -> int:
  start = 1
  path = [start]
  visited = {start: True}
  return _travel(graph, path, visited, 0, start)


if '__main__' == __name__:
  graph = {
    1: {
      2: 10,
      3: 15,
      4: 20
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
  print(travel(graph))
  assert 80 == travel(graph)
