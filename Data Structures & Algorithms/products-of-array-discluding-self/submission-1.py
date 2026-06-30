class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            ans = 1
            before = nums[0:i]
            after = nums[(i+1)::]
            for j in before:
                ans *= j
            for j in after:
                ans *= j
            output.append(ans)
        return output

            