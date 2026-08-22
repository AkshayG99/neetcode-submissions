# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        origin = head

        N = 0
        while head:
            N += 1 
            head = head.next
        
        removeIdx = N - n

        head = origin

        if removeIdx == 0:
            return origin.next

        idx = 0

        while True:
            if idx + 1 == removeIdx:
                head.next = head.next.next
                break
            idx +=1 
            head = head.next

        return origin
        