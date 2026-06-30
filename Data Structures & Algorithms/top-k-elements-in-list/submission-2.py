class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArr = [[] for i in range(len(nums) + 1)]
        #index is frequency
        #value is list of numbers with that frequency

        count = defaultdict(int)
        #key : number
        #value : number of repitions
        for i in range(len(nums)):
            count[nums[i]] = count[nums[i]] + 1

        for num, freq in list(count.items()):
            countArr[freq].append(num)
        
        topK = []
        
        for i in range(len(countArr) - 1, -1, -1):
            for num in countArr[i]:
                topK.append(num)
                if len(topK) == k:
                    return topK