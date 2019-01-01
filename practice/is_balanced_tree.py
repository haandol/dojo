class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val


def get_height(node):
  if not node:
    return 0
  return 1 + max(get_height(node.left), get_height(node.right))


def is_balanced(node):
  balance = abs(get_height(node.left) - get_height(node.right))
  return balance < 2


if __name__ == '__main__':
  root = Node(5)
  root.left = Node(3)
  root.right = Node(8)

  root.left.left = Node(3)
  root.left.right = Node(12)

  root.left.left.left = Node(2)

  assert 4 == get_height(root)
  assert False == is_balanced(root)

  root.left.left.left = None
  assert 3 == get_height(root)
  assert True == is_balanced(root)