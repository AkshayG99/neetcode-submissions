class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lowerIndex, upperIndex = 0, 0
        substring = []
        longest = 0

        while upperIndex < len(s):
            if not substring:
                substring.append(s[lowerIndex])
                upperIndex += 1
                continue
            if s[upperIndex] in substring:
                longest = max(longest, len(substring))
                while s[upperIndex] in substring:
                    substring.pop(0)
                lowerIndex += 1
            substring.append(s[upperIndex])
            upperIndex += 1
        return max(longest, len(substring))