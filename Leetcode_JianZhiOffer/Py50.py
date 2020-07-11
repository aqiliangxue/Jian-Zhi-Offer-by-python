class Solution:
    def firstUniqChar(self, s: str) -> str:
        d={}
        for c in s:
            # 多次出现，将键值设为False
            d[c]= not c in d
        for c in s:
            if d[c]:
                return c
        return " "