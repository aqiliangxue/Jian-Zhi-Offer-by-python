class Solution:
    def printNumbers(self, n: int) -> List[int]:
        m=[]
        for i in range(1,pow(10,n)):
            m.append(i)
        return m