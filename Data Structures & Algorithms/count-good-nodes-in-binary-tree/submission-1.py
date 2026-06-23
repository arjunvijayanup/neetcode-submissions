# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, curr_max):
            if not root:
                return 0
            
            good = 1 if root.val >= curr_max else 0

            return (good + 
                    dfs(root.left, max(curr_max, root.val)) +
                    dfs(root.right, max(curr_max, root.val)))
            
        
        return dfs(root, root.val)


        

