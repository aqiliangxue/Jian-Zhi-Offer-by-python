class Solution:
    def constructArr(self, a: List[int]) -> List[int]:

        # 超出时间限制
        # m=[1]*len(a)
        # for j in range(0,len(a)):
        #     for i in range(0,len(a)):
        #         if i==j:continue
        #         m[j]=m[j]*a[i]
        # return m

        b,tmp=[1]*len(a),1
        # 先计算下三角乘积
        for i in range(1,len(a)):
            b[i]=b[i-1]*a[i-1]
        # 然后计算上三角乘积
        for i in range(len(a)-2,-1,-1):
            tmp=tmp*a[i+1]
            b[i]=b[i]*tmp
        return b