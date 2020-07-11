class Solution:
    def cuttingRope(self, n: int) -> int:
        # if n=2:return 1
        # if n=3:return 2

        # 贪心算法，切割长度相等，且长度为3，可以取得最大值
        # 如果对3求余有余数，需要考虑
        # if n<=3:return n-1
        # a,b=n//3,n%3
        # if b==0:return pow(3,a)
        # if b==1:return pow(3,a-1)*2*2
        # if b==2:return pow(3,a)*2

        # 动态规划

        if n <= 3: return n - 1
        b = [0] * (n + 1)
        b[1] = 1
        b[2] = 2
        b[3] = 3  # 为了满足后续递推
        # b[4]=4
        # m=0
        for i in range(4, n + 1):
            m = 0
            for j in range(1, i // 2 + 1):
                if b[j] * b[i - j] > m:
                    m = b[j] * b[i - j]
            b[i] = m
        return b[n]