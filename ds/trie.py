class Node(object):
  def __init__(self):
    self.children = {}
    self.end = False
    self.word = None

  def __repr__(self):
    return ','.join(self.children.keys())


class Trie(object):
  def __init__(self):
    self.root = Node()

  def insert(self, s):
    node = self.root

    for ch in s:
      if ch not in node.children:
        node.children[ch] = Node()
      node = node.children[ch]
    
    node.end = True
    node.word = s

  def print_leaf(self, node, words):
    if node.end:
      words.append(node.word)
    
    for ch in node.children:
      self.print_leaf(node.children[ch], words)

  def search(self, s):
    words = []
    node = self.root
    for ch in s:
      if ch not in node.children:
        return False
      
      if node.end:
        words.append(node.word)
      node = node.children[ch]

    self.print_leaf(node, words)
    return words


trie = Trie()
trie.insert('the')
trie.insert('there')
trie.insert('their')
trie.insert('answer')
trie.insert('any')
trie.insert('bye')

assert ['the', 'their', 'there'] == trie.search('the')
