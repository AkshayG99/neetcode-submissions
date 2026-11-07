class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 0
        longest = 0
        seen = set()

        for p2, val in enumerate(s):
            while val in seen:
                seen.remove(s[p1])
                p1 += 1
            
            seen.add(val)
            longest = max(longest, p2 - p1 + 1)

        return longest