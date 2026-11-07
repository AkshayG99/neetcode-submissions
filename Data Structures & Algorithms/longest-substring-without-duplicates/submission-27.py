class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}

        l = 0
        longest = 0
        r = 0
        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            longest = max(longest,r - l + 1)

            r+= 1
        
        return longest
