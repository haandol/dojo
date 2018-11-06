# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(n, s):
    counts = []
    for el in s:
        if el == 'U':
            counts.append(1)
        else:
            counts.append(-1)

    for i in range(1, n):
        counts[i] += counts[i-1]

    valley_start = False
    valley_count = 0
    for el in counts:
        if el < 0 and not valley_start:
            valley_start = True
        elif 0 == el and valley_start:
            valley_start = False
            valley_count += 1

    return valley_count


if __name__ == '__main__':
    result = countingValleys(12, 'DDUUDDUDUUUD')
    assert 2 == result

    result = countingValleys(8, 'UDDDUDUU')
    assert 1 == result
