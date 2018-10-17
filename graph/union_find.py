# https://www.geeksforgeeks.org/union-find/

def union(parent, p1, p2):
  parent[p1] = p2

def find(parent, node):
  if parent[node] == -1:
    return node
  return find(parent, parent[node])

def is_cyclic(graph):
  parent = { k: -1 for k in graph }

  for node in graph:
    for edge in graph[node]:
      p1 = find(parent, node)
      p2 = find(parent, edge)
      if p1 == p2:
        return True
      union(parent, p1, p2)

  return False



G = {
  0: [1],
  1: [2],
  2: [0],
}
assert True == is_cyclic(G)

G = {
  0: [1],
  1: [2],
  2: [],
}
assert False == is_cyclic(G)