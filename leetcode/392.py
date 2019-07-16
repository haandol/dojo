class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True
        if not t:
            return False

        n = len(s)
        m = len(t)
        i = 0
        j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if n == i:
            return True
        return False

s = Solution()
print(s.isSubsequence('abc', 'ahbgdc'))
print(s.isSubsequence('axc', 'ahbgdc'))