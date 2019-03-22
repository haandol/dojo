# F: Forward, M: Midfielder, D: Defender
# Available Patterns in ['D', 'F', 'F', 'M'] ['D', 'F', 'M', 'M'] ['D', 'D', 'F', 'M']
from itertools import permutations
from pprint import pprint

FORMATIONS = [
  'DFFM',
  'DFMM',
  'DDFM'
]

def generate(player_formation):
  res = FORMATIONS[:]
  for f in player_formation:
    for i in range(len(res)):
      if not res[i]:
        break
      if f not in res[i]:
        res[i] = None
      else:
        res[i] = res[i].replace(f, '', 1)
  return list(filter(None, res))


P = {
  'D': generate('D'),
  'F': generate('F'),
  'M': generate('MF'),
  'DD': generate('DD'),
  'DF': generate('DF'),
  'DM': generate('DM'),
  'FF': generate('FF'),
  'FM': generate('FM'),
  'MM': generate('MM'),
  'DDF': generate('DDF'),
  'DDM': generate('DDM'),
  'DFF': generate('DFF'),
  'DFM': generate('DFM'),
  'DMM': generate('DMM'),
}

'''
P = {'D': ['FFM', 'FMM', 'DFM'],
 'DD': ['FM'],
 'DDF': ['FM'],
 'DDM': ['FM'],
 'DF': ['FM', 'MM', 'DM'],
 'DFF': ['M'],
 'DFM': ['F', 'M', 'D'],
 'DM': ['FF', 'FM', 'DF'],
 'DMM': ['F'],
 'F': ['DFM', 'DMM', 'DDM'],
 'FF': ['DM'],
 'FM': ['DF', 'DM', 'DD'],
 'M': ['DF', 'DM', 'DD'],
 'MM': ['DF']}
'''

def findCombination(w, n, combinations):
  for i in range(1, 4-len(w)):
    for item in permutations(n, i):
      target = ''.join(item)
      for comb in combinations:
        if comb == target:
          return comb
  return ''


waiting = 'F'
queue = ['FF', 'DF', 'D', 'DM', 'M', 'FFM']
nodes = []
for node in queue:
  nodes.append(node)
  combination = findCombination(waiting, nodes, P[waiting])
  if combination:
    print(combination)
    break