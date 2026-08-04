# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visit = deque([(p,q)])

        while visit:
            currP, currQ = visit.popleft()
            if not currP and not currQ:
                continue
            if currP and not currQ or not currP and currQ:
                return False
            if currP.val != currQ.val:
                return False
            visit.append((currP.left, currQ.left))
            visit.append((currP.right, currQ.right))
        
        return True