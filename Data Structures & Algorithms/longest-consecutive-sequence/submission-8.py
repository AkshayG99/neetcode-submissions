class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 in numSet:
                continue
            localMax = 1
            while (num + localMax in numSet):
                localMax += 1
            longest = max(longest, localMax)
        
        return longest
