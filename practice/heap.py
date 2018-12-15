class MinHeap:
  def __init__(self):
    self.arr = []

  def insert(self, val):
    self.arr.append(val)
    self.siftup(len(self.arr)-1)

  def siftup(self, c):
    if c == 0:
      return

    p = int((c - 1) / 2)
    if self.arr[c] < self.arr[p]:
      self.arr[c], self.arr[p] = self.arr[p], self.arr[c]
      self.siftup(p)

  def pop(self):
    val = self.arr[0]
    self.arr[0] = self.arr.pop()
    self.siftdown(0)
    return val

  def siftdown(self, p):
    c = p * 2 + 1
    if len(self.arr) <= c:
      return

    if self.arr[c] < self.arr[p]:
      self.arr[c], self.arr[p] = self.arr[p], self.arr[c]
      self.siftdown(c)

    c = p * 2 + 2
    if len(self.arr) <= c:
      return

    if self.arr[c] < self.arr[p]:
      self.arr[c], self.arr[p] = self.arr[p], self.arr[c]
      self.siftdown(c)


if __name__ == '__main__':
  heap = MinHeap()
  L = [4, 10, 3, 5, 1]
  for el in L:
    heap.insert(el)
  assert [1, 3, 4, 10, 5] == heap.arr

  assert 1 == heap.pop()
  assert [3, 5, 4, 10] == heap.arr
