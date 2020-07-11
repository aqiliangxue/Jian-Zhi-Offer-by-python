# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p,q在root的左子树，向左子树探索
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        # p，q在root的右子树，向右子树探索
        if p.val >root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        # p，q分别在左右子树，返回root
        return root