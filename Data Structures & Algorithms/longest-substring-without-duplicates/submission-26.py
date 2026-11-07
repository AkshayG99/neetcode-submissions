class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}

        l = 0
        longest = 0

        for r, char in enumerate(s):
            if char in mp:
                l = max(mp[char] + 1, l)
            mp[char] = r
            longest = max(longest,r - l + 1)
        
        return longest
