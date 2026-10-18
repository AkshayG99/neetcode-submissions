class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = defaultdict(int)

        for num in nums:
            freqCounter[num] += 1 
        
        heap = []

        for num, freq in freqCounter.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        res = []
        for i in heap:
            res.append(i[1])
        return res
        


