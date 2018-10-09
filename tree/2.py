# https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/


class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def solution(node, isRoot=False):
  if node.left is None and node.right is None:
    return node.value

  if node.left is None:
    return max(node.value, node.value + solution(node.right))

  if node.right is None:
    return max(node.value, node.value + solution(node.left))

  left_value = solution(node.left)
  right_value = solution(node.right)
  res = max(node.value, node.value + left_value, node.value + right_value)

  if isRoot:
    res = max(res, node.value + left_value + right_value)

  return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
assert 6 == solution(root, True)


root = Node(10)
root.left = Node(2)
root.left.left = Node(20)
root.left.right = Node(1)

root.right = Node(10)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
assert 42 == solution(root, True)
