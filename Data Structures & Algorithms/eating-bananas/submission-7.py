class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)

        while minK <= maxK:
            midK = (minK + maxK) // 2

            localTime = 0
            for pile in piles:
                localTime += (pile + midK - 1) // midK
            if localTime <= h:
                maxK = midK - 1
            else:
                minK = midK + 1
            
        

        return minK

            
