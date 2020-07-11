# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # if len(preorder)==0:
        #     return None
        # root=TreeNode(preorder[0])
        # i=inorder.index(preorder[0])
        # root.left=self.buildTree(preorder[1:i+1],inorder[:i])
        # root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        # return root

        # 递归结束条件，preorder为0，返回None
        if len(preorder)==0:
            return None
        root = TreeNode(preorder[0])
        i=inorder.index(preorder[0])
        # 按照i的索引，分开左右子树，递归建树
        root.left=self.buildTree(preorder[1:i+1],inorder[:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        return root