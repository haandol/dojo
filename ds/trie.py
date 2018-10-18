# https://www.geeksforgeeks.org/trie-insert-and-search/

class Node:
  def __init__(self):
    self.children = {}
    self.end = False


class Trie:
  def __init__(self):
    self.root = Node()

  def search(self, s):
    node = self.root
    for i, ch in enumerate(s):
      if ch not in node.children:
        return

      node = node.children[ch]
      if node.end:
        print(s[:i+1])
    
    self.print_tree(s[:i+1], node) 

  def print_tree(self, word, node):
    if node.end:
      print(word)

    for ch in node.children:
      self.print_tree(word + ch, node.children[ch])
      
  def insert(self, s):
    node = self.root
    for ch in s:
      if ch not in node.children:
        node.children[ch] = Node()
      node = node.children[ch]
    node.end = True


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
