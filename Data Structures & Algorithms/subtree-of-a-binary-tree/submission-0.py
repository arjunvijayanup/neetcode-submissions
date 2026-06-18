# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: # If tree is empty, no subtree can exist in it 
            return False 
        if self.isSameTree(root, subRoot): # Checking if current node is start of subRoot
            return True
        else: # Check if children is the start of the subRoot
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot: # Reached left and right of leaf nodes
            return True
        if root and subRoot and root.val == subRoot.val: # Keeps on returning True if both left and right exists and have same values
            return (self.isSameTree(root.left, subRoot.left) and 
            self.isSameTree(root.right, subRoot.right))
        else:
            return False # False if there is a mismatch in values b/w same nodes in any of the two trees