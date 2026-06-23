# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, currMin, currMax):
            if not root:
                return True

            if not(currMin < root.val < currMax):
                return False
            
            return (dfs(root.left, currMin, root.val) and 
                    dfs(root.right, root.val, currMax))
        
        return dfs(root, float("-inf"), float("inf"))
