# https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/

class Node:
  left = None
  right = None

  def __init__(self, val):
    self.val = val


def solve(node, val1, val2):
  if not node.left or not node.right:
    return node.val

  if val1 < node.val and val2 < node.val:
    return solve(node.left, val1, val2)
  elif node.val < val1 and node.val < val2:
    return solve(node.right, val1, val2)
  else:
    return node.val


if __name__ == '__main__':
  root = Node(20)
  root.left = Node(8)
  root.right = Node(22)

  root.left.left = Node(4)
  root.left.right = Node(12)

  root.left.right.left = Node(10)
  root.left.right.right = Node(14)

  assert 12 == solve(root, 10, 14)
  assert 8 == solve(root, 14, 8)
  assert 20 == solve(root, 10, 22)