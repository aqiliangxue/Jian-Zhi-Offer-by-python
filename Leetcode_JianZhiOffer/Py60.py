class Solution:
    def twoSum(self, n: int) -> List[float]:
        # n个骰子，一共有6**n种情况
        # n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
        # n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
        # 其中F（N,S）表示投第N个骰子时，点数和为S的次数

        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        # n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
        for i in range(1,7):
            dp[1][i] = 1
        # 迭代第n个硬币次数
        for i in range(2,n+1):
            # 对于range(i,i*6+1)，骰子的最小点数为骰子个数，比如i为6，骰子个数为6-36
            #j代表s，即骰子朝上点数之和
            for j in range(i,i*6+1):
                for k in range(1,7):
                    # if j >= k+1:#用来避免重复计算的
                        dp[i][j] +=dp[i-1][j-k]
        res = []
        for i in range(n,n*6+1):
            res.append(dp[n][i]*1.0/6**n) #一共6的n次方种可能
        return res