# https://www.tutorialspoint.com/data_structures_algorithms/heap_data_structure.htm
# https://www.cs.usfca.edu/~galles/visualization/Heap.html
'''
10 14 19 26 31 42 27 44 35
0  1  2  3  4  5  6  7  8

0 - 1, 2
1 - 3, 4
2 - 5, 6
3 - 7, 8

n * 2 + 1, n * 2 + 2
'''

class MinHeap(object):
  def __init__(self):
    self.L = []
    self.n = -1

  def insert(self, value):
    self.L.append(value)
    self.n += 1
    self.up(self.n)

  def up(self, c):
    if c <= 0:
      return

    if c % 2 == 0:
      p = (c - 2) / 2
    else:
      p = (c - 1) / 2

    if self.L[c] < self.L[p]:
      self.L[c], self.L[p] = self.L[p], self.L[c]

    self.up(p)

  def down(self, p):
    if self.n < p * 2 + 1:
      return 

    c = p * 2 + 1
    if self.L[c] < self.L[p]:
      self.L[c], self.L[p] = self.L[p], self.L[c]
    self.down(c)
    
    if self.n < p * 2 + 2:
      return 

    c = p * 2 + 2
    if self.L[c] < self.L[p]:
      self.L[c], self.L[p] = self.L[p], self.L[c]
    self.down(c)

  def pop(self):
    value = self.L[0]
    self.L[0] = self.L.pop()
    self.n -= 1

    self.down(0)
    return value


heap = MinHeap()
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

assert [10, 14, 19, 26, 31, 42, 27, 44, 35, 33] == heap.L
assert 10 == heap.pop()
assert [14, 26, 19, 33, 31, 42, 27, 44, 35] == heap.L
