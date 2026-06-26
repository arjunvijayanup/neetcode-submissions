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

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Max sum through this node 
            totSum[0] = max(totSum[0], root.val + leftMax + rightMax)

            # Max Downward Path starting at this node -> returned to parent node
            return root.val + max(leftMax, rightMax)
        
        dfs(root)

        return totSum[0]
            