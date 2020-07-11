class Solution:
    def hammingWeight(self, n: int) -> int:
        # cnt=0
        # for i in str(n):
        #     cnt+=int(i)
        # return cnt
        cnt=0
        while n:
            cnt=cnt+(n&1)
            # n >>=1
            n=n>>1
        return cnt