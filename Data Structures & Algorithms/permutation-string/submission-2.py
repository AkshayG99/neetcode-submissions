class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1) - 1
        print(len(s2) - windowSize - 1)
        for i in range(len(s2) - windowSize):
            if sorted(s2[i:i+windowSize+1]) == sorted(s1):
                return True
        return False