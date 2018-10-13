class MaxHeap(object):
  def __init__(self):
    self.L = []
    self.n = -1

  def up(self, c):
    if c == 0:
      return

    if c % 2 == 1:
      p = int((c - 1) / 2)
    else:
      p = int((c - 2) / 2)

    if self.L[p] < self.L[c]:
      self.L[p], self.L[c] = self.L[c], self.L[p]

    self.up(p)

  def insert(self, value):
    self.L.append(value)
    self.n += 1

    self.up(self.n)

  def down(self, p):
    c = int(p * 2 + 1)
    if c <= self.n and self.L[p] < self.L[c]:
      self.L[p], self.L[c] = self.L[c], self.L[p]
      self.down(c)

    c = int(p * 2 + 2)
    if c <= self.n and self.L[p] < self.L[c]:
      self.L[p], self.L[c] = self.L[c], self.L[p]
      self.down(c)

  def pop(self):
    value = self.L[0]
    self.L[0] = self.L.pop()
    self.n -= 1

    self.down(0)

    return value


heap = MaxHeap()
heap.insert(35)
heap.insert(33)
heap.insert(42)
heap.insert(10)
heap.insert(14)
heap.insert(19)
heap.insert(27)
heap.insert(44)
heap.insert(26)
heap.insert(31)

assert [44, 42, 35, 33, 31, 19, 27, 10, 26, 14] == heap.L
assert 44 == heap.pop()
assert [42, 33, 35, 26, 31, 19, 27, 10, 14] == heap.L
