# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 先序遍历，此解法运行时间长
        # def Helper(root):
        #     if root==None:return 0
        #     left=1+Helper(root.left)
        #     right=1+Helper(root.right)
        #     return max(left,right)
        #     # return max(self.Helper(root.left),self.Helper(root.right))+1
        # if root==None:return True
        # return abs(Helper(root.left)-Helper(root.right))<=1 and \
        # self.isBalanced(root.left) and self.isBalanced(root.right)

        def recur(root):
            if not root: return 0
            left = recur(root.left)
            # 等于-1，直接剪枝，不在计算后续
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1