class HashMap:
  def __init__(self):
    self.hsize = 100
    self._list = [None] * self.hsize

  def hash(self, key):
    return sum(map(lambda x: ord(x), str(key))) % self.hsize

  def insert(self, key, val):
    index = self.hash(key)
    while index < self.hsize and None != self._list[index]:
      index += 1
    self._list[index] = (key, val)

  def get(self, key):
    index = self.hash(key)
    while index < self.hsize and self._list[index] and key != self._list[index][0]:
      index += 1
    return self._list[index] and self._list[index][1]

  def delete(self, key):
    index = self.hash(key)
    while index < self.hsize and self._list[index] and key != self._list[index][0]:
      index += 1
    self._list[index] = None

  def has_key(self, key):
    index = self.hash(key)
    while index < self.hsize and self._list[index] and key != self._list[index][0]:
      index += 1
    return bool(self._list[index] and self._list[index][1])


if __name__=='__main__':
  hmap = HashMap()
  assert 97 == hmap.hash('a')
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