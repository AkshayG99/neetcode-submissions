# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halfway point
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        r = slow.next
        slow.next = None
        prev = None

        while r:
            nxt = r.next
            r.next = prev
            prev = r
            r = nxt
        r = prev
        l = head
        
        #merge both lists

        while r:
            nxt1 = l.next
            nxt2 = r.next

            l.next = r
            l.next.next = nxt1
            l = nxt1
            r = nxt2
        
        