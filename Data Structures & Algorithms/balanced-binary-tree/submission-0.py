# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return [True, 0]
            l, r = 0, 0

            if root.left:
                l += 1 + dfs(root.left)[1]
            if root.right:
                r += 1 + dfs(root.right)[1]
            
            if abs(l-r) > 1:
                self.balanced = False
    
            
            return [True, max(l, r)]

        dfs(root)
        return self.balanced
            

        