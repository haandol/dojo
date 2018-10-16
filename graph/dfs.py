# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

def solution(graph, start, visited=[]):
  visited.append(start)

  for edge in graph[start]:
    if edge not in visited:
      solution(graph, edge, visited)    

  return visited


G = {
  0: [1, 2],
  1: [2],
  2: [0, 3],
  3: [3]
}
assert [2, 0, 1, 3] == solution(G, 2, [])
