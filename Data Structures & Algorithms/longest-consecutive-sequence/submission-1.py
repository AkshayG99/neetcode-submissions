class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        globalMax = 1
        for num in nums:
            localMax = 1
            nextNum = num + 1
            while nextNum in nums:
                localMax += 1 
                nextNum += 1
            globalMax = max(globalMax, localMax)
        return globalMax

