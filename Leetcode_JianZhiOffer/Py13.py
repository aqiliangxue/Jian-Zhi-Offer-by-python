class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 辅助函数
        def sumn(num):
            return num//10+num%10
        # # 解法1 采用广度优先搜索bfs
        # quene,visited=[(0,0,0,0)],set()
        # while quene:
        #     i,j,si,sj=quene.pop(0)
        #     # 索引越界或者个数和大于k或者当前节点已经位于visited，跳过本次循环
        #     if i>=m or j>=n or si+sj>k or (i,j) in visited: continue
        #     visited.add((i,j))
        #     # 向下，向右探索
        #     quene.append((i+1,j,sumn(i+1),sumn(j)))
        #     quene.append((i,j+1,sumn(i),sumn(j+1)))
        # return len(visited)

        # 解法2 深度优先搜索
        def dfs(i,j,si,sj):
            # 索引越界或者个数和大于k或者当前节点已经位于visited，返回0
            if i>=m or j>=n or si+sj>k or (i,j) in visited:
                return 0
            # 否则当前节点加入集合,并且数量+1
            visited.add((i,j))
            # 返回1和向左和向右探索的数量
            return 1+dfs(i+1,j,sumn(i+1),sumn(j))+dfs(i,j+1,sumn(i),sumn(j+1))
        visited=set()
        return dfs(0,0,0,0)