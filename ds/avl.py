# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.height = 1


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

  node.height = 1 + max(get_height(node.left), get_height(node.right))

  balance = get_balance(node)

  # LL
  if balance > 1 and val < node.left.val:
    return rotate_right(node)
  # RR
  if balance < -1 and node.right.val < val:
    return rotate_left(node)
  # LR
  if balance > 1 and node.left.val < val:
    node.left = rotate_left(node.left)
    return rotate_right(node)
  # RL
  if balance < -1 and val < node.right.val:
    node.right = rotate_right(node.right)
    return rotate_left(node)

  return node

def get_height(node):
  if node is None:
    return 0

  return node.height

def get_balance(node):
  return get_height(node.left) - get_height(node.right)

def rotate_left(x):
  y = x.right
  c = y.left

  y.left = x
  x.right = c

  x.height = 1 + max(get_height(x.left), get_height(x.right))
  y.height = 1 + max(get_height(y.left), get_height(y.right))

  return y

def rotate_right(x):
  y = x.left
  c = y.right

  y.right = x
  x.left = c

  x.height = 1 + max(get_height(x.left), get_height(x.right))
  y.height = 1 + max(get_height(y.left), get_height(y.right))

  return y

def delete(node):
  pass

def preorder(node):
  if node is None:
    return

  print(node.val, node.height)
  preorder(node.left)
  preorder(node.right)


if __name__ == '__main__':
  root = Node(10)
  root = insert(root, 20) 
  root = insert(root, 30) 
  root = insert(root, 40) 
  root = insert(root, 50) 
  root = insert(root, 25) 

  preorder(root)