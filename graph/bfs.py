def solution(graph, start, visited=[]):
  visited.append(start)
  for edge in graph[start]:
    if edge not in visited:
      solution(graph, edge, visited)
  return ''.join(visited)

G = {
  '0': ['1', '2'],
  '1': ['2'],
  '2': ['0', '3'],
  '3': ['3'],
}
assert '2013' == solution(G, '2', [])

G = {
  'A': ['B', 'C'],
  'B': ['A', 'D', 'E'],
  'C': ['A', 'E'],
  'D': ['B', 'E', 'F'],
  'E': ['B', 'C', 'D'],
  'F': ['D', 'E'],
}
assert 'ABDECF' == solution(G, 'A', [])
