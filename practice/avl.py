class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.height = 1


def get_height(node):
  if not node:
    return 0
  return node.height


def get_balance(node):
  return get_height(node.left) - get_height(node.right)


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
  # unbalance
  if 1 < balance:
  # LL
    if val < node.left.val:
      return rotate_right(node)
  # LR
    elif node.left.val < val:
      node.left = rotate_left(node.left)
      return rotate_right(node)
  elif balance < -1:
  # RR
    if node.right.val < val:
      return rotate_left(node)
  # RL
    elif val < node.right.val:
      node.right = rotate_right(node.right)
      return rotate_left(node)

  return node


def rotate_left(x):
  z = x.right
  a = z.left

  z.left = x
  x.right = a

  x.height = 1 + max(get_height(x.left), get_height(x.right))
  z.height = 1 + max(get_height(z.left), get_height(z.right))

  return z


def rotate_right(x):
  y = x.left
  b = y.right

  y.right = x
  x.left = b

  x.height = 1 + max(get_height(x.left), get_height(x.right))
  y.height = 1 + max(get_height(y.left), get_height(y.right))

  return y



def delete(node, val):
  if not node:
    return

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

  node.height = 1 + max(get_height(node.left), get_height(node.right))
  balance = get_balance(node)
  # unbalance
  if 1 < balance:
  # LL
    if val < node.left.val:
      return rotate_right(node)
  # LR
    elif node.left.val < val:
      node.left = rotate_left(node.left)
      return rotate_right(node)
  elif balance < -1:
  # RR
    if node.right.val < val:
      return rotate_left(node)
  # RL
    elif val < node.right.val:
      node.right = rotate_right(node.right)
      return rotate_left(node)
 
  return node


def get_successor(node):
  while node.left:
    node = node.left
  return node


def preorder(node):
  if not node:
    return

  print(node.val)
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
  print()

  root = delete(root, 30)
  preorder(root)
  print()