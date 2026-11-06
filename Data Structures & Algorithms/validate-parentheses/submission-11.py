class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for i in s:
            #open bracket
            if i in mapping:
                stack.append(i)
                continue
            #closed bracket
            if not stack or i != mapping[stack.pop()]:
                return False
        
        return not stack
            