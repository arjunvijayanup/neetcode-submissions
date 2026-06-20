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
        
        while queue:
            o = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    o.append(curr.val)
                    queue.append(curr.left) # Even if left or right is None, when this loop runs it will return curr as False as it is None
                    queue.append(curr.right)
                
            if o: order.append(o)
        
        return order