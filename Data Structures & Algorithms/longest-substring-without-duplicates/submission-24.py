class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 0
        longest = 0
        seen = set()

        while p2 < len(s):
            if p1 == p2:
                seen.add(s[p1])
                p2 += 1
            elif s[p2] in seen:
                longest = max(longest, p2-p1)
                while s[p2] in seen:
                    seen.remove(s[p1])
                    p1 += 1
            else:
                seen.add(s[p2])
                p2 += 1
        longest = max(longest, p2-p1)
        return longest