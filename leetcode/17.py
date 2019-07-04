class Solution:
    def helper(self, s, i, n, path, res, table):
        if i == n:
            if len(path) == n:
                res.append(path)
            return

        letters = table[s[i]]
        for letter in letters:
            self.helper(s, i+1, n, path+letter, res, table)

    def letterCombinations(self, digits: str):
        if not digits:
            return []

        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        self.helper(digits, 0, len(digits), '', res, table)
        return res

s = Solution()
print(s.letterCombinations('23'))