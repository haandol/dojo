class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def insert(node, val):
  if val <= node.val:
    if node.left:
      node.left = insert(node.left, val)
    else:
      node.left = Node(val)
  elif node.val < val:
    if node.right:
      node.right = insert(node.right, val)
    else:
      node.right = Node(val)

  return node


def inorder(node):
  if not node:
    return

  if node.left:
    inorder(node.left)
  print(node.val)
  if node.right:
    inorder(node.right)


def search(node, val):
  if not node:
    return False

  if val < node.val:
    return search(node.left, val)
  elif node.val < val:
    return search(node.right, val)
  else:
    return True


def delete(node, val):
  if not node:
    return None

  if val < node.val:
    node.left = delete(node.left, val)
  elif node.val < val:
    node.right = delete(node.right, val)
  else:
    if not node.left:
      return node.right
    elif not node.right:
      return node.left
    
    successor = get_successor(node.right)
    node.val = successor.val
    node.right = delete(node.right, successor.val)

  return node


def get_successor(node):
  while node.left:
    node = node.left

  return node


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