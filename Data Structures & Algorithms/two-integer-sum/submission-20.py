class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for idx, val in enumerate(nums):
            goal = target - val 
            if goal in prevMap:
                return [prevMap[goal], idx]
            prevMap[val] = idx
        