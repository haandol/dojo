# 4.8 - 어떤 이진 트리가 이진 탐색트리인지 판별하는 함수를 구현하라

class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val


def check_bst(node):
  if not node:
    return True
  
  if node.left and node.val < node.left.val:
    return False
  if node.right and node.right.val < node.val:
    return False

  return check_bst(node.left) and check_bst(node.right)


if __name__ == '__main__':
  root = Node(5)
  root.left = Node(3)
  root.right = Node(7)
  assert True == check_bst(root)

  root = Node(5)
  root.left = Node(9)
  root.right = Node(7)
  assert False == check_bst(root)

  root = Node(5)
  root.left = Node(1)
  root.right = Node(3)
  assert False == check_bst(root)