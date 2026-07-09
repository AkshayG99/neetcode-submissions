class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        globalMax = 0
        for num in nums:
            if num - 1 in nums:
                continue
            localMax = 0
            while num in nums:
                localMax += 1
                num += 1
            globalMax = max(globalMax, localMax)
        return globalMax


