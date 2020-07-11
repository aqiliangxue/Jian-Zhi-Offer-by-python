class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        tmp1=s[:n]
        tmp2=s[n:]
        return tmp2+tmp1