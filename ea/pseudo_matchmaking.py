playerPositions = 'F'
getPossiblePositions = [DMM, DFM, DDM]
generateCombination(DMM) = [[DMM], [DM, M], [D, MM], [D, M, M]]

def matchmaking(playerPositions):
  possiblePositions = getPossiblePosition(playerPositions)
  for possiblePosition in possiblePositions:
    for combination in generateCombination(possiblePosition):
      nodes = []
      found = True
      for position in combination:
        node = pullNodeFromQueue(position, nodes)
        if node: nodes.append(node)
        else:
          found = False
          break
      if found:
        return nodes
  return []