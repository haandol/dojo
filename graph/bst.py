# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def insert(node, val):
  if node is None:
    return

  if val <= node.val:
    if node.left:
      insert(node.left, val)
    else:
      node.left = Node(val)
  else:
    if node.right:
      insert(node.right, val)
    else:
      node.right = Node(val)


def search(node, val):
  if node is None:
    return False

  if node.val == val:
    return True

  if val < node.val:
    return search(node.left, val)
  elif node.val < val:
    return search(node.right, val)


def delete(node, val):
  if node is None:
    return

  if val < node.val:
    node.left = delete(node.left, val)
  elif node.val < val:
    node.right = delete(node.right, val)
  else:
    if node.left is None:
      return node.right
    elif node.right is None:
      return node.left
    else:
      temp = get_successor(node.right)
      node.val = temp.val
      node.right = delete(node.right, temp.val)

  return node


def get_successor(node):
  while node.left:
    node = node.left
  return node


def inorder(node):
  if node.left:
    inorder(node.left)
  print(node.val)
  if node.right:
    inorder(node.right)


if __name__ == '__main__':
  root = Node(50)
  insert(root, 30)
  insert(root, 20)
  insert(root, 40)
  insert(root, 70)
  insert(root, 60)
  insert(root, 80)

  inorder(root)
  print()

  assert True == search(root, 40)
  assert False == search(root, 45)

  root = delete(root, 30)
  assert root.val == 50
  inorder(root)
  print()

  root = delete(root, 50)
  assert root.val == 60
  inorder(root)
  print()