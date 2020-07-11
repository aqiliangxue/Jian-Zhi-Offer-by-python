class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        # 采用深度优先算法解题
        def dfs(i,j,k):
            res=False
            # 数组越界或者第k个字符和第k个探索到的字符不相等 返回false
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!=word[k]: return False
            # 如果k等于word的长度，说明找到一个序列，并且这个序列等于word
            if k==len(word)-1:return True
            # 探索board[i][j]的下一格时，将board[i][j]替换为" ",防止本序列重复探索
            tmp,board[i][j]=board[i][j]," "
            # 递归探索
            res=dfs(i,j+1,k+1) or dfs(i,j-1,k+1) or dfs(i-1,j,k+1) or dfs(i+1,j,k+1)
            # 探索完成之后将board[i][j]改为原来的值
            board[i][j]=tmp
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False