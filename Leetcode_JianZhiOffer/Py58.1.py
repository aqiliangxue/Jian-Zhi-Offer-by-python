class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        return " ".join([a[i-2].strip() for i in range(len(a)+1,1,-1)])


        # s = s.split()[::-1]
        # return ' '.join(s)