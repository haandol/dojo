# 오름차순 정렬 배열로부터 높이가 가장 낮은 이진 탐색트리 생성

class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val


def _generate(arr, l, r):
  if r < l:
    return

  m  = int((l+r)/2)
  node = Node(arr[m])
  node.left = _generate(arr, l, m-1)
  node.right = _generate(arr, m+1, r)
  return node


def generate(arr):
  n = len(arr) - 1
  return _generate(arr, 0, n)


def preorder(node):
  if not node:
    return

  print(node.val)
  if node.left:
    preorder(node.left)
  if node.right:
    preorder(node.right)


if __name__ == '__main__':
  arr = [1, 2, 3, 4, 5, 6, 7]
  root = generate(arr)
  preorder(root)