def _travel(graph, path, visited, start, weight):
  if len(path) == len(graph):
    return weight + graph[path[-1]][start]

  ret = float('inf')
  for node in graph:
    if node in visited:
      continue

    prev = path[-1]
    path.append(node)
    visited.append(node)
    ret = min(ret, _travel(graph, path, visited, start, weight + graph[prev][node]))
    path.pop()
    visited.pop()

  return ret


def travel(graph, start):
  path = [start]
  visited = [start]
  return _travel(graph, path, visited, start, 0)


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
  assert 80 == travel(graph, 1)