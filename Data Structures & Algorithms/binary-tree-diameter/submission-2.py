# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        # For returning height
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.length = max(self.length, left + right) # Updates global max length (dia)

            return 1 + max(left, right) # Returns height of current node to its parent.
        
        dfs(root)

        return self.length