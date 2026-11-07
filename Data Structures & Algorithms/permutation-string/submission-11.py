class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for c in s1:
            s1Count[c] = 1 + s1Count.get(c, 0)
        
        s2Count = {}
        l = 0
        length = len(s1)

        for r, c in enumerate(s2):
            if s2Count == s1Count:
                return True
            if (r-l) < length:
                s2Count[c] = 1 + s2Count.get(c, 0)
            else:
                if s2Count[s2[l]] > 1:
                    s2Count[s2[l]] -= 1
                else:
                    s2Count.pop(s2[l])
                s2Count[c] = 1 + s2Count.get(c, 0)
                l += 1
        return s1Count == s2Count
                
