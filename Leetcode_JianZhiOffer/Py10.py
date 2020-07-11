class Solution:
    def fib(self, n: int, m=[0] * 101) -> int:

        # 解法1
        # if n == 0:
        #     m[0] = 0
        #     return 0
        # elif n == 1:
        #     m[1] = 1
        #     return 1
        # # elif m[str(n)] != None:
        # #     return m[n]
        # if m[n]>0:
        #     return m[n]
        # m[n] = self.fib(n - 1,m) + self.fib(n - 2,m)

        # # print(m)
        # return m[n]%1000000007

        # 解法2
        # 斐波那契数列格式为：1、1、2、3、5、8、13、21、34
        m[0] = 0
        m[1] = 1
        if n >= 2:
            for i in range(2, n + 1):
                m[i] = m[i - 1] + m[i - 2]
        return m[n] % 1000000007