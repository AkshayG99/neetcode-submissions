class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        l, r = 0, k - 1
        for i in range(0, k):
            heapq.heappush_max(heap, (nums[i], i))

        while r < len(nums):
            if l !=0:
                heapq.heappush_max(heap, (nums[r], r))
            while not (l <= heap[0][1] <= r):
                heapq.heappop_max(heap)
            res.append(heap[0][0])
            l+=1
            r+=1

        return res




            


