class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while True:
            store = nums[i]
            if nums[i] == -1:
                return i
            nums[i] = -1

            i = store