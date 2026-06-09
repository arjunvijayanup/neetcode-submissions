# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1, p2 = head, head.next if head else -1
        while p1 and p2:
            if p1 == p2:
                return True
            else:
                p1 = p1.next
                p2 = p2.next.next if p2.next and p2.next.next else None
        
        return False