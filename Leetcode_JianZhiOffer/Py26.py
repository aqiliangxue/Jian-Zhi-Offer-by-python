# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 定义辅助递归函数，判断两个树是否完全相等
        def recur(A,B):
            # 如果越过B叶子节点，返回True 或者B已经越过叶子节点，说明两树相等
            if not B: return True
            # 如果B不为空，A为空，或者A的值和B的值不相等，说明两树不相等
            if not A or A.val!=B.val:return False
            # 向下递归
            return recur(A.left,B.left) and recur(A.right,B.right)
        # 主函数调用辅助递归函数，判断A树和B树是否相等  或者A的左子树和B树相等  或者A的右子树和B树相等
        return bool(A and B) and(recur(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B))