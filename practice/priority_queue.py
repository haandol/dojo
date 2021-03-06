class PriorityQueue:
  def __init__(self):
    self.heap = []

  def push(self, priority, val):
    self.heap.append((priority, val))
    self.siftup(len(self.heap) - 1)

  def siftup(self, c):
    if c == 0:
      return

    p = int((c - 1) / 2)
    if self.heap[p][0] < self.heap[c][0]:
      self.heap[c], self.heap[p] = self.heap[p], self.heap[c]
      self.siftup(p)

  def pop(self):
    if not self.heap:
      return (-1, None)

    last = self.heap.pop()
    if not self.heap:
      return last

    val = self.heap[0]
    self.heap[0] = last
    self.siftdown(0)
    return val

  def siftdown(self, p):
    c = p * 2 + 1
    if c < len(self.heap):
      if self.heap[p][0] < self.heap[c][0]:
        self.heap[c], self.heap[p] = self.heap[p], self.heap[c]
        self.siftdown(c)

    c = p * 2 + 2
    if c < len(self.heap):
      if self.heap[p][0] < self.heap[c][0]:
        self.heap[c], self.heap[p] = self.heap[p], self.heap[c]
        self.siftdown(c)


if __name__ == '__main__':
  queue = PriorityQueue()
  queue.push(0, 'a') 
  queue.push(4, 'q') 
  queue.push(2, 'd') 
  queue.push(3, 'e') 
  queue.push(1, 'c') 

  print(queue.heap)

  assert (4, 'q') == queue.pop()
  assert (3, 'e') == queue.pop()
  assert (2, 'd') == queue.pop()
  assert (1, 'c') == queue.pop()
  assert (0, 'a') == queue.pop()
  assert (-1, None) == queue.pop()