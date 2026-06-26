# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        totSum = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            # If left or right maxes have -ve values, return 0
            leftMax = dfs(root.left) if dfs(root.left) > 0 else 0
            rightMax = dfs(root.right) if dfs(root.right) > 0 else 0

            # Maximum sum through root node
            totSum[0] = max(totSum[0], root.val + leftMax + rightMax)

            # Max downward sum starting at this node -> Return to parent node
            return root.val + max(leftMax, rightMax)

        dfs(root)

        return totSum[0]

            