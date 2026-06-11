"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToMap = {None:None}
        curr = head
        while curr: # First pass for only copying nodes
            copy = Node(curr.val)
            oldToMap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr: # Second pass for copying next and random pointers
            copy = oldToMap[curr]
            copy.next = oldToMap[curr.next]
            copy.random = oldToMap[curr.random] 
            curr = curr.next
        
        return oldToMap[head]