class HashMap:
  def __init__(self):
    self.size = 100
    self.L = [None] * self.size

  def hash(self, val):
    return sum(map(ord, val)) % self.size

  def insert(self, key, val):
    i = self.hash(key)
    while self.L[i] and i < self.size:
      i += 1
    if i == self.size:
      raise RuntimeError('runtime error')
    
    self.L[i] = (key, val)

  def has_key(self, key):
    i = self.hash(key)
    while self.L[i] and i < self.size:
      if self.L[i][0] == key:
        return True
      i += 1
    return False

  def get(self, key):
    i = self.hash(key)
    while self.L[i] and i < self.size:
      if self.L[i][0] == key:
        return self.L[i][1]
      i += 1
    return None

  def delete(self, key):
    i = self.hash(key)
    while self.L[i] and i < self.size:
      if self.L[i][0] == key:
        self.L[i] = None
      i += 1


if __name__=='__main__':
  hmap = HashMap()
  assert 97 == hmap.hash('xM')
  assert 97 == hmap.hash('a')
  assert 1 == hmap.hash('e')
  assert 9 == hmap.hash('hi')

  hmap.insert('a', 36)
  hmap.insert('g', 16)
  hmap.insert('z', 96)

  assert True == hmap.has_key('a')
  assert True == hmap.has_key('g')
  assert False == hmap.has_key('f')

  assert 36 == hmap.get('a')
  assert 16 == hmap.get('g')
  assert None == hmap.get('f')

  hmap.delete('a')
  hmap.delete('c')

  assert None == hmap.get('a')
  assert 96 == hmap.get('z')

  hmap.insert('a', 36)
  hmap.insert('xM', 38)
  assert True == hmap.has_key('a')
  assert True == hmap.has_key('xM')