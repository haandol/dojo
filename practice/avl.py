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
    if not node:
        return Node(val)

    if val <= node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    # LL
    if 1 < balance and val <= node.left.val:
        node = rotate_right(node)
    # LR
    elif 1 < balance and node.left.val < val:
        node.left = rotate_left(node.left)
        node = rotate_right(node)
    # RR
    elif balance < -1 and node.right.val < val:
        node = rotate_left(node)
    # RL
    elif balance < -1 and val <= node.right.val:
        node.right = rotate_right(node.right)
        node = rotate_left(node)

    return node


def rotate_left(x):
    z = x.right
    a = z.left

    z.left = x
    x.right = a

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

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

    # LL
    if 1 < balance and val <= node.left.val:
        node = rotate_right(node)
    # LR
    elif 1 < balance and node.left.val < val:
        node.left = rotate_left(node.left)
        node = rotate_right(node)
    # RR
    elif balance < -1 and node.right.val < val:
        node = rotate_left(node)
    # RL
    elif balance < -1 and val <= node.right.val:
        node.right = rotate_right(node.right)
        node = rotate_left(node)

    return node


def get_successor(node):
    while node.left:
        node = node.left
    return node


def inorder(node):
    if not node:
        return

    inorder(node.left)
    print(node.val, node.height)
    inorder(node.right)


if __name__ == '__main__':
    root = Node(10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 25)
    inorder(root)
    print()

    root = delete(root, 30)
    inorder(root)
    print()
