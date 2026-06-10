# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):, Sized
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reversing list
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head = prev

        i = 1
        nxt = head
        pre = None
        while nxt:
            if i == n:
                if pre == None:
                    head = nxt.next
                else:
                    pre.next = pre.next.next
                break
            pre = nxt
            nxt = nxt.next
            i += 1


        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        
