# https://www.geeksforgeeks.org/binary-heap/

class MaxHeap(object):
  def __init__(self):
    self.L = []

  def insert(self, val):
    self.L.append(val)
    self.siftup(len(self.L) - 1)

  def pop(self):
    val = self.L[0]
    self.L[0] = self.L.pop()
    self.siftdown(0)
    return val

  def siftup(self, c):
    if c == 0:
      return

    p = int((c - 1) / 2)
    if self.L[p] < self.L[c]:
      self.L[p], self.L[c] = self.L[c], self.L[p]

    self.siftup(p)

  def siftdown(self, p):
    n = len(self.L)
    c = p * 2 + 1
    if c < n:
      if self.L[p] < self.L[c]:
        self.L[p], self.L[c] = self.L[c], self.L[p]
        self.siftdown(c)

    c = p * 2 + 2
    if c < n:
      if self.L[p] < self.L[c]:
        self.L[p], self.L[c] = self.L[c], self.L[p]
        self.siftdown(c)


heap = MaxHeap()
arr = [4, 10, 3, 5, 1]
for el in arr:
  heap.insert(el)
assert [10, 5, 3, 4, 1] == heap.L

assert 10 == heap.pop()
assert [5, 4, 3, 1] == heap.L
