class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}":"{", ")":"(", "]":"["}

        stack = []

        for c in s:
            if c not in mapping:
                #c is an open bracket
                stack.append(c)
                continue
            #c is a closed bracket
            if not stack or stack[-1] != mapping[c]:
                #brackets dont match
                return False
            stack.pop()
        
        if not stack:
            return True
        return False
            