[12,13,14,15,1,2,3,4,5,6,7,8,9,10,11]
[5,6,7,8,9,10,11,0,1,2,3,4]
#lowest number found when previous number > current number

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[(0+len(nums))//2] <= nums[-1]:
                return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left+right) // 2
         
            if nums[middle] > nums[right]: #left is sorted array, therefore search right
                left = middle + 1
            else: #right is the sorted array, so search left
                right = middle 
            
        return nums[left]