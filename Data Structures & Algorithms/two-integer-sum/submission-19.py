class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            goal = target - nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] == goal:
                    idx2 = j
                    return([i,j])