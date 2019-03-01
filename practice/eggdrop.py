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
    df = [
        [float('inf')] * (f+1)
        for _ in range(e+1)
    ]

    for i in range(e+1):
        df[i][0] = 0
        df[i][1] = 1

    for i in range(f+1):
        df[0][i] = 0
        df[1][i] = i

    for i in range(2, e+1):
        for j in range(2, f+1):
            for k in range(1, j+1):
                res = 1 + max(df[i-1][k-1], df[i][j-k])
                df[i][j] = min(res, df[i][j])

    return df[e][f]


if __name__ == '__main__':
    assert 2 == eggdrop(1, 2)
    assert 2 == eggdrop(2, 2)
    assert 3 == eggdrop(2, 6)
    assert 4 == eggdrop(2, 7)
    assert 4 == eggdrop(3, 14)
    assert 8 == eggdrop(2, 36)
    print(eggdrop(4, 10000))
