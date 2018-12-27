from pprint import pprint

decompressed = [
  [None] * 10
  for _ in range(10)
]

def decompress(it, y, x, size):
  ch = next(it)
  if ch == 'b' or ch == 'w':
    for dy in range(size):
      for dx in range(size):
        decompressed[y+dy][x+dx] = ch
  else:
    half = int(size / 2)
    decompress(it, y, x, half)
    decompress(it, y, x+half, half)
    decompress(it, y+half, x, half)
    decompress(it, y+half, x+half, half)


if __name__ == '__main__':
  s = 'xbwxwbbwb'
  s = 'xbwwb'
  decompress(iter(s), 0, 0, len(s))
  pprint(decompressed)