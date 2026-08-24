class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [1] * len(nums)

        for num in nums:
            seen[num - 1] -= 1
            if seen[num - 1] < 0:
                return num
        