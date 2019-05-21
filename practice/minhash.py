import re
import sys
import random


def n_gram(s, n):
    s = re.sub(r'([^\w ])+', '', s.lower())
    L = s.split(' ')
    res = []
    for i in range(len(L)):
        shingle = L[i:i+n]
        if len(shingle) == n:
            res.append('_'.join(shingle))
    return res


def min_hash(s):
    m = sys.maxsize
    for x in s:
        h = hash(x) % 400
        m = min(h, m)
    return m


if __name__ == '__main__':
    s1 = n_gram('Hello world, my name is Daniel!', 3)
    s2 = n_gram('My name is Daniel, hello world!', 3)
    print(min_hash(s1))
    print(min_hash(s2))