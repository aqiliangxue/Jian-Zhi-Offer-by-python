class Solution:
    def countDigitOne(self, n: int) -> int:
        # m=0
        # for i in range(1,n+1):
        #     for j in str(i):
        #         if j=="1":
        #             m=m+1
        # return m

        # s=""
        # for i in range(1,n+1):
        #     s=s+str(i)
        # return s.count("1")
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            # 得到低位
            low += cur * digit
            # 求余得到该位的值
            cur = high % 10
            # high除10得到高位
            high //= 10
            # 位于哪一位，各位 十位 一次向上乘以10
            digit *= 10
        return res