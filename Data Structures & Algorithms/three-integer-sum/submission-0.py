class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)
        print(nums)

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            targetSum = -nums[i]
            while left < right:
                if left == i:
                    left += 1
                if right == i:
                    right -= 1
                
                if nums[left] + nums[right] < targetSum:
                    left += 1
                elif nums[left] + nums[right] > targetSum:
                    right -= 1
                else:
                    if [nums[i], nums[left], nums[right]] not in results:
                        results.append([nums[i], nums[left], nums[right]])
                    left += 1
        return results


            