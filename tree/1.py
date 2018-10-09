# https://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def solution(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    if node.left is None:
        return 1 + solution(node.right)

    if node.right is None:
        return 1 + solution(node.left)

    return 1 + min(solution(node.left), solution(node.right))


def solution2(root):
    Q = [root]
    D = {
        root.value: 1,
    }

    while Q:
        node = Q.pop(0)
        depth = D[node.value]
        if node.left is None and node.right is None:
            return depth
        
        if node.left:
            Q.append(node.left)
            D[node.left.value] = depth + 1

        if node.right:
            Q.append(node.right)
            D[node.right.value] = depth + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

assert 2 == solution(root)
assert 2 == solution2(root)

root = Node(10)
root.left = Node(5)

assert 2 == solution(root)
assert 2 == solution2(root)
