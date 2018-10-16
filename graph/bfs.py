# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

def solution(graph, start):
  queue = []
  visited = []

  queue.append(start)

  while queue:
    node = queue.pop(0)
    visited.append(node)

    for edge in graph[node]:
      if edge not in visited and edge not in queue:
        queue.append(edge)

  return visited


G = {
  0: [1, 2],
  1: [2],
  2: [0, 3],
  3: [3]
}
assert [2, 0, 3, 1] == solution(G, 2)
