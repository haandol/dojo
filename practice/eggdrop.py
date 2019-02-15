def eggdrop(e, f):
  if f == 0 or f == 1:
    return f

  if e == 1:
    return f

  trials = float('inf')
  for i in range(1, f+1):
    res = max(eggdrop(e-1, i-1), eggdrop(e, f-i))
    trials = min(trials, res)

  return trials + 1

print(eggdrop(2, 10))