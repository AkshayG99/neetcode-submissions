class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}
        
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in seenMap.keys():
                return [seenMap[compliment], idx]
            seenMap[num] = idx