# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        order = []

        if root:
            queue.append(root)
            order.append([root.val])
        
        while queue:
            o = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    o.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    o.append(curr.right.val)

            if o: order.append(o)
        
        return order
            
                