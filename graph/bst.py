# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def insert(node, val):
  return node


def search(node, val):
  pass


def delete(node, val):
  pass


def inorder(node):
  if node.left:
    inorder(node.left)
  print(node.val)
  if node.right:
    inorder(node.right)


if __name__ == '__main__':
  root = Node(50)
  root = insert(root, 30)
  root = insert(root, 20)
  root = insert(root, 40)
  root = insert(root, 70)
  root = insert(root, 60)
  root = insert(root, 80)

  inorder(root)