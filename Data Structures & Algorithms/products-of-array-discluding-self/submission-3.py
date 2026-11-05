class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [0] * n
        for i in range(0,n):
            if i == 0:
                prefix[i] = nums[i]
                postfix[n-1-i] = nums[n-1-i]
                continue
            prefix[i] = prefix[i-1] * nums[i] 
            postfix[n-1-i] = postfix[n-i] * nums[n-1-i] 
        for i in range(0,n):
            before = prefix[i-1] if i !=0 else 1
            after = postfix[i+1] if i !=n-1 else 1 
            res[i] = before * after
        
        return res
            