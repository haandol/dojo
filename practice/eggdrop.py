def helper(e, f):
    if e == 1:
        return f
    if f < 2:
        return f

    min_so_far = float('inf')
    for i in range(1, f+1):
        res = max(helper(e-1, i-1), helper(e, f-i))
        min_so_far = min(min_so_far, res)
    
    return min_so_far + 1


def eggdrop(e, f):
    return helper(e, f)


if __name__ == '__main__':
    assert 2 == eggdrop(1, 2)
    assert 2 == eggdrop(2, 2)
    assert 3 == eggdrop(2, 6)
    assert 4 == eggdrop(2, 7)
    assert 4 == eggdrop(3, 14)
