# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # a=[]
        # if root:
        #     print(root.val)
        #     a.append(root.val)
        #     a.append(self.levelOrder(root.left))
        #     a.append(self.levelOrder(root.right))
        #     return root.val

        # 采用bfs广度优先搜索解决问题
        if root==None:return []
        a,res=[],[]
        a.append(root)
        while a:
            b=a.pop(0)
            res.append(b.val)
            if b.left:a.append(b.left)
            if b.right:a.append(b.right)
        return res