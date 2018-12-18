class Node:
  def __init__(self):
    self.children = {}
    self.val = None
    self.isEnd = False


class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, val):
    node = self.root
    for ch in val:
      if ch not in node.children:
        node.children[ch] = Node()
      node = node.children[ch]
    node.isEnd = True
    node.val = val

  def print(self, node):
    if node.isEnd:
      print(node.val)

    for k in node.children:
      self.print(node.children[k])

  def search(self, val):
    node = self.root
    for ch in val:
      if ch not in node.children:
        return False
      
      if node.isEnd:
        print(node.val)
      node = node.children[ch]

    self.print(node)


trie = Trie()
trie.insert('the')
trie.insert('there')
trie.insert('their')
trie.insert('these')
trie.insert('thaw')
trie.insert('bye')
trie.insert('any')
trie.insert('answer')

trie.search('an')
print()
trie.search('th')
print()
trie.search('tha')
print()
trie.search('b')
print()
trie.search('bt')
