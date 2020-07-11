class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 把幂次n换算为二进制简化求解，例如9的二进制为1001 转为x的8次方+x的一次方
        if x==0: return 0
        res=1
        # n<0,x转换为倒数，将n取为正数
        if n<0:x,n= 1/x,-n
        while n:
            # n和1与，为1需要相乘
            if n&1: res=res*x
            x=x*x
            n=n>>1
        return res