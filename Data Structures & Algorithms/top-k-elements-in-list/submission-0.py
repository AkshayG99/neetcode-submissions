class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1 
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        print(arr)

        i = 0
        topK = []
        
        while i < k:
            topK.append(arr[len(arr) - 1][1])
            arr.pop()
            i += 1
        return topK