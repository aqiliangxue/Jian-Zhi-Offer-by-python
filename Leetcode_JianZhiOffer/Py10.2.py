class Solution:
    def numWays(self, n: int, m=[0] * (100 + 1)) -> int:
        # 青蛙跳台阶问题： f(0)=1, f(1)=1 , f(2)=2 ,f(3)=3
        # 斐波那契数列问题：f(0)=0, f(1)=1 , f(2)=1 ,f(3)=2
        # m=[0]*(n+1)

        # m[0]=1
        # m[1]=1
        # if n>=2:
        #     for i in range(2,n+1):
        #         m[i]=m[i-1]+m[i-2]
        # return m[n]%1000000007
        a, b = 1, 1
        for _ in range(n):
            # a=0,b=1
            # 这种赋值，先计算等值 右边 就是 b=1 a+b=1
            # 再赋值给a和b，那么 a=1, b=1
            # 然后就是依次这样
            a, b = b, a + b

            # a=0,b=1
            # a = b
            # 此时 b=1, 那么a=1
            # b = a+b
            # 那么 b=2
        return a % 1000000007