def solution(graph, start):
  Q = [start]
  P = { k: None for k in graph }
  W = { k: float('inf') for k in graph }
  W[start] = 0
  visited = []

  while Q:
    node = Q.pop(0)
    if node not in visited:
      visited.append(node)

    for edge, weight in graph[node]:
      if edge not in visited:
        Q.append(edge)
        alt = W[node] + weight
        if alt < W[edge]:
          W[edge] = alt
          P[edge] = node

  return P, W


G = {
  '0': [
    ('1', 4),
    ('7', 8),
  ],
  '1': {
    ('0', 4),
    ('2', 8),
    ('7', 11),
  },
  '2': [
    ('1', 8),
    ('3', 7),
    ('5', 4),
    ('8', 2),
  ],
  '3': [
    ('2', 7),
    ('4', 9),
    ('5', 14),
  ],
  '4': [
    ('3', 9),
    ('5', 10),
  ],
  '5': [
    ('2', 4),
    ('3', 14),
    ('4', 10),
    ('6', 2),
  ],
  '6': [
    ('5', 2),
    ('7', 1),
    ('8', 6),
  ],
  '7': [
    ('0', 8),
    ('1', 11),
    ('6', 1),
    ('8', 7),
  ],
  '8': [
    ('2', 2),
    ('6', 6),
    ('7', 7),
  ],
}

k = '0'
P, W = solution(G, k)
assert [('0', 0), ('1', 4), ('2', 12), ('3', 19), ('4', 21), ('5', 11), ('6', 9), ('7', 8), ('8', 14)] == \
       sorted(W.items(), key=lambda x: x[0])
