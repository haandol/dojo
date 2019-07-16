class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        res = []
        intervals.sort(key=lambda x: x[0])
        for item in intervals:
            if not res:
                res.append(item)
            elif res[-1][1] < item[0]:
                res.append(item)
            else:
                if item[0] <= res[-1][0]:
                    res[-1][0] = item[0]
                if res[-1][1] < item[1]:
                    res[-1][1] = item[1]
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert [[1, 6], [8, 10], [15, 18]] == s.merge(arr)

    arr = [[1, 4], [4, 5]]
    assert [[1, 5]] == s.merge(arr)

    arr = [[1, 4], [0, 4]]
    assert [[0, 4]] == s.merge(arr)