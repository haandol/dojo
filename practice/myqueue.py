class MyQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def append(self, val):
    self.stack1.append(val)

  def pop(self):
    while self.stack1:
      self.stack2.append(self.stack1.pop())
    val = self.stack2.pop()
    while self.stack2:
      self.stack1.append(self.stack2.pop())
    return val


if __name__ == '__main__':
  queue = MyQueue()
  queue.append(1)
  queue.append(2)
  queue.append(3)

  assert 1 == queue.pop()
  assert 2 == queue.pop()
  assert 3 == queue.pop()