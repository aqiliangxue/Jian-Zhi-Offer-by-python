
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        # 设定 “左、上、右、下”四个边界，边界相遇则退出循环
        l,r,t,b,res=0,len(matrix[0])-1,0,len(matrix)-1,[]
        while True:
            for i in range(l,r+1):
                res.append(matrix[l][i])
            t=t+1
            if t>b: break

            for i in range(t,b+1):
                res.append(matrix[i][r])
            r=r-1
            if r<l:break

            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b=b-1
            if b<t:break

            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l=l+1
            if l>r:break

        return res