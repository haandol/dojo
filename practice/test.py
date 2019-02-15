class NestedIterator(object):
    def __init__(self, nestedList):
        self.it = self.flatten(nestedList)
        self.val = next(self.it)

    def flatten(self, nestedList):
        for el in nestedList:
            if type(el) == int:
              yield el
            else:
              for y in self.flatten(el):
                yield y

    def next(self):
      ret = self.val
      try:
        self.val = next(self.it)
      except StopIteration:
        self.val = None
      return ret

    def hasNext(self):
      return bool(self.val)


nestedList = [[1,1],2,[1,1]]
nestedList = []
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)
