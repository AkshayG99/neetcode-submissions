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
        while l1 and l2:

            sum = l1.val + l2.val + carry
            carry = 0
            if sum >= 10:
                carry = 1
                sum = sum - 10
            
            outHead.next = ListNode(sum)
            outHead = outHead.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            carry = 0
            if sum >= 10:
                carry = 1
                sum = sum - 10
            outHead.next = ListNode(sum)
            outHead = outHead.next
            l1 = l1.next

        while l2:
            sum = l2.val + carry
            carry = 0
            if sum >= 10:
                carry = 1
                sum = sum - 10
            outHead.next = ListNode(sum)
            outHead = outHead.next
            l2 = l2.next

        if carry:
            outHead.next = ListNode(carry)
        return origin.next
            
            
