class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0] * 26
        countT = [0] * 26

        for char in s:
            countS[ord(char) - 97] += 1
        for char in t:
            countT[ord(char) - 97] += 1
        if countS == countT:
            return True
        return False