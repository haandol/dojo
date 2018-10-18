# https://www.geeksforgeeks.org/trie-insert-and-search/

class Node:
  def __init__(self):
    self.children = {}
    self.end = False


class Trie:
  def __init__(self):
    self.root = Node()

  def search(self, val):
    pass
 
  def insert(self, val):
    pass



trie = Trie()
trie.insert('the')
trie.insert('there')
trie.insert('their')
trie.insert('these')
trie.insert('thaw')
trie.insert('bye')
trie.insert('any')
trie.insert('answer')
