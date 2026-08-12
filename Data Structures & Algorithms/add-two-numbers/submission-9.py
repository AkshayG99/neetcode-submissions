# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        outHead = ListNode(0)
        origin = outHead

        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            lowerColumn = total % 10
            carry = total // 10

            outHead.next = ListNode(lowerColumn)
            outHead = outHead.next
            l1, l2 = l1.next if l1 else 0, l2.next if l2 else 0
        
        return origin.next
        
