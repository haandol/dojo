def solution(graph, start, visited=[]):
  Q = [start]

  while Q:
    node = Q.pop(0)
    if node not in visited:
      visited.append(node)

    for edge in graph[node]:
      if edge not in visited:
        Q.append(edge)

  return ''.join(visited)


G = {
  '0': ['1', '2'],
  '1': ['2'],
  '2': ['0', '3'],
  '3': ['3'],
}
assert '2031' == solution(G, '2', [])

G = {
  '1': ['2', '3'],
  '2': ['1', '4', '5'],
  '3': ['1', '5'],
  '4': ['2', '5', '6'],
  '5': ['3', '4', '6'],
  '6': ['4', '5'],
}
assert '123456' == solution(G, '1', [])
