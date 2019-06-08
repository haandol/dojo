class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        res = []
        for item in intervals:
            if not res:
                res.append(item)
            elif res[-1][1] < item[0]:
                res.append(item)
            elif item[0] <= res[-1][1] and res[-1][1] < item[1]:
                res[-1][1] = item[1]
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert [[1, 6], [8, 10], [15, 18]] == s.merge(arr)

    arr = [[1, 4], [4, 5]]
    assert [[1, 5]] == s.merge(arr)