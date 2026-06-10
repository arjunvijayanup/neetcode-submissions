# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Slow and fast pointers to split the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Splitting both halves
        node1 = head
        node2 = slow.next
        slow.next = None

        # Reversing 2nd half
        curr = node2
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        node2 = prev

        # Adding alternative elements from both lists
        while node2:
            temp1, temp2 = node1.next, node2.next
            node1.next = node2
            node2.next = temp1
            node1, node2 = temp1, temp2
            
        

        

            
