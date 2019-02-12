import re

class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        
        fs = re.findall(r'([-+]?\d+)', s)
        if not fs:
            return 0
        
        if not s.startswith(fs[0]):
            return 0
        
        print(fs)
        for el in fs:
            ls = list(el)
            sign = -1 if ls[0] == '-' else 1
            if ls[0] in ['-','+'] : del ls[0]
            ret, i = 0, 0
            while i < len(ls) and ls[i].isdigit() :
                ret = ret*10 + ord(ls[i]) - ord('0')
                i += 1
            return max(-2**31, min(sign * ret,2**31-1))

s = Solution()
print(s.myAtoi('+0 123'))