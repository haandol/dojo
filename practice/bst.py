class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


def insert(node, val):
    if not node:
        return Node(val)

    if val <= node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)

    return node


def search(node, val):
    if not node:
        return False

    if val == node.val:
        return True
    elif val < node.val:
        return search(node.left, val)
    else:
        return search(node.right, val)


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
        if not node.right:
            return node.left
        successor = get_successor(node.right)
        node.val = successor.val
        node.right = delete(node.right, successor.val)

    return node


def get_successor(node):
    while node.left:
        node = node.left
    return node


def inorder(node):
    if not node:
        return

    inorder(node.left)
    print(node.val)
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

    assert search(root, 40)
    assert not search(root, 45)

    root = delete(root, 30)
    assert root.val == 50
    inorder(root)
    print()

    root = delete(root, 50)
    assert root.val == 60
    inorder(root)
    print()
